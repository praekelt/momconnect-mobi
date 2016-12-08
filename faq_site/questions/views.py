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
    catagory=Catagory.objects.get(catagory_title=catagory_name)
    #return HttpResponse("Displaying" + catagory.catagory_title + "!")
    catagory_questions = catagory.qanda_set.all()
    return render(request, 'questions/questions.html', {'catagory': catagory, 'catagory_questions': catagory_questions})


def answers(request, catagory_name, question_id):
    return HttpResponse("This page with display "
                        "individual question answer pairs")
