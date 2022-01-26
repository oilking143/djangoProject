import random

from mnemonic import Mnemonic
from rest_framework import serializers
from lottory.models import Lottory
import requests
import json
import re
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

        if value != '0,0,0,0,0':
            return value
        else:

            return origin




class Tobip39(serializers.CharField):
    def to_representation(self, value):
        bip39 = Mnemonic("english")
        bip39words = bip39.generate(strength=256)
        bip39seed = bip39.to_seed(bip39words, passphrase="")
        return bip39words

class ToSha256(serializers.CharField):
    def to_representation(self, value):
        bip39 = Mnemonic("english")
        bip39words = bip39.generate(strength=256)
        bip39seed = bip39.to_seed(bip39words, passphrase="")
        shabip39 = hashlib.sha256(bip39.to_hd_master_key(bip39seed, False).encode("utf8")).hexdigest()
        response = requests.post(
            'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=FX1VWGWUFSXRHEMVM14X6N27CA47V14IV5',
            json={})
        j = json.loads(response.text)
        ethusd=j['result']['ethusd']
        ethusd_timestamp = j['result']['ethusd_timestamp']
        origin = j['result']['ethusd']
        origin += j['result']['ethusd_timestamp']

        nopoint = str(origin).replace(",","")
        hashstr = hashlib.sha512(nopoint.encode("utf8")).hexdigest()
        numstr = re.sub('[a-zA-Z]','',hashstr)
        result = "".join(dict.fromkeys(numstr))
        jstr = '{"list": '+result+', "hashstr": '+hashstr+', "ethusd": '+ethusd+', "ethusd_timestamp": '+ethusd_timestamp+'}'
        return jstr

class LottorySerializer(serializers.ModelSerializer):

    number = ToUpperCaseCharField()
    bip39 = Tobip39()
    sha256 = ToSha256()


    class Meta:
        model = Lottory
        # fields = 'all'
        fields = ( 'period', 'number', 'bip39', 'sha256')