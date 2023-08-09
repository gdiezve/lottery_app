from django.test import TestCase
from django.utils import timezone
from .models import Participant, Ballot, Lottery
from .cron import close_active_lottery_and_create_new
import datetime


class ParticipantTestCase(TestCase):
    def test_list_ballots(self):
        participant = Participant.objects.create(name="John", surname="Doe", national_id_card="1234567890", age=30)
        lottery_date = timezone.now().date()
        ballot1 = Ballot.objects.create(number=1, lottery_date=lottery_date, participant=participant)
        ballot2 = Ballot.objects.create(number=2, lottery_date=lottery_date, participant=participant)

        ballots = participant.list_ballots()
        self.assertIn(ballot1, ballots)
        self.assertIn(ballot2, ballots)


class LotteryTestCase(TestCase):
    def test_choose_winner_ballot(self):
        lottery_date = timezone.now().date() + datetime.timedelta(days=1)
        lottery = Lottery.objects.create(lottery_date=lottery_date)
        participant = Participant.objects.create(name="Jane", surname="Smith", national_id_card="9876543210", age=25)
        ballot = Ballot.objects.create(number=1, lottery_date=lottery_date, participant=participant)

        # Ensure that choosing the winner ballot works correctly
        chosen_ballot = lottery.choose_winner_ballot()
        self.assertEqual(chosen_ballot, ballot)

        # Ensure that choosing the winner ballot again returns the same result
        chosen_ballot_again = lottery.choose_winner_ballot()
        self.assertEqual(chosen_ballot_again, chosen_ballot)

    def test_choose_winner_ballot_already_chosen(self):
        lottery_date = timezone.now().date() + datetime.timedelta(days=2)
        lottery = Lottery.objects.create(lottery_date=lottery_date)
        participant = Participant.objects.create(name="Alice", surname="Johnson", national_id_card="4567891230", age=40)
        ballot = Ballot.objects.create(number=1, lottery_date=lottery_date, participant=participant)
        lottery.winner_ballot = ballot
        lottery.save()

        # Ensure that choosing the winner ballot for a lottery that already has a winner returns the same winner
        chosen_ballot = lottery.choose_winner_ballot()
        self.assertEqual(chosen_ballot, ballot)


class BallotTestCase(TestCase):
    def test_ballot_str(self):
        participant = Participant.objects.create(name="Mary", surname="Brown", national_id_card="1357902468", age=35)
        lottery_date = timezone.now().date()
        ballot = Ballot.objects.create(number=1, lottery_date=lottery_date, participant=participant)

        expected_str = f"Ballot Nº:{ballot.number}, Lottery Date: {lottery_date}, Participant: {participant}"
        self.assertEqual(str(ballot), expected_str)


class CloseAndCreateLotteryTestCase(TestCase):
    def setUp(self):
        # Create an active lottery for yesterday
        self.yesterday = timezone.now().date() - datetime.timedelta(days=1)
        self.active_lottery = Lottery.objects.create(lottery_date=self.yesterday)
        self.participant = Participant.objects.create(name="John", surname="Doe", national_id_card="1234567890", age=30)
        self.ballot = Ballot.objects.create(number=1, lottery_date=self.yesterday, participant=self.participant)
        self.active_lottery.save()

    def test_close_active_lottery_and_create_new(self):
        # Close active lottery by choosing a winner ballot and creates a new one
        new_lottery = close_active_lottery_and_create_new()
        closed_lottery = Lottery.objects.filter(lottery_date=self.yesterday)

        self.assertEqual(self.active_lottery, closed_lottery[0])
        self.assertIsNotNone(closed_lottery[0].winner_ballot)
        self.assertEqual(new_lottery[0].lottery_date, timezone.now().date())
        self.assertIsNone(new_lottery[0].winner_ballot)
        self.assertNotEqual(new_lottery[0], self.active_lottery)

    def test_close_no_active_lottery_and_create_new(self):
        # Attempt to close the active lottery when there is none and creates a new one
        self.active_lottery.delete()
        new_lottery = close_active_lottery_and_create_new()

        self.assertEqual(new_lottery[0].lottery_date, timezone.now().date())

    def test_create_new_lottery_already_exists(self):
        # Attempt to create a new lottery when one already exists for today
        Lottery(lottery_date=timezone.now().date()).save()
        new_lottery = close_active_lottery_and_create_new()

        self.assertIsNone(new_lottery)
