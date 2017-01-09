from django.conf.urls import url
from django.conf.urls.static import static

from .views import TweetListView, TweetDetailView

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name = 'list'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name = 'detail'),
]