from rest_framework import permissions

permission_classes = (permissions.IsAuthenticatedOrReadOnly,)