from django.shortcuts import render

tasks = [
    {"title": "Lesson 4", "done": True},
    {"title": "Homework 1", "done": False},
    {"title": "Quiz 1", "done": True},
    {"title": "Quiz 2", "done": False},
    {"title": "Lesson 5", "done": False},
]

def home(request):
    return render(request, "home.html", {"tasks": tasks})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")