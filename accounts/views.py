from django.shortcuts import render
from rest_framework.views import APIView
from django.views import View
from django.db.models import Q
import json
from django.urls import reverse_lazy
# Create your views here.
from .serializers import GroupSerializer
from django.utils import timezone
from django.shortcuts import render
from .forms import PermissionCreationForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
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

from accounts.forms import PermissionForm,CustomUserUpdateForm, GroupUpdateForm, GroupCreationForm,GroupAddForm, AdminResetUserPassword ,CustomUserLoginForm,CustomPasswordChangeForm
from django.utils import timezone
import random
import string
from django.core.mail import send_mail
import logging
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.http import HttpResponseForbidden

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        # Vérifie si l'utilisateur est authentifié et s'il est un superutilisateur
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def handle_no_permission(self):
        # Redirige l'utilisateur vers une page d'interdiction d'accès s'il n'est pas un superutilisateur
        return HttpResponseForbidden("Vous n'êtes pas autorisé à accéder à cette page.")

def is_superuser(user):
    return user.is_authenticated and user.is_superuser

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
            selected_groups  = form.cleaned_data["groups"]
            
            print(user)
            user.reset_by_admin = True   

            user.save()
            if selected_groups:
                for group in selected_groups:
                    
                    user.groups.add(group)
                    user.save()
                    for permission_ in group.permissions.all():
                        assign_perm(permission_, user)
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


@login_required
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
def list_groups(request):
    groups = Group.objects.all()
    return render(request, 'list_groups.html', {'groups': groups})

