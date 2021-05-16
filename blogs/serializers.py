from rest_framework import serializers
from blogs.models import Category, Blog, Cover


class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = ['id', 'name', 'description']


class BlogSerializer(serializers.ModelSerializer):
    # cover_name = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # cover_description = serializers.ReadOnlyField(source='cover.description')
    cover = CoverSerializer()
    created = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Blog
        fields = ['id', 'name', 'active', 'content', 'created', 'cover', 'category']
        # fields = ['id', 'name', 'active', 'content', 'created', 'cover', 'cover_name', 'cover_description']

    def create(self, validate_data):
        cover_data = validate_data.pop('cover')
        cover = Cover.objects.create(**cover_data)

        blog = Blog.objects.create(
            cover=cover,
            **validate_data
        )
        return blog


class CategorySerializer(serializers.ModelSerializer):

    blogs = BlogSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'blogs']
