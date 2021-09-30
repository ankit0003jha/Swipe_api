from django.db.models import indexes
from django.urls import path
from .views import HistoryListView, LikeView, LikedMeListView, WhomILikedListView, dislikeView, getPhoneNumberLogin, getPhoneNumberRegistered
from . import views 


urlpatterns = [

  path("Register/<phone>/", getPhoneNumberRegistered.as_view(), name="OTP Gen"),
  path("Login/<phone>/", getPhoneNumberLogin.as_view(), name="OTP Gen"),
  path('like/<int:id>', LikeView.as_view() , name='like'),
  path('dislike/<int:id>', dislikeView.as_view(), name='dislike'),
  path('History', HistoryListView.as_view(), name='liked_me'),
  path('liked-me', LikedMeListView.as_view(), name='liked_me'),
  path('whom-i-liked', WhomILikedListView.as_view(), name='whom_i_liked'),
]