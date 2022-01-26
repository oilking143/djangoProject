# Create your views here.
from period.models import Period
from period.serializers import PeriodSerializer

from rest_framework import viewsets


# Create your views here.
class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer