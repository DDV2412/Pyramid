import schedule
import time

from app.utils.send_mail import send_email


def schedule_email(mail: dict):
    schedule.every().day.at(mail.get("scheduled").strftime("%H:%M")).do(send_email, mail)

    while True:
        schedule.run_pending()
        time.sleep(1)
