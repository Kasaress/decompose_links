
from django.contrib import admin
from django.urls import include, path

from .views import redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', redirect_view)
]
