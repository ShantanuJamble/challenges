from datetime import datetime, timedelta
import time
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import QuizModel
from mcqs.models import Question, MCQuestion, Sitting


class QuizDetailView(DetailView):
    model = QuizModel
    slug_field = 'url'
    context_object_name = 'quiz'

    def get_context_data(self, **kwargs):
        context = super(QuizDetailView, self).get_context_data(**kwargs)
        questions = MCQuestion.objects.all().filter(quiz=self.object.id).order_by('?')
        context['questions'] = questions
        context['url'] = self.object.get_absolute_url()
        return context


class QuizListView(ListView):
    model = QuizModel
    context_object_name = 'quiz_list'


def start_quiz(request, quiz_id):
    new_sitting = None
    quiz = QuizModel.objects.get(id=quiz_id)
    new_sitting = Sitting.objects.user_sitting(request.user, quiz)
    if not new_sitting:
        allowed = False
        message = 'U have completed the test already!'
    else:
        allowed = True
        questions = str(new_sitting.question_order)
        questions = questions.split(',')
        try:
            new_sitting.start_time = datetime.now()
            new_sitting.end_time = datetime.now() + timedelta(minutes=int(quiz.duration))
            milliseconds = time.mktime(new_sitting.end_time.timetuple()) * 1000
            new_sitting.save()
        except:
            print "Session Object creation failed"
            allowed = False
        question_set = []
        index = 0
        question_count = len(questions)
        while index < question_count:
            question_set.append(int(questions[index]))
            index += 1
    return render_to_response('mcqs/quiz_form.html', locals(), context_instance=RequestContext(request))


def quiz_take(request, quiz):
    if request.user.is_authenticated():
        quiz = QuizModel.objects.get(url=quiz)
        try:
            user = quiz.participants.get(username=request.user.username)
        except Exception:
            user = None
        now = timezone.now()
        start = quiz.start_time
        end = quiz.end_time
        count = quiz.participants.count()
        if user is None and start <= now < end:
            message = "Register"
        else:
            if now > start:
                message = "Started"
            if now > end:
                message = "Ended"
            if now < start:
                message = "Participated"
                # start_quiz(quiz, request)
    else:
        allowed = False
        message = 'Dude you aren\'t logged in'

    return render_to_response('mcqs/quiz_form.html', locals(), context_instance=RequestContext(request))


# Register method for quiz
def register(request, quiz_id):
    print 'i am in'
    if request.user.is_authenticated():
        try:
            quiz = QuizModel.objects.get(id=quiz_id)
            quiz.participants.add(request.user)
            quiz.save()
            return HttpResponseRedirect(quiz.get_absolute_url())
        except QuizModel.DoesNotExist:
            print 'Quiz Object not found'
    else:
        pass