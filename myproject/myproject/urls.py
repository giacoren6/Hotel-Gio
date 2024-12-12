from django.contrib import admin
from django.urls import path, re_path
from myapp import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
    path('book/', views.book, name='book'),
    path('booking_success/', views.booking, name='booking_success'),
    path('view/', views.view_bookings, name='view_bookings'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('book_done/', views.book_done, name='book_done'),
    path('login_done/', views.login_done, name='login_done'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

#path('admin/', admin.site.urls),