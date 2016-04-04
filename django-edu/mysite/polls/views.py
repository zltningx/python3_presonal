
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import Question, Choice

# def index(request):
#     return HttpResponse(u"弢哥决定用django 快速开发小黄网")

# def detail(request, question_id):
#     return HttpResponse(u"你正在查看的问题是 {}".format(question_id))
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # return HttpResponse(u"你投票给了问题 {}".format(question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render (request, 'polls/detail.html', {
            'question': question,
            'error_message': "你一个不选什么意思？",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(render(request, 'polls/index.html', context))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("麻痹往哪里翻呢你！ ")
    return render(request, 'polls/detail.html', {'question': question})

def results(requeset, question_id):
    # response = u"你正在查看问题的结果 {}."
    # return HttpResponse(response.format(question_id))
    question = get_object_or_404(Question,pk=question_id)
    return render(requeset, 'polls/results.html', {'question': question})
'''