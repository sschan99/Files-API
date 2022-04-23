from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from files import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('files/', views.FileRootList.as_view(), name='file-root-list'),
    path('files/<path:path>/', views.FileList.as_view(), name='file-list'),
    path('file/<int:pk>/', views.FileDetail.as_view(), name='file-detail'),
])
