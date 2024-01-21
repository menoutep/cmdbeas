path('module_applicatif', views.ModuleApplicatifListView.as_view(), name='module_applicatif-list'),
path('module_applicatif/<int:pk>/', views.ModuleApplicatifDetailView.as_view(), name='detail-module_applicatif'),
path('module_applicatif/<int:pk>/update/', views.ModuleApplicatifUpdateView.as_view(), name='update-module_applicatif'),
path('module_applicatif/create', views.ModuleApplicatifCreateView.as_view(), name='create-module_applicatif'),
path('module_applicatif/<int:pk>/delete/', views.ModuleApplicatifDeleteView.as_view(), name='delete-module_applicatif'),