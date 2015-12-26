from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
# Create your views here.
from mcqs.forms import QuestionForm
from mcqs.models import MCQuestion


class MCQDetailView(DetailView):
    model = MCQuestion
    slug_field = 'id'
    context_object_name = 'question'

    def get_context_data(self, *args, **kwargs):
        context = super(MCQDetailView, self).get_context_data(**kwargs)
        return context


class MCQListView(ListView):
    model = MCQuestion


class QuizTake(FormView):
    form_class = QuestionForm
    template_name = 'mcqs/quiz_form.html'

    def dispatch(self, request, *args, **kwargs):
        print self.kwargs['quiz']
        print self.kwargs['username']
        return super(QuizTake, self).dispatch(self.request, *args, **kwargs)