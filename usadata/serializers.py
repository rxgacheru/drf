from rest_framework import serializers
from usadata.models import State, Person

class StateSerializer(serializers.ModelSerializer):
  class Meta:
    model = State
    fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = '__all__'



