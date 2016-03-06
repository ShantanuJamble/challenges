import json
from wsgiref.validate import check_content_type
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
# Create your views here.
from mcqs.forms import QuestionForm
from mcqs.models import MCQuestion, Sitting


class MCQDetailView(DetailView):
    model = MCQuestion
    slug_field = 'id'
    context_object_name = 'question'

    def get_context_data(self, *args, **kwargs):
        context = super(MCQDetailView, self).get_context_data(**kwargs)
        print 'i m here'
        return context


class MCQListView(ListView):
    model = MCQuestion


'''def get_mcq(request, slug):
    question = MCQuestion.objects.get(id=slug)
    form = QuestionForm(question)
    answers = request.POST.getlist('answers')
    if request.POST.get('quiz') is not None:
        quiz = int(request.POST.get('quiz'))
    else:
        quiz = 1
    print quiz
    sitting = None
    try:
        sitting = Sitting.objects.all().filter(user=request.user, quiz_id=quiz)
        sitting = sitting.first()
        marks = sitting.score
    except:
        sitting = Sitting.objects.create(user=request.user, quiz_id=quiz)
        sitting.save()
        marks = 0
    print sitting
    print answers
    print marks
    data = ''
    if len(answers) == 1:
        print request.is_ajax()
        correct_ans = MCQuestion.check_if_correct(answers[0])
        print answers[0]
        if correct_ans:
            if marks is None:
                marks = 1
            else:
                marks += 1
            if sitting is not None:
                sitting.score = marks
                sitting.save()
        jason_data = json.dumps({'marks': marks})
        print jason_data
        return HttpResponse(jason_data, content_type="application/json")
    else:
        if marks is None:
            marks = 0
        else:
            marks = marks
    return render_to_response('mcqs/mcquestion_detail.html', locals(), context_instance=RequestContext(request))
'''


def get_mcq(request, slug):
    question = MCQuestion.objects.get(id=slug)
    options = question.get_answers()
    return render_to_response('mcqs/mcquestion_detail.html', locals(), context_instance=RequestContext(request))


def accept_answer(request, slug):
    marks = 0
    if request.method == 'POST':
        question = MCQuestion.objects.get(id=slug)
        user_answer = request.POST.get('choice')
        if question.check_if_correct(user_answer):
            marks += 1
        else:
            marks = 0
    else:
        marks = 0
    jason_data = json.dumps({'marks': marks})
    return HttpResponse(jason_data, content_type="application/json")


def quiz_take(request, quiz, username):
    print username
    print quiz
    if request.user.is_authenticated():
        new_sitting = Sitting.objects.new_sitting(quiz, request.user)
        questions = str(new_sitting.question_order)
        questions = questions.split(',')
        question_set = []
        index = 0
        question_count = len(questions)
        while index < question_count - 1:
            question_set.append(int(questions[index]))
            index += 1
    else:
        print 'Dude you aren\'t logged in'
    return render_to_response('mcqs/quiz_form.html', locals(), context_instance=RequestContext(request))


class SittingDetailView(DetailView):
    model = Sitting
    # slug = 'id'
    context_object_name = 'quiz'
    template_name = 'quizz/quizmodel_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SittingDetailView, self).get_context_data(**kwargs)
        print context
        return context
