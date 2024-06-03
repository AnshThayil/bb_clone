"""bb_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from boulders.views import BoulderDetailApi, BoulderCreateApi
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = 'BB Clone API',
        default_version='v1'
    )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gyms.urls')),
    path('boulder/', include('boulders.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/user', user_views.UserList.as_view(), name='user-list'),
    path('api/user/<int:pk>', user_views.UserDetail.as_view(), name='user-detail'),
    path('api/group', user_views.GroupList.as_view(), name='group-list' ),
    path('api/group/<int:pk>', user_views.GroupDetail.as_view(), name='group-detail'),
    path('api/boulder/<int:pk>', BoulderDetailApi.as_view(), name='boulder-detail'),
    path('api/boulder', BoulderCreateApi.as_view(), name='boulder-create'),
    path('api/auth', views.obtain_auth_token, name='auth-token'),
    path('api', schema_view.with_ui('swagger'), name='api-doc')
]
