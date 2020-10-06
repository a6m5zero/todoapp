from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    # path('login/', views.LoginView.as_view(), name = 'login')
    path('login/', auth_views.LoginView.as_view(), name = 'login' ),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout' ),
    path('register/', views.register, name='register'),
    path("edit/", views.edit, name="edit"),
    # standartnie view smeni parolya, template lezhit v korne prilozhenia 
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url = reverse_lazy('accounts:password_change_done')), name ='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name ='password_change_done'),
    # standart view sbrosa passwd po email
    path('pwd-reset/done/', auth_views.PasswordResetDoneView.as_view(), name = "password_reset_done"),
    path('pwd-reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    path('pwd-reset/complete/',auth_views.PasswordResetCompleteView.as_view(), name = "password_reset_complete"),
    path('pwd-reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),

# path('users/password_reset/done/', 
#     PasswordResetDoneView.as_view(
#     template_name='commons/password_reset_done.html'),name="password_reset_done"),

# path('users/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
#     template_name='commons/password_reset_confirm.html',
#     success_url='/users/reset/done/'),name="password_reset_confirm"),

# path('users/reset/done/',
#     PasswordResetCompleteView.as_view(template_name='commons/password_reset_complete.html'),
#     name="password_reset_complete"),
]