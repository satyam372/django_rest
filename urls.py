"""
URL configuration for Createapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.urls import path
from .views import CustomTokenObtainPairView
from .views import SecureEndpoint , Registercomplaint
from django.conf import settings
from django.conf.urls.static import static



from . import views


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Createapi import views  # Import your views module
from Createapi.views import SecureEndpoint, CustomTokenObtainPairView, Registercomplaint,Registercomplaint_2,CombinedComplaintsView
# from .views import ComplaintDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('show/', views.showemp, name='showemp'),  # Ensure that you import the views module correctly
    path('validate/', views.validate, name='validate'),  # Ensure that you import the views module correctly
    path('secure-endpoint/', SecureEndpoint.as_view(), name='secure_endpoint'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('Register-complaint/', Registercomplaint.as_view(), name='Registercomplaint'), # registring 1st part of complaint
    path('Register-complaint_2/', Registercomplaint_2.as_view(),name='Registercomplaint_2'), # refistring 2nd part of complaint
    path('employee-complaints/<int:emp_id>/', CombinedComplaintsView.as_view(), name='complaints_by_employee'),
 # api to retrive complaint
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # to save the image to a directory