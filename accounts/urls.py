from django.urls import path
from accounts import views
app_name='accounts'

urlpatterns = [


path('signup/', views.signup, name='create-user'),
path('login/',views.custom_login, name="login"),
path('reset_password/',views.reset_password, name="change-password"),
path('assign-permissions/', views.assign_permissions, name='assign-permissions'),
path('create-permission/', views.create_permission, name='create-permissions'),
path('list-permissions/', views.PermissionListView.as_view(), name='list-permissions'),
path('list-groups/', views.GroupListView.as_view(), name='list-groups'),
path('detail-group/<int:pk>/', views.GroupDetailView.as_view(), name='detail-groups'),

path('create-group/', views.create_group, name='create-groups'),
path('edit-group/<int:group_id>/', views.edit_group, name='edit-groups'),
path('add-user-to-group/', views.add_user_to_group, name='add-user-to-groups'),
path('change-password/', views.reset_password, name='change-password'),
path('admin-reset-user/', views.admin_reset_user_password, name='admin-reset-user'),
path('logout/', views.logout_view, name='logout'),

path('user', views.UserListView.as_view(), name='user-list'),
path('user/<int:pk>/', views.UserDetailView.as_view(), name='detail-user'),
path('user/<int:pk>/update/', views.UserUpdateView.as_view(), name='update-user'),

]