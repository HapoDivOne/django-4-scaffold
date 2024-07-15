from users import views
from users.views import UserApi, UserRegister, LogoutView, UserExport
from django.urls import path, include  # Ensure `include` is imported
from rest_framework import routers
from rest_framework.permissions import IsAuthenticated

urlpatterns = [
    path('user/register', UserRegister.as_view({'post': 'register'})),
    path('user/list', UserApi.as_view({'get': 'list'})),
    path('user/show/<int:id>', UserApi.as_view({'get': 'show'})),
    path('user/delete/<int:id>', UserApi.as_view({'delete': 'delete'})),
    path('user/update/<int:id>', UserApi.as_view({'post': 'update'})),
    path('user/logout', LogoutView.as_view({'post': 'logout'}),name='logout'),
    path('user/export-csv', UserExport.as_view({'post': 'export_csv'}),name='export_csv'),
    path('user/export-pdf', UserExport.as_view({'post': 'export_pdf'}),name='export_pdf'),
    path('user/export-xlsx', UserExport.as_view({'post': 'export_xlsx'}),name='export_xlsx')
]
