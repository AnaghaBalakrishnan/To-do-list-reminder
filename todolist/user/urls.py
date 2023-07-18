from django.urls import path
from .views import viewreminder,DeleteReminder,updateRem,SignUp,Signin,Addreminder

urlpatterns = [
    path('vreminder',viewreminder.as_view(),name='viewreminder'),
    path('drmdr/<int:rid>',DeleteReminder.as_view(),name='drmdr'),
    path('urmdr/<int:rid>',updateRem.as_view(),name='urmdr'),
    path('signup',SignUp.as_view(),name='signup'),
    path('',Addreminder.as_view(),name="addreminder")
    

]
