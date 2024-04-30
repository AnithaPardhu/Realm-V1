# urls.py
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from .views import player, movie_upload, movie_details
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path("", views.index, name="index"),
    path("signin/", views.signin, name="signin"),
    path("profiles/", views.profiles, name="profiles"),
    path("add_profile/", views.add_profile, name="add_profile"),
    path("profiles/<int:profile_id>/edit/", views.edit_profile, name="edit_profile"),
    path(
        "profiles/<int:profile_id>/delete/", views.delete_profile, name="delete_profile"
    ),
    path("otp-verification/", views.otp_verification, name="otp_verification"),
    path("movie_upload", movie_upload, name="movie_upload"),
    path("signup", views.signup, name="signup"),
   
    path('home/', views.home, name='home'),
    path("videos/<int:genre_id>/", views.video_list, name="video_list"),
    path("search/", views.search, name="search"),
    path("movies/", views.movies, name="movies"),
    path("search_kids/", views.search_kids, name="search_kids"),
    path("schedule", views.schedule, name="schedule"),
    path('home_kids', views.home_kids, name='home_kids'),
    path("video_list1/<int:genre_id>/", views.video_list1, name="video_list1"),
    path("unlock-pin", views.unlock_pin, name="unlock_pin"),
    path("logout/", views.logout_view, name="logout"),
    
    path("movie/<int:video_id>/", movie_details, name="movie_details"),
    path("unlock", views.unlock, name="unlock"),
    path("movie/<int:video_id>/", views.movie_details, name="movie_details"),
    path("player/<int:video_id>/", views.player, name="player"),
    path("get_notifications/", views.get_notifications, name="get_notifications"),
    path('add_to_watchlist/<int:video_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path("watchlist_display/", views.watchlist_display, name="watchlist_display"),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('update_password/', views.update_password, name='update_password'),
    path('password_updated/', views.password_updated, name='password_updated'),
    path('hover/', views.hover_view, name='hover'),
    path('hover_player/', views.hover_player_view, name='hover_player'),
    path('profiles/<int:profile_id>/', views.profile_detail, name='profile_detail'),
    path('shows',views.shows,name='shows'),
    path('select_profile/<str:profile_name>/', views.select_profile, name='select_profile'),
    # path('remove_from_watchlist/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path("dummy/<int:profile_id>/", views.dummy, name="dummy"),
    path(
        "dummy_for_edit/<int:profile_id>/", views.dummy_for_edit, name="dummy_for_edit"
    ),
    path('watchlist/remove/<int:video_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('profile/password/', views.profile_password_page, name='profile_password_page'),
    path('profile/lock/', views.profile_lock_page, name='profile_lock_page'),
    path("fullaccess",views.fullaccess,name='fullaccess'),
    
    path('help-center/', views.help_center, name='help_center'),
    path('save_form/', views.save_form_data, name='save_form_data'),
    path('save-selection/', views.save_selection, name='save_selection'),
    # path('adv', views.adv, name='adv'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('delete_tokens',views.delete_tokens,name='delete_tokens'),
    path('payment_form',views.payment_form,name='payment_form'),
    path("pre_signin/", views.pre_signin, name="pre_signin"),
#    path('pay', views.payment_view, name='payment_view'),
#     path('payment_success/', views.payment_success, name='payment_success'),
#     path('subscription',views.subscription,name='subscription'),
#    path('plan1',views.plan1,name='plan1'),
#    path('plan2',views.plan2,name='plan2'),
#    path('plan3',views.plan3,name='plan3'),
#    path('plan4',views.plan4,name='plan4'),


   path('remove-data/', views.remove_data, name='remove_data'),
   path("fullaccess1",views.fullaccess1,name='fullaccess1'),
   path('remove_saved_data/', views.remove_saved_data, name='remove_saved_data'),  



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)