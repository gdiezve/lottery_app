from rest_framework import serializers
from .models import *


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields = ("id", "name", "surname", "national_id_card", "age")


class BallotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ballot
        fields = ("number", "lottery_date", "participant")


class LotterySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lottery
        fields = ("lottery_date", "winner_ballot")
