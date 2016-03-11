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


def get_mcq(request, slug):
    question = MCQuestion.objects.get(id=slug)
    sitting_id = request.POST.get('sitting_id')
    marks = 0
    try:
        sitting = Sitting.objects.get(id=sitting_id)
        marks = sitting.score
    except:
        marks = 0
    options = question.get_answers()
    return render_to_response('mcqs/mcquestion_detail.html', locals(), context_instance=RequestContext(request))


def accept_answer(request, slug):
    marks = 0
    if request.method == 'POST':
        question = MCQuestion.objects.get(id=slug)
        user_answer = request.POST.get('choice')
        sitting_id = request.POST.get('sitting_id')
        sitting = Sitting.objects.get(id=sitting_id)
        marks = int(sitting.score)
        question_set = list(sitting.question_order)  # [int(x) for x in sitting.question_order.split(',')]
        answer_set = list(sitting.answers_set)
        if answer_set[question_set.index(str(question.id))] == '1':
            pass
        else:
            if question.check_if_correct(user_answer):
                marks += 1
                print 1
                answer_set[question_set.index(str(question.id))] = '1'
                sitting.answers_set = ''.join(answer_set)
                print sitting.answers_set
            else:
                marks = marks
            sitting.score = marks
            sitting.save()
    else:
        marks = marks
    jason_data = json.dumps({'marks': marks})
    return HttpResponse(jason_data, content_type="application/json")


class SittingDetailView(DetailView):
    model = Sitting
    # slug = 'id'
    context_object_name = 'quiz'
    template_name = 'quizz/quizmodel_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SittingDetailView, self).get_context_data(**kwargs)
        print context
        return context
