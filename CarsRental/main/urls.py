from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about_view, name="about"),
    path("password/generate/", views.password, name="password"),
    path("get-json/", views.get_json, name="get_json"),

]