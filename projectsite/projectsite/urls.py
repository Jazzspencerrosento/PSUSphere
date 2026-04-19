from django.contrib import admin
from django.urls import path
from studentorg.views import (
    HomePageView, 
    OrganizationList, 
    OrganizationCreateView, 
    OrganizationUpdateView, 
    OrganizationDeleteView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'), 
    
    # Organization URLs
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'), 
    path('organization_list/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),
    
    # COMMENTED OUT because ProgramCreateView is not defined in views.py
    # path('program/add/', ProgramCreateView.as_view(), name='program-add'),
]