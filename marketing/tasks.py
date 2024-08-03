from celery import shared_task
import time

@shared_task
def send_emails(students):
    for name in students:
        print(f'sending email to {name}')
        time.sleep(1)