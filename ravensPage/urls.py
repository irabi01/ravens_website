from django.conf.urls import url
from . import views as page

urlpatterns = [
    url(r'^$', page.home, name="home"),
    url(r'^home/', page.home, name="home"),
    url(r'^about/', page.about, name="about"),
    url(r'^contact/', page.contact, name="contact"),
    url(r'^events/', page.events, name="events"),
    url(r'^details/(?P<id>\d+)/$', page.details, name="details"),
    # url(r'^service/', page.service, name="service"),
    url(r'^research/', page.research, name="research"),
    url(r'^ict/', page.ict, name="ict"),
    url(r'^publication/', page.publication, name="publication"),
]
