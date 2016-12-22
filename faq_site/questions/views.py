from django.shortcuts import render
from .models import Catagory, QandA


# Create your views here.
def home(request):
    return render(request, 'questions/home.html', {})


def index(request):
    all_catagories = Catagory.objects.all()
    return render(request, 'questions/index.html',
                  {'all_catagories': all_catagories})


def questions(request, catagory_name):
    catagory = Catagory.objects.get(catagory_title=catagory_name)
    catagory_questions = catagory.qanda_set.all()
    return render(request, 'questions/questions.html',
                  {'catagory': catagory,
                   'catagory_questions': catagory_questions})


def answers(request, catagory_name, question_id):
    catagory = Catagory.objects.get(catagory_title=catagory_name)
    question = QandA.objects.get(id=question_id)
    return render(request, 'questions/answers.html',
                  {'catagory': catagory, 'question': question})
