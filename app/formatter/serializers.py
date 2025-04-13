from formatter.models import Query
from rest_framework import serializers

class QuerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Query
        fields = ['id', 'raw_Query', 'formatted_Query', 'user', 'created_at']
        extra_kwargs = {'formatted_Query': {'read_only': True},'user': {'read_only': True},'id': {'read_only': True},'created_at': {'read_only': True}}