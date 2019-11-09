from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^demands/$', views.DemandsListAPI.as_view(), name='demands-list'),
    url(r'^user/$', views.UserList.as_view(), name='user-list'),
    url(r'^user_detail/$', views.UserDetailsList.as_view(), name='user-list'),
]
