import random
import sys

from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    national_id_card = models.CharField(max_length=10)
    age = models.IntegerField()

    def list_ballots(self):
        sys.stdout.write(f"List of ballots submitted by {self.__str__()}:")
        ballots = [ballot for ballot in Ballot.objects.filter(participant=self)]
        sys.stdout.write(f"{ballots}")
        return ballots

    def __str__(self):
        return f"{self.name} {self.surname}"


class Ballot(models.Model):
    number = models.IntegerField(primary_key=True)
    lottery_date = models.DateField()
    participant = models.ForeignKey(
        Participant,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"Ballot Nº:{self.number}, Lottery Date: {self.lottery_date}, Participant: {self.participant}"


class Lottery(models.Model):
    lottery_date = models.DateField(primary_key=True)
    winner_ballot = models.OneToOneField(
        Ballot,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def choose_winner_ballot(self):
        sys.stdout.write(f"Choosing winner ballot for {self.lottery_date} Lottery...\n")
        if not self.winner_ballot:
            self.winner_ballot = random.choice(list(Ballot.objects.filter(lottery_date__day=self.lottery_date.day)))
            sys.stdout.write(f"Winner is: {self.winner_ballot.__str__()}\n")
        else:
            sys.stdout.write(f"Winner was already chosen for this lottery: {self.winner_ballot.__str__()}\n")
        return self.winner_ballot

    def __str__(self):
        return f"Lottery from {self.lottery_date}"
