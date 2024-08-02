from django.shortcuts import render
import time


def send_campaign_emails(request):
    students = ['omar', 'ahmed', 'mohamed', 'moataz', 'john', 'mark', 'osama', 'khaled', 'essam']
    for name in students:
        print(f'sending email to {name}')
        time.sleep(1)

    return render(request, 'udemy.html', {})
