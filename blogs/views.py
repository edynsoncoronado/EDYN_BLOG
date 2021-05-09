from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogs.models import Category, Blog, Cover
from blogs.serializers import CategorySerializer, BlogSerializer, CoverSerializer

@api_view(['GET', 'POST'])
def category_list(request, format=None):
    if request.method == 'GET':
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializers = BlogSerializer(blogs, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = BlogSerializer(data={
            'name': request.data['name'],
            'content': request.data['content'],
            'cover': {
                'name': request.data['cover_name'],
                'description': request.data['cover_description']
            },
            'category': {
                'name': request.data['category_name']
            }
        })
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def category_detail(request, pk):
    print("GETTTTT", pk)
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = CategorySerializer(category)
        return Response(serializers.data)


# @api_view(['GET', 'PUT', 'DELETE'])
@api_view(['GET'])
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    """
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    """