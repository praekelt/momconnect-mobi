from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^questions/$', views.index, name='index'),
    url(r'^questions/(?P<catagory_name>[a-zA-Z]+)/$', views.questions, name='questions'),
    url(r'^questions/(?P<catagory_name>[a-zA-Z]+)/(?P<question_id>[0-9]+)/$',
        views.answers, name='answers'),
]
