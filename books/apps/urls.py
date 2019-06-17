from django.conf.urls import url
from . import views_generic
urlpatterns = [
    url(r'^books/$', views_generic.BooksView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views_generic.BookView.as_view()),
]
