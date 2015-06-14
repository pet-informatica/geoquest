from django.conf.urls import patterns, include, url
from questions.views import RandomQuestion

from users.views import CustomUserViewSet

urlpatterns = patterns('questions',
    # Examples:
    # url(r'^$', 'geoquest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^random/$', RandomQuestion.as_view(), name="random"),

  )
