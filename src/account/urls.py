from django.urls import path
from . import views
app_name ='account'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('forgotpass/',views.forgotpass,name='forgotpass'),
    path('forgot_password_validate/<uidb64>/<token>', views.forgot_password_validate, name='forgot_password_validate'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),

]