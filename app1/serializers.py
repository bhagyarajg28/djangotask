from .models import Branches
from rest_framework import serializers


class Bankserializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'
