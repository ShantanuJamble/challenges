from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import QuizModel, Category, SubCategory  # Sitting
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


def quiz_take(request, quiz):
    print quiz
    if request.user.is_authenticated():
        new_sitting = None
        new_sitting = Sitting.objects.user_sitting(request.user, quiz)
        if new_sitting == False:
            allowed = False
            message = 'U have completed the test already!'
        else:
            allowed=True
            questions = str(new_sitting.question_order)
            questions = questions.split(',')
            question_set = []
            index = 0
            question_count = len(questions)
            while index < question_count - 1:
                question_set.append(int(questions[index]))
                index += 1
    else:
        allowed = False
        message = 'Dude you aren\'t logged in'

    return render_to_response('mcqs/quiz_form.html', locals(), context_instance=RequestContext(request))