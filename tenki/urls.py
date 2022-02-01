from django.urls import path
from . import views

app_name    = "tenki"
urlpatterns = [
    path('', views.index, name="index"),

    #ここのtest/の部分はuuidを使うなどして予測されないように仕立てる。
    path('test/', views.admin, name="admin"),
]
