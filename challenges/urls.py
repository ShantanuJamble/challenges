from django.conf.urls import patterns, include, url
from django.contrib import admin
from mcqs.views import MCQDetailView, MCQListView, QuizTake
from quizz.views import QuizDetailView, QuizListView

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'challenges.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       # QuizUrl
                       url(r'^quiz/(?P<slug>[-_\w]+)/$', QuizDetailView.as_view(), name='quiz_detials'),
                       url(r'^quiz/$', QuizListView.as_view(), name='quiz_list'),
                       # MCQURLS
                       url(r'^mcqs/(?P<slug>\d)/$', MCQDetailView.as_view(), name='mcq_detail'),
                       url(r'^mcqs/$', MCQListView.as_view(), name='mcq_list'),

                       #QuizTake
                       url(r'^quiz/(?P<quiz>[-_\w]+)/(?P<username>[-_\w]+)/$', QuizTake.as_view(), name='quiz_take')
)
