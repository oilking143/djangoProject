import random

from mnemonic import Mnemonic
from rest_framework import serializers
from period.models import Period
import hashlib


class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        origin = str(random.randint(0, 9))
        origin += ','
        origin += str(random.randint(0, 9))
        origin += ','
        origin += str(random.randint(0, 9))
        origin += ','
        origin += str(random.randint(0, 9))
        origin += ','
        origin += str(random.randint(0, 9))
        bip39 = Mnemonic("english")
        bip39words = bip39.generate(strength=256)
        bip39seed = bip39.to_seed(bip39words, passphrase="")
        origin += bip39.to_hd_master_key(bip39seed, False)
        shabip39 = hashlib.sha256(bip39.to_hd_master_key(bip39seed, False).encode("utf8")).hexdigest()
        return origin


class PeriodSerializer(serializers.ModelSerializer):
    number = ToUpperCaseCharField()

    class Meta:
        model = Period
        # fields = '__all__'
        fields = ('id', 'period', 'number', 'created')
