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
        validated_data = {**self.validated_data, **kwargs}
        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
            assert self.instance is not None, (
                '`update()` did not return an object instance.'
            )
        else:
            try:
                validated_data['author'] = self.initial_data['author']
                validated_data['title'] = self.initial_data['title']
                self.instance = self.create(validated_data)
                assert self.instance is not None
            except Exception:
                raise serializers.ValidationError("There is already review from this user")
        return self.instance


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        read_only_fields = ('id', 'author', 'pub_date')

    def save(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}
        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
            assert self.instance is not None, (
                '`update()` did not return an object instance.'
            )
        else:
            try:
                validated_data['author'] = self.initial_data['author']
                validated_data['review'] = self.initial_data['review']
                self.instance = self.create(validated_data)
                assert self.instance is not None
            except Exception:
                raise serializers.ValidationError("Problem with posting new comment")
        return self.instance
