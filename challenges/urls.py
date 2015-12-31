from django.conf.urls import patterns, include, url
from django.contrib import admin
import mcqs
from mcqs.views import MCQDetailView, MCQListView, SittingDetailView
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
                       url(r'^mcqs/(?P<slug>\d)/$', mcqs.views.get_mcq, name='mcq_detail'),
                       url(r'^mcqs/$', MCQListView.as_view(), name='mcq_list'),

                       # QuizTake
                       url(r'^quiz/(?P<quiz>[-_\w]+)/(?P<username>[-_\w]+)/$', mcqs.views.quiz_take, name='quiz_take'),

                       #sitting view
                       url(r'^sitting/(?P<id>\d)/$', SittingDetailView.as_view(), name='sitting_details'),
)
