from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('SignUp',views.SignUp),
    path('Login',views.login),
    path('Logout',views.logout),
    path('addBlog',views.addBlog),
    path('updateBlog/<id>',views.updateBlog),
]