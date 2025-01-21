from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),  # For the homepage or default route
    path("songs/", views.songs, name="songs"),  # Route for songs
    path("photos/", views.photos, name="photos"),  # Route for photos
    path("login/", views.login_view, name="login"),  # Route for login
    path("logout/", views.logout_view, name="logout"),  # Route for logout
    path("signup/", views.signup, name="signup"),  # Route for signup
    path("concerts/", views.concerts, name="concerts"),  # Route for concerts
    path("concert-detail/<int:id>/", views.concert_detail, name="concert_detail"),  # Route for concert detail
    path("concert-attendee/", views.concert_attendee, name="concert_attendee"),  # Route for concert attendee
]

