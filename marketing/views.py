from django.shortcuts import render
import time

from .tasks import send_emails

def send_campaign_emails(request):
    students = ['omar', 'ahmed', 'mohamed', 'moataz', 'john', 'mark', 'osama', 'khaled', 'essam']  
    send_emails.delay(students)
    return render(request, 'udemy.html', {})
