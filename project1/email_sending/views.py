""" views functions for email sending"""
from django.shortcuts import render

# from django.core.mail import send_mail
from django.http import HttpResponse
from .models import EmailMessage


def send_email(request):
    """handles POST methods"""
    if request.method == "POST":
        subject = request.POST.get("subject")
        body = request.POST.get("body")
        recipient = request.POST.get("recipient")
        EmailMessage.objects.create(
            subject=subject, body=body, recipient=recipient
        )  # pylint member disabled

        return HttpResponse("Email sent successfully!")
    return render(request, "email_send.html")
