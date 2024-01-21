from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from accounts.models import User
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.decorators import user_passes_test
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from guardian.shortcuts import  assign_perm
from django.contrib import messages
from accounts.forms import PermissionForm, GroupCreationForm,GroupAddForm, AdminResetUserPassword ,CustomUserLoginForm,CustomPasswordChangeForm
from django.utils import timezone
import random
import string
from django.core.mail import send_mail
import logging

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


logger = logging.getLogger(__name__)
def send_password_email(email,password):
    # Créez le contenu de l'e-mail
    user_ = User.objects.get(email=email)
    print(user_)
  
    subject = 'Demande de réinitialisation de mot de passe'
    message = f"Bonjour {user_.first_name}.\n"
    message += f"Vous avez fais une demande de réinitialisation de mot de passe pour le compte : {user_.username} .\n"
    message += f"Votre mot de passe est  : {password} .\n"    
    
    from_email = 'jozacoder@gmail.com'  # Remplacez par votre adresse e-mail
    recipient_list = [user_.email]  # Adresse e-mail du destinataire (utilisateur)
    send_mail(subject, message, from_email, recipient_list)



def generate_random_password(taille):
    # Définissez les caractères possibles pour chaque catégorie
    taille_= int(taille)
    digits = string.digits
    special_chars = '!@#$%^&*()_-+=<>?'
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase

    # Concaténez tous les caractères possibles
    all_chars = digits + special_chars + uppercase_letters + lowercase_letters

    # Générez un mot de passe aléatoire de 14 caractères
    random_password = ''.join(random.choice(all_chars) for _ in range(taille_))

    # Vous pouvez renvoyer le mot de passe dans la réponse JSON
    return random_password


def is_superuser(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(is_superuser)
def signup(request):
    print(request.user.username)
    user_ip = get_client_ip(request)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            is_staff = form.cleaned_data["is_staff"]
            if is_staff == True:
                password = generate_random_password(14)
                form.cleaned_data["password1"]=password
            else:
                password = generate_random_password(12)
                form.cleaned_data["password1"]=password
            user = form.save(commit=False)
            print(user)
            user.reset_by_admin = True      
            user.save()
            send_password_email(user.email,password)
            logger.info('user email: %s user id: %s user date joined: %s account status: %s  compte utilisateur creer par admin  to ip adress :%s ',user.email,user.pk,user.date_joined.date(),user.is_active,user_ip)
            return redirect('base:index')  # Remplacez 'home' par le nom de votre page d'accueil
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/sign.html', {'form': form})

@login_required
def reset_password(request):
    user_ip = get_client_ip(request)
    user = User.objects.get(email=request.user.email)

    if  user.reset_by_admin == True or user.age_of_last_password_change > 1:
        if request.method == 'POST':
            form = CustomPasswordChangeForm(user=user,data=request.POST)
            if form.is_valid():             
                password = form.cleaned_data["new_password1"]
                user.set_password(password)
                user.last_password_change = timezone.now().date()
                user.reset_by_admin = False
                user.save()
                logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s  mot de passe réinitialiser par utilisateur ',user.email,user.pk,user.date_joined.date(),user.is_active,user.last_login.date(),user.last_password_change,user_ip)
                user_ = authenticate(request, username=user.email, password=password)
                login(request, user_,backend='django.contrib.auth.backends.ModelBackend')
                print(user.last_password_change,user.last_login)
                return redirect('base:index')  # Remplacez 'home' par le nom de votre page d'accueil
           
        else:
            form = CustomPasswordChangeForm(user=user)
        return render(request, 'accounts/change_password.html', {'form': form})
    
    elif user.age_of_last_password_change < 1: 
        print(user.age_of_last_password_change)
        logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s  tentative de reinitialisation password too young ',user.email,user.pk,user.date_joined.date(),user.is_active,user.last_login.date(),user.last_password_change,user_ip)
        return redirect('base:index') 
    else:   
        print('bizare')
        return redirect('base:index') 


@user_passes_test(is_superuser)
def admin_reset_user_password(request):
    user_ip = get_client_ip(request)
    q= request.GET.get('q') if request.GET.get('q') != None else ''

    
    print(q)
    if request.method == 'POST':
        form = AdminResetUserPassword(request.POST)
        if form.is_valid():          
            user = get_object_or_404(User, id=request.POST['user'])
            if user.is_staff == True:
                password = generate_random_password(14)
            elif user.is_staff == False:
                password = generate_random_password(12)
            logger.info('user email: %s user id: %s user date joined: %s account status: %s to ip adress :%s  mot de passe réinitialiser par admin ',user.email,user.pk,user.date_joined.date(),user.is_active,user_ip)
            user.set_password(password)
            send_password_email(user.email,password)
            user.reset_by_admin = True
            user.save()                
    else:
        if q: 
            user_instance = User.objects.get(username=q)
            print(user_instance)
            form = AdminResetUserPassword(initial={'user': user_instance})
        else : 
            form = AdminResetUserPassword()
    context = {'form':form}
    return render(request, 'accounts/admin_reset_user_password.html',context)

def custom_login(request):
    user_ip = get_client_ip(request)
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST) 
        if form.is_valid():
            email = form.cleaned_data["email"]
            print(email)
            password = form.cleaned_data["password"]
            print(password)
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                user_ = User.objects.get(email=email)
                print(user_.reset_by_admin)
                if user_.reset_by_admin==True:
                    print("reset b admin")
                    logger.info('user email: %s user id: %s user date joined: %s account status: %s to ip adress :%s  utilisateur jamais connecté redirigé vers reset password ',user_.email,user_.pk,user_.date_joined.date(),user_.is_active,user_ip)
                    login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('accounts:change-password') 
                else:
                    if user_.age_of_last_password_change > 90 :  
                        logger.warning('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s  password age too long ',user_.email,user_.pk,user_.date_joined.date(),user_.is_active,user_.last_login.date(),user_.last_password_change,user_ip)
                        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                        return redirect('accounts:change-password')
                    else:   
                        logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s  connected ',user_.email,user_.pk,user_.date_joined.date(),user_.is_active,user_.last_login.date(),user_.last_password_change,user_ip)
                        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                        
                        return redirect('base:index')    
            else:
                
                logger.warning('tentative de connexion echoué au compte %s depuis ip adress :%s',email,user_ip)
    else:
        form = CustomUserLoginForm()
        
    context = {'form': form}
    return render(request, 'accounts/login.html', context)




