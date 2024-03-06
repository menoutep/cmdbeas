from django_cron import CronJobBase, Schedule
from django.utils import timezone
from accounts.models import User

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 2  # every 2 minutes for testing purposes; adjust as needed
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'accounts.MyCronJob'  # a unique code

    def do(self):

        users = User.objects.filter(is_staff=False)
        threshold_date = timezone.now() - timezone.timedelta(days=90)

        for user in users:
            if user.last_login and user.last_login.date() < threshold_date.date():
                user.is_active = False
                print("Deactivated user:", user.username)
                user.save()
                

        threshold_date = timezone.now() - timezone.timedelta(days=30)
        users = User.objects.filter(is_staff=True)
        for user in users:
            if user.last_login and user.last_login.date() < threshold_date.date():
                user.is_active = False
                print("Deactivated user:", user.username)
                user.save()
