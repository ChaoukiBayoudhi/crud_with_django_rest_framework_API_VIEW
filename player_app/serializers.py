from player_app.models import Player
from rest_framework import serializers

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id',
                  'name',
                  'email',
                  'tshirtNumber',
                  'birthDate',
                  'country')