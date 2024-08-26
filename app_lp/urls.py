from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('admin_user', admin_dashboard, name='adm'),
]