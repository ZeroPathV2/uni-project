
from django.urls import path
from .views import login_user, logout_user, main, register_user,spotify,youTube

app_name = 'frontend'

urlpatterns = [
    path('home',main),
    path('spotify',spotify),
    path('youtube',youTube),
    path('log-in',login_user),
    path('log-out',logout_user),
    path('sign-up',register_user),

    
    


]
