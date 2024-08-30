"""Polls views.py"""
# from django.template import loader
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
# from django.urls import reverse

from .models import Question

# Get questions and display them


def index(request):
    """ functions for index"""
    latest_question_list = Question.objects.order_by("-pub_date")[:5]# pylint: disable=no-member
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


# Show specific question and choices


def detail(request, question_id):
    """functions for detail"""
    question = get_object_or_404(Question, pk=question_id)  # pylint: disable=no-member
    return render(request, "polls/details.html", {"question": question})

# Get question and display results


def results(request, question_id):
    """functions for results"""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html", {"question": question})


# Vote for a question choice


def vote(request, question_id):
    """functions for vote"""
    question = get_object_or_404(Question, pk=question_id)

    choice_id = request.POST.get("choice")
    if choice_id is None:
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )

    # No need for 'else' here, just continue execution
    # If the if condition is met, the function will return

    # The code below is de-indented as it's not inside an 'else' block anymore
    return render(
        request,
        "polls/details.html",
        {
            "question": question,
            "error_message": "Invalid choice selected.",
        },
    )
