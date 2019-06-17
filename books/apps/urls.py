from django.conf.urls import url

from apps.views_genericviewset import BookInfoViewSet
from . import views_generic
from . import views_apiview
from . import views_mixin
from . import views_generic_minxin
from . import views_viewset

urlpatterns = [
    url(r'^books/$', BookInfoViewSet.as_view({'get': 'list'})),
    url(r'^books/latest/$', BookInfoViewSet.as_view({'get': 'latest'})),
    url(r'^books/(?P<pk>\d+)/$', BookInfoViewSet.as_view({'get': 'retrieve'})),
    url(r'^books/(?P<pk>\d+)/read/$', BookInfoViewSet.as_view({'put': 'read'})),
    # url(r'^books/$', views_viewset.BooksView.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^books/(?P<pk>\d+)/$',
    #     views_viewset.BookView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destory'})),
    # url(r'^books/$', views_generic_minxin.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_generic_minxin.BookView.as_view()),
    # url(r'^books/$', views_mixin.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_mixin.BookView.as_view()),
    # url(r'^books/$', views_generic.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_generic.BookView.as_view()),
    # url(r'^books/$', views_apiview.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views_apiview.BookView.as_view()),
]
