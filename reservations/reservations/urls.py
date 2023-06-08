"""reservations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# swagger
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

description = '''
<img src="https://media.licdn.com/dms/image/C4D0BAQEoDcRay1vjng/company-logo_200_200/0/1647283602276?e=2147483647&v=beta&t=mh_4cXfdaPARrbA1_kC_4UqmqjBO-XAH3XWGVZ6fu7k">
</br>
</br>
<h2>APIs Doc</h2>
'''

schema_view = get_schema_view(
  openapi.Info(
     title="Booking system",
     default_version='1.0.0',
     description=description,
  ),
  public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include('core.api.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
