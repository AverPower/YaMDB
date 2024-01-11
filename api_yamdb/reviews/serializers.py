from rest_framework import serializers

from .models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        read_only_fields = ('id', 'author', 'pub_date')

    def save(self, **kwargs):
        user = self.context['request'].user
        validated_data = self.validated_data
        validated_data['author'] = user
        validated_data['title'] = self.initial_data['title']
        try:
            self.instance = self.create(validated_data)
            return self.instance
        except Exception:
            raise serializers.ValidationError("There is already review from this user")


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('text')
