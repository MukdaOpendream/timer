from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.TimerView.as_view(), name='timer'),
    url(r'^timers$', views.TimersView.as_view(), name='timers'),
    url(r'^no-bootstrap$', views.TimerNoBootstrapView.as_view(), name='timer_css')
]
