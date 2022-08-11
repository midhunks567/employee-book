from django.urls import path

from . import views


urlpatterns=[
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('add', views.add, name='add'),
    path('detail',views.emp_view,name='detail'),
    path('delete/<int:empid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
]