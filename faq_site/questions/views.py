from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("This page will list question catagories")


def questions(request, catagory_name):
    return HttpResponse("This page will list questions"
                        " relating to a particular catagory")


def answers(request, catagory_name, question_id):
    return HttpResponse("This page with display "
                        "individual question answer pairs")
