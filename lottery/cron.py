import sys
from datetime import timedelta
from django.utils import timezone

from .models import Lottery


def close_active_lottery_and_create_new():
    sys.stdout.write("Executing scheduled cronjob to choose a winner ballot from yesterday's lottery...\n")
    yesterday = timezone.now().date() - timedelta(days=1)

    active_lottery = Lottery.objects.filter(lottery_date=yesterday)
    if active_lottery.count() <= 0:
        sys.stdout.write("There's no active lottery to close, no winner will be chosen.\n")
    else:
        active_lottery.update(winner_ballot=active_lottery[0].choose_winner_ballot())
        sys.stdout.write(f"Lottery for {active_lottery[0].lottery_date} successfully closed. \n")

    return _create_new_lottery()


def _create_new_lottery():
    sys.stdout.write("Creating today's new lottery...\n")
    new_lottery = Lottery.objects.filter(lottery_date=timezone.now().date())
    if new_lottery.count() > 0:
        sys.stdout.write(f"Lottery for {new_lottery[0].lottery_date} already created.\n")
        return None

    new_lottery.create(lottery_date=timezone.now().date())
    sys.stdout.write(f"New lottery created: {new_lottery[0].lottery_date}.\n")
    return new_lottery
