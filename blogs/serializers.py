from rest_framework import serializers
from blogs.models import Category, Blog, Cover


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CoverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cover
		fields = ['id', 'name', 'description']


class BlogSerializer(serializers.ModelSerializer):
	# cover_name = serializers.SlugRelatedField(read_only=True, slug_field='name')
	# cover_description = serializers.ReadOnlyField(source='cover.description')
	cover = CoverSerializer()

	class Meta:
		model = Blog
		fields = ['id', 'name', 'active', 'content', 'created', 'cover']
		# fields = ['id', 'name', 'active', 'content', 'created', 'cover', 'cover_name', 'cover_description']

	def create(self, validate_data):
		cover_data = validate_data.pop('cover')
		cover = Cover.objects.create(**cover_data)
		blog = Blog.objects.create(
			cover=cover,
			**validate_data
		)
		return blog