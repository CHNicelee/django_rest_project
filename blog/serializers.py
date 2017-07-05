from rest_framework import serializers
from blog.models import *

class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.name')
    class Meta:
        exclude = []
        model = Blog
        fields = ('id', 'title', 'body', 'owner')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = User
        field = ('id', 'username', 'name')


class UserSerializer(serializers.ModelSerializer):
    blog_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())
    class Meta:
        exclude = []
        model = User
        field = ('id', 'username', 'blog_set')