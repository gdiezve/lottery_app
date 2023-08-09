from rest_framework import viewsets
from .serializers import *
from .models import *


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all().order_by('id')
    serializer_class = ParticipantSerializer


class BallotViewSet(viewsets.ModelViewSet):
    queryset = Ballot.objects.all().order_by('number', 'lottery_date')
    serializer_class = BallotSerializer


class LotteryViewSet(viewsets.ModelViewSet):
    queryset = Lottery.objects.all().order_by('lottery_date')
    serializer_class = LotterySerializer
