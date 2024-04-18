from bb_clone.celery import app
from django.core.mail import send_mail
from users.models import User
from boulders.models import Sender
import datetime

@app.task
def task_one():
    print("Task one is called and worker is running as expected")
    return "success"

@app.task
def weekly_report_task():
    subject = 'Weekly Report'
    users = User.objects.all()
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    for user in users:
        sends_this_week = user.sender_set.filter(date__range=[start_week, end_week])
        message = ''
        message += (user.username + "'s Ascents This Week\n")
        for send in sends_this_week:
            message += ("_____________\n")
            message += (send.boulder.boulder_name + "\n")
            message += (send.date.strftime('%d-%m-%Y'))
            message += ("\n")
            if (send.flash):
                message += ("FLASH\n")
        message += ("=============\n")
    
        if (user.email):
            send_mail('Weekly Report', message, 'dwafqxnqvuuqtcmgkp@cazlg.com', [user.email], fail_silently=False)
            print(message)
    
    return 0


