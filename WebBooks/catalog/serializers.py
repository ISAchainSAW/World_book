from rest_framework import serializers
from .models import Author


class AuthorModel:
    def __init__(self, first_name, last_name, date_of_birth, date_of_death):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.date_of_death = date_of_death


class AuthorSerializier(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_of_birth=serializers.DateField()
    date_of_death=serializers.DateField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.date_of_birth = validated_data.get("date_of_birth", instance.date_of_birth)
        instance.date_of_death = validated_data.get("date_of_death", instance.date_of_death)
        instance.save()
        return instance
