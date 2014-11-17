from django.conf.urls import patterns, include, url
from django.contrib import admin

from ajaxsite.views import CommentView, CommentCreateView, HomeView, ObservationView, ObservationCreateView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    
    url(r'^observation/(?P<pk>\d+)/$', ObservationView.as_view(), name='view_comment'),
    url(r'^observation/add/$', ObservationCreateView.as_view(), name='create_observation'),

    url(r'^comment/(?P<pk>\d+)/$', CommentView.as_view(), name='view_comment'),    
    url(r'^comment/add/$', CommentCreateView.as_view(), name='create_comment'),

    url(r'^admin/', include(admin.site.urls)),
)
