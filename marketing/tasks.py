from celery import shared_task
import time

@shared_task
def send_emails():
    for name in range(10):
        print(f'sending email to {name}')
        time.sleep(1)
    # for name in students:
    #     print(f'sending email to {name}')
    #     time.sleep(1)