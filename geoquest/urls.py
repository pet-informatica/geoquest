from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from questions.views import QuestionViewSet, CategoryViewSet, AnswerViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geoquest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^', include(router.urls)),
)
