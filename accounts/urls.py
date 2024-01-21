from django.urls import path
from accounts import views
app_name='accounts'

urlpatterns = [


path('signup/', views.signup, name='signup'),
path('login/',views.custom_login, name="login"),
path('reset_password/',views.reset_password, name="change-password"),
path('assign-permissions/', views.assign_permissions, name='assign-permissions'),
path('create-group/', views.create_group, name='create-group'),
path('add-user-to-group/', views.add_user_to_group, name='add-user-to-group'),
path('change-password/', views.reset_password, name='change-password'),
path('admin-reset-user/', views.admin_reset_user_password, name='admin-reset-user'),
path('logout/', views.logout_view, name='logout'),
]