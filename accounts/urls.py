from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path('login/',views.loginn,name="loginn"),
    path('logout/',views.logoutt,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('profileRegister',views.profileregister,name="profileregister"),
    path('profileedit/',views.ProfileEdit,name='profileedit')

]
