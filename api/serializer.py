from rest_framework import serializers
from fruit.models import Fruit
from accounts.models import Profile


class FruitSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Fruit
        exclude = ['image']

