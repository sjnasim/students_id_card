from xml.dom.minidom import Document
from django.urls import path , re_path
from . import views
from django.utils.http import urlencode
import urllib

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.home, name="home"),
    
   

    path('create_emp/', views.createEmp, name="create_emp"),
    path('update_emp/<str:pk>', views.updateEmp, name="update_emp"),

    path('employee/authentication.html?emp_id=<str:pk>', views.idCard, name="id"),

    path('login/', views.loginPage, name="login"), 
    path('logout/', views.logoutUser, name="logout"),



]

urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)