class GroupListView(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    model = Permission
    template_name = 'accounts/list_groups.html'
    context_object_name = 'groups'
    def get(self, request, *args, **kwargs):
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = Group.objects.all()
        # Vérifier le type du paramètre et trier en conséquence
        if q : 
           
          queryset = Group.objects.filter(
                              Q(name__icontains=q) |
                              Q(permissions__content_type__model__icontains=q) | 
                              Q(permissions__codename__icontains=q) |    
                              Q(permissions__name__icontains=q)).distinct()
        # Passer le queryset trié au template
        
        context = {'groups': queryset}
        return render(request, self.template_name, context)



class GroupDetailView(LoginRequiredMixin,SuperuserRequiredMixin,DetailView):
    model = Group
    template_name = 'accounts/detail_groups.html'
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupérer l'historique de la relation many-to-many 'cluster'
        permissions = self.object.permissions.all()
        
        
        serializer = GroupSerializer(self.object)
        #serializer_data=json.dumps(serializer.data)
        #context['serializer_data'] = serializer_data      
        context['permissions'] = permissions
        return context
@login_required
@user_passes_test(is_superuser)
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
            group.created = timezone.now() 
            group.permissions.set(selected_permissions)
            group.save()
            return redirect('base:index')
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
def edit_group(request, group_id):
    user = User.objects.get(email=request.user.email)
    user_ip = get_client_ip(request)
    
    group = get_object_or_404(Group, id=group_id)
    original_permissions = list(group.permissions.all())
    
    if request.method == 'POST':
        form = GroupUpdateForm(request.POST)
        if form.is_valid():
            selected_permissions = request.POST.getlist('permissions')
            name = form.cleaned_data["name"]
            historical_change_reason = form.cleaned_data["historical_change_reason"]

            # Appliquez les modifications au groupe
            group.name = name
            group.save()
            group.permissions.set(selected_permissions)
            group.updated = timezone.now() 
            group.save()
            # Enregistrez l'historique des modifications avec la raison du changement
            history_snapshot = group.history.latest()
            history_snapshot.history_change_reason = historical_change_reason
            history_snapshot.save()

            logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s groupe modifie :%s par admin. Historique des modifications avec raison : %s', user.email, user.pk, user.date_joined.date(), user.is_active, user.last_login.date(), user.last_password_change, user_ip, name, historical_change_reason)
            return redirect('accounts:list-groups')
        else:
            logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s echecs de la tentative de modification de groupe par admin, entrée invalide ', user.email, user.pk, user.date_joined.date(), user.is_active, user.last_login.date(), user.last_password_change, user_ip)
    else:
        # Pré-remplissez le formulaire avec les données actuelles du groupe
        form = GroupUpdateForm(initial={'name': group.name, 'historical_change_reason': ''})
        form.fields['permissions'].queryset = Permission.objects.all()
        form.fields['permissions'].initial = [perm.id for perm in original_permissions]

    context = {'form': form, 'group': group}
    return render(request, 'accounts/create_groupe.html', context)

@login_required
@user_passes_test(is_superuser)
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
                user.save()
                user.groups.add(group_)
                for permission_ in group_.permissions.all():
                    assign_perm(permission_, user)
                    user.save()
                #assign_perm(group_, user)
                logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s groupe:%s attribuer à  :%s par admin ',user_.email,user_.pk,user_.date_joined.date(),user_.is_active,user_.last_login.date(),user_.last_password_change,user_ip,name,user.username)
                return redirect('base:index')
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
            return redirect('accounts:list-permissions')
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





class PermissionListView(LoginRequiredMixin,SuperuserRequiredMixin,ListView):
    model = Permission
    template_name = 'accounts/list_permissions.html'
    context_object_name = 'permissions'
    def get(self, request, *args, **kwargs):
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = Permission.objects.all()
        # Vérifier le type du paramètre et trier en conséquence
        if q : 
          queryset = Permission.objects.filter(
                              Q(name__icontains=q) |
                              Q(codename__icontains=q) |    
                              Q(content_type__model__icontains=q) | 
                              Q(group__name__icontains=q)      
                              )
        # Passer le queryset trié au template
        
        context = {'permissions': queryset}
        return render(request, self.template_name, context)

@login_required
@user_passes_test(is_superuser)
def create_permission(request):
    user = User.objects.get(email=request.user.email)
    user_ip = get_client_ip(request)
    
    if request.method == 'POST':
        form = PermissionCreationForm(request.POST)
        if form.is_valid():
            # Enregistrez la permission
            permission = form.save(commit=False)
            permission.created = timezone.now() 
            permission.save()
            logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s nouvelle permission creee : %s par admin', user.email, user.pk, user.date_joined.date(), user.is_active, user.last_login.date(), user.last_password_change, user_ip, form.cleaned_data["name"])

            return redirect('accounts:list-permissions')
        else:
            logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s echecs de la tentative de creation de permission par admin, entree invalide ', user.email, user.pk, user.date_joined.date(), user.is_active, user.last_login.date(), user.last_password_change, user_ip)
    else:
        form = PermissionCreationForm()

    context = {'form': form}
    return render(request, 'accounts/create_permission.html', context)


@login_required
@user_passes_test(is_superuser)
def edit_permission(request, permission_id):
    permission = get_object_or_404(Permission, id=permission_id)

    if request.method == 'POST':
        form = PermissionForm(request.POST, instance=permission)
        if form.is_valid():
            form.save()
            return redirect('accounts:list_permissions')
    else:
        form = PermissionForm(instance=permission)

    return render(request, 'accounts/edit_permission.html', {'form': form, 'permission': permission})



def logout_view(request):
    user_ip = get_client_ip(request)
    user_ = User.objects.get(email=request.user.email)
    logger.info('user email: %s user id: %s user date joined: %s account status: %s last connexion: %s last password change: %s to ip adress :%s  disconnected ',user_.email,user_.pk,user_.date_joined.date(),user_.is_active,user_.last_login.date(),user_.last_password_change,user_ip)
    logout(request)
    return redirect('base:index')  # logout


#######################user management views##############

class UserListView(LoginRequiredMixin,SuperuserRequiredMixin,View):
    template_name = 'accounts/list_users.html'

    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        parametre = request.GET.get('parametre')
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = User.objects.all()

        # Vérifier le type du paramètre et trier en conséquence
        if parametre:
            group = Group.objects.get(pk=parametre)
            
            # Afficher les users liées à un objet Cluster
            queryset = group.user_set.all()
            print(queryset)
        elif q : 
            queryset = User.objects.filter(
                            Q(first_name__icontains=q) |
                            Q(last_name__icontains=q) |
                            Q(username__icontains=q) |  
                            Q(email__icontains=q) |   
                            Q(departement__name__icontains=q) |         
                            Q(groups__name__icontains=q)|
                            Q(user_permissions__name__icontains=q)|
                            Q(user_permissions__codename__icontains=q)).distinct()  
        # Passer le queryset trié au template
        print(queryset)
        groups =  Group.objects.all()
        context = {'users': queryset}
        return render(request, self.template_name, context)

class UserDetailView(LoginRequiredMixin,SuperuserRequiredMixin,DetailView):
    model = User
    template_name = 'accounts/user_detail.html'
    context_object_name = 'user'


class UserUpdateView(LoginRequiredMixin,SuperuserRequiredMixin,UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = 'accounts/sign.html'
    success_url = reverse_lazy('accounts:user-list')

class UserDeleteView(LoginRequiredMixin,SuperuserRequiredMixin,DeleteView):
    model = User
    template_name = 'accounts/user_confirm_delete.html'
    success_url = reverse_lazy('accounts:user-list')
