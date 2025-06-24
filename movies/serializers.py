from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError("A data de lançamento deve ser a partir de 1900.")
        return value
    
    def validate_resume(self, value):
        if len(value) > 2000:
            raise serializers.ValidationError("O resumo deve ter no máximo 2000 caracteres.")
        return value