from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from pg_app import views

router = routers.DefaultRouter()
router.register(r'pg_app',  views.PropertyView, 'property')

urlpatterns = [
    # path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