@login_required
@user_passes_test(is_superuser)
@permission_required('auth.change_permission', raise_exception=True)
@permission_required('auth.delete_permission', raise_exception=True)
@permission_required('auth.add_permission', raise_exception=True)
def create_group(request):
    user = User.objects.get(email=request.user.email)
    user_ip = get_client_ip(request)
    permissions = Permission.objects.all()
    print(permissions)
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            selected_permissions = request.POST.getlist('permissions')
            name = form.cleaned_data["name"]
            group = Group.objects.create(name=name)
            group.permissions.set(selected_permissions)
            logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s  nouveau groupe :%s creer par admin ',user.email,user.pk,user.date_joined.date(),user.is_active,user.last_login.date(),user.last_password_change,user_ip,name)
        # Attribuer les permissions à l'utilisateur
        else:
            logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s  echecs de la tentative de création de groupe par admin, entrée invalide ',user.email,user.pk,user.date_joined.date(),user.is_active,user.last_login.date(),user.last_password_change,user_ip)   
    else:
        form = GroupCreationForm()
    context = {'form':form}
    return render(request, 'accounts/create_groupe.html',context)

@login_required
@user_passes_test(is_superuser)
@permission_required('accounts.modifier_user', raise_exception=True)
@permission_required('accounts.lire_user', raise_exception=True)
@permission_required('accounts.ajouter_user', raise_exception=True)
@permission_required('accounts.supprimer_user', raise_exception=True)
def add_user_to_group(request):
    user_ip = get_client_ip(request)
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    permissions = Permission.objects.all()
    print(permissions)
    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            user_ = User.objects.get(email=request.user.email)
            selected_groups = request.POST.getlist('group')
            user = get_object_or_404(User, id=request.POST['user'])
            for group in selected_groups:
                group_ = Group.objects.get(id=group)
                name = group_.name
                print(group_)
                user.groups.add(group_)
                for permission_ in group_.permissions.all():
                    assign_perm(permission_, user)
                    user.save()
                #assign_perm(group_, user)
                logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s groupe:%s attribuer à  :%s par admin ',user_.email,user_.pk,user_.date_joined.date(),user_.is_active,user_.last_login.date(),user_.last_password_change,user_ip,name,user.username)
        else:
            logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s echec attribution groupe à  :%s par admin ',user_.email,user_.pk,user_.date_joined.date(),user_.is_active,user_.last_login.date(),user_.last_password_change,user_ip,user.username)
    else:
        if q:
            user_instance = User.objects.get(username=q)
            form = GroupAddForm(initial={'user': user_instance})
        else:
            form = GroupAddForm()
    context = {'form':form}
    return render(request, 'accounts/assign_group.html',context)

@login_required
@user_passes_test(is_superuser)
@permission_required('auth.change_permission', raise_exception=True)
@permission_required('auth.delete_permission', raise_exception=True)
@permission_required('auth.add_permission', raise_exception=True)
def assign_permissions(request):
    user_ip = get_client_ip(request)
    permissions = Permission.objects.all()
    user_ = User.objects.get(email=request.user.email)
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    if request.method == 'POST':
        form = PermissionForm(request.POST)
        if form.is_valid():
            selected_permissions = request.POST.getlist('permissions')
            user = get_object_or_404(User, id=request.POST['user'])
        # Attribuer les permissions à l'utilisateur
            for permission in selected_permissions:
                permission_ = Permission.objects.get(id=permission)
                name = permission_
                assign_perm(permission_, user)
                logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s permission:%s attribuer à  :%s par admin ',user_.email,user_.pk,user_.date_joined.date(),user_.is_active,user_.last_login.date(),user_.last_password_change,user_ip,name,user.username)
            messages.success(request, 'Permissions attribuées avec succès.')
    else:
        if q:
            user_instance = User.objects.get(username = q)
            permission_instance = user_instance.user_permissions.all()
            print(permission_instance)
            form = PermissionForm(initial={'user': user_instance,'permissions':permission_instance})
        else :
            form = PermissionForm()
    context = {'form':form}
    return render(request, 'accounts/assign_permissions.html',context)


def logout_view(request):
    user_ip = get_client_ip(request)
    user_ = User.objects.get(email=request.user.email)
    logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s  disconnected ',user_.email,user_.pk,user_.date_joined.date(),user_.is_active,user_.last_login.date(),user_.last_password_change,user_ip)
    logout(request)
    return redirect('base:index')  # logout