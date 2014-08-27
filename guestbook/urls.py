from django.conf.urls import patterns, url
from guestbook import views


urlpatterns = patterns(
    'guestbook.views',
    url(r'^$', views.GuestBookList.as_view()),
    url(r'^/(?P<id>.+)$', views.GuestBookRetrieve.as_view()),
    url(r'^/(?P<id>.+)/entries$', views.GuestBookEntryList.as_view())
)
