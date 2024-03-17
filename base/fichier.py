
path('app_deployment', views.AppServerListView.as_view(), name='app_deployment-list'),
path('app_deployment/<int:pk>/', views.AppServerDetailView.as_view(), name='detail-app_deployment'),
path('app_deployment/<int:pk>/update/', views.AppServerUpdateView.as_view(), name='update-app_deployment'),
path('app_deployment/create', views.AppServerCreateView.as_view(), name='create-app_deployment'),
path('app_deployment/<int:pk>/delete/', views.AppServerDeleteView.as_view(), name='delete-app_deployment'),
