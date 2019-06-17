from django.conf.urls import url
from . import views_generic
from . import views_apiview
urlpatterns = [
    # url(r'^books/$', views_generic.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_generic.BookView.as_view()),
    url(r'^books/$', views_apiview.BooksView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views_apiview.BookView.as_view()),
]
