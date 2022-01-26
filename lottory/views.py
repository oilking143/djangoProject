# Create your views here.
from lottory.models import Lottory
from lottory.Serializers import LottorySerializer

from rest_framework import viewsets


# Create your views here.
class LottoryViewSet(viewsets.ModelViewSet):
    queryset = Lottory.objects.all()
    serializer_class = LottorySerializer