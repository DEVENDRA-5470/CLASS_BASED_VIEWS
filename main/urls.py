from django.urls import path
from main.views import *

urlpatterns = [
    path('',homeview.as_view(),name="home"),
    path('about/',aboutview.as_view(),name="about"),
    path('sign_up/',sign_up.as_view(),name="sign_up"),
    path('register/',register.as_view(template_name="register.html"),name="register"),



    # crud
    path('create_view/',create_view.as_view(),name="create_view"),
    path('delete_view/<int:id>',delete_view.as_view(),name="delete_view"),
    path('update_view/<int:id>/',update_view.as_view(),name='update_view'),
]

