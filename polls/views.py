from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *
from django.urls import reverse
from django.template import loader
# Create your views here.

def list(request):
    questions=Question.objects.all()
    context={'questions':questions}
    return render(request,'polls/list.html',context)

def detail(request,question_id):
    try: 
        question=Question.objects.get(pk=question_id)
        choices=question.choice_set.all()
        context={'question':question,'choices':choices} # even if we pass just question thats enought
        # we can access choices from the template also in for loop we can put for choice in question.choice_set.all()
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exist")
    
    return render(request,'polls/detail.html',context)
def results(request,question_id):
    #question=Question.objects.get(pk=question_id)
    question=get_object_or_404(Question,pk=question_id)
    choices=question.choice_set.all()
    context={'question':question,'choices':choices}
    return render(request,'polls/results.html',context)

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
        
    except (KeyError, Choice.DoesNotExist):
        return render(request,'polls/detail.html',{'question':question,'error_message':"You didn't select a choice"})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results_question',args=(question_id,)))

def home(request):
    return render(request,'polls/home.html')


