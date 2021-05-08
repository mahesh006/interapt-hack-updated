from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('',views.home,name='home'),
    path('search',views.search,name='search'),
    path('search_project',views.search_project,name='search-project'),
    path('project-list',views.project_list,name='project-list'),
    path('search-ongoingproject',views.search_ongoingproject,name='search-ongoingproject'),
    path('search-completedproject',views.search_completedproject,name='search-completedproject'),
    path('role-list',views.role_list,name='role-list'),
    path('employee-list',views.employee_list,name='employee-list'),
    path('project-employee-list/<int:cat_id>',views.project_employee_list,name='project_employee-list'),
    path('role-employee-list/<int:brand_id>',views.role_employee_list,name='role_employee-list'),
    path('employee/<str:slug>/<int:id>',views.employee_detail,name='employee_detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
   
