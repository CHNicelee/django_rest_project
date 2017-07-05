# coding=utf-8
from rest_framework import permissions


# 用于修改 删除博客
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, blog):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return blog.owner.id == request.session.get('user_id')


# 用于提交博客
class IsLoginOrReadOnly(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.session.get('user_id') is not None