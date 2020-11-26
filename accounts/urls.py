from django.urls import path
from django.contrib.auth import views as auth_views
from .import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('teacher_register/',views.teacher_register.as_view(), name='teacher_register'),
     path('student_register/',views.student_register.as_view(), name='student_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),


     path('reset_password/',auth_views.PasswordResetView.as_view(template_name="../templates/password_reset_form.html"), name="reset_password"),

     path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="../templates/password_reset_sent.html"), name="password_reset_done"),
     
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="../templates/password_reset.html"), name="password_reset_confirm"),

     path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="../templates/password_reset_complete.html"), name="password_reset_complete")
     
]