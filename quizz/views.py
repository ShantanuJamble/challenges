from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import QuizModel, Category, SubCategory  # Sitting
from mcqs.models import Question, MCQuestion


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

