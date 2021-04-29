from rest_framework import serializers
from blogs.models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BlogSerializer(serializers.ModelSerializer):
	cover = serializers.SlugRelatedField(read_only=True, slug_field='name')
	cover_description = serializers.ReadOnlyField(source='cover.description')

	class Meta:
		model = Blog
		fields = ['id', 'name', 'active', 'content', 'created', 'cover', 'cover_description']