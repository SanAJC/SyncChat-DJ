from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='inicio'),
    path('login/',views.login,name='login'),
    path('registro/',views.register, name="registro"),
    path('logout/',views.logout_view,name='logout'),
    path('chat/', views.chat_rooms, name='chat_rooms'),
    path('chat/<str:room_name>/', views.room, name='room'),
]

