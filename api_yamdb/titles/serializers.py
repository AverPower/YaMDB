from datetime import datetime

from rest_framework import serializers

from .models import Title, Genre, Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        try:
            value = self.queryset.get(name=data)
        except Exception:
            raise serializers.ValidationError("Could not find such genre")
        return value


class CategoryField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        try:
            value = self.queryset.get(name=data)
        except Exception:
            raise serializers.ValidationError("Could not find such category")
        return value


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreListingField(queryset=Genre.objects.all(), many=True, source='genres')
    category = CategoryField(queryset=Category.objects.all())
    id = serializers.IntegerField(source='pk', read_only=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre', 'category')

    def create(self, validated_data):
        genres = validated_data.pop('genres')
        title = Title.objects.create(**validated_data)
        for genre in genres:
            title.genres.add(genre)
        title.save()
        return title

    def validate_year(self, value):
        current_year = datetime.now().year
        if current_year < value:
            raise serializers.ValidationError("Year must be lower than current")
        return value
