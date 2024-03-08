from django.contrib import admin
from django.urls import path
from myapp.views import page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/<int:page_num>/', page),
]