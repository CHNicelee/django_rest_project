from rest_framework import serializers
from blog.models import *

class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.name')
    class Meta:
        model = Blog
        fields = ('id', 'title', 'body', 'owner')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name')

#custom relational field
class BlogListField(serializers.RelatedField):

    def to_representation(self, value):
        return 'blog_id:%d,blog_title:%s' % (value.id, value.title)

class UserSerializer(serializers.ModelSerializer):
    # blog_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Blog.objects.all())
    # blog_set = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='blog-detail')
    # blog_set = serializers.StringRelatedField(many=True)
    # blog_set = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # blog_listing = serializers.HyperlinkedIdentityField(view_name='blog-detail')
    blog_set = BlogListField(many=True,read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'blog_set')