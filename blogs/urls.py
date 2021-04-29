from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blogs import views

urlpatterns = [
    path('category/', views.category_list),
    path('blogs/', views.blog_list),
    path('blog/<int:pk>', views.blog_detail)
]

# urlpatterns = format_suffix_patterns(urlpatterns)