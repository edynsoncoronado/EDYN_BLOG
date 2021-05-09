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
    # category = CategorySerializer()

    class Meta:
        model = Blog
        fields = ['id', 'name', 'active', 'content', 'created', 'cover', 'category']
        # fields = ['id', 'name', 'active', 'content', 'created', 'cover', 'cover_name', 'cover_description']

    def create(self, validate_data):
        category_data = validate_data.pop('category')
        category = Category.objects.filter(name__contains=category_data.get('name'))
        if not category:
            category = Category.objects.create(**category_data)
        else:
            category = category[0]

        cover_data = validate_data.pop('cover')
        cover = Cover.objects.create(**cover_data)

        blog = Blog.objects.create(
            cover=cover,
            category=category,
            **validate_data
        )
        return blog


class CategorySerializer(serializers.ModelSerializer):

    blogs = BlogSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'blogs']

    """
    def get_blog_list(self, obj):
        print("get_blog_list>>>>", obj)
        blog_list = Blog.objects.filter(category=Category.objects.get(pk=obj.id))
        print("blog", blog_list)
        return BlogSerializer(blog_list, many=True).data
    """
