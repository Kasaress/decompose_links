from django.urls import path

from .views import LinksView

app_name = 'api'


urlpatterns = [
    path('v1/links/', LinksView.as_view()),
]
