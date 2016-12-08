from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Catagory, QandA


# Create your views here.
def home(request):
    return HttpResponse("This is the home page")


def index(request):
    all_catagories = Catagory.objects.all()
    return render(request, 'questions/index.html', {'all_catagories': all_catagories})


def questions(request, catagory_name):
    # catagory_questions =
    return render(request, 'questions/questions.html', {'catagory_name': catagory_name})


def answers(request, catagory_name, question_id):
    return HttpResponse("This page with display "
                        "individual question answer pairs")
