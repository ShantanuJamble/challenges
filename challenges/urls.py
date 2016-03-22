from django.conf.urls import patterns, include, url
from django.contrib import admin
import mcqs
from mcqs.views import MCQDetailView, MCQListView, SittingDetailView
import quizz
from quizz.views import QuizDetailView, QuizListView
from users import views

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'users.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       # QuizUrl
                       # url(r'^quiz/(?P<slug>[-_\w]+)/$', QuizDetailView.as_view(), name='quiz_detials'),
                       url(r'^quiz/$', QuizListView.as_view(), name='quiz_list'),
                       # MCQURLS
                       url(r'^mcqs/(?P<slug>\d)/$', mcqs.views.get_mcq, name='mcq_detail'),
                       url(r'^checkans/(?P<slug>\d)/$', mcqs.views.accept_answer, name='check_answer'),
                       url(r'^mcqs/$', MCQListView.as_view(), name='mcq_list'),

                       # QuizTake
                       #url(r'^quiz/(?P<quiz>[-_\w]+)/(?P<username>[-_\w]+)/$', mcqs.views.quiz_take, name='quiz_take'),
                       url(r'^quiz/(?P<quiz>[-_\w]+)/$', quizz.views.quiz_take, name='quiz_take'),
                       url(r'^register/(?P<quiz_id>\d)/$', quizz.views.register),
                       url(r'^start/(?P<quiz_id>\d)/$', quizz.views.start_quiz),

                       # sitting view
                       url(r'^sitting/(?P<id>\d)/$', SittingDetailView.as_view(), name='sitting_details'),

                       #login cha links
                       url(r'^login/', 'users.views.login_handler'),
                       url(r'^logout/', 'users.views.logoutrequest'),


)
