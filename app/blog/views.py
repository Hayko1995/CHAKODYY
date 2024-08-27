from django.shortcuts import render
from rest_framework.views import APIView
from blog.serializers import CreateActionSerializer, CreateRolesSerializer, CreateGroupsSerializer, CreateProjectSerializer, BlogGetSerializer
from rest_framework.response import Response
from rest_framework import status


class CreateActions(APIView):
    def post(self, request, format=None):
        serializer = CreateActionSerializer(
            data=request.data, context={'user': request.user})
        results = serializer.create(request.data)
        return Response({'msg': results}, status=status.HTTP_201_CREATED)


class CreateRoles(APIView):
    def post(self, request, format=None):
        serializer = CreateRolesSerializer(
            data=request.data, context={'user': request.user})
        results = serializer.create(request.data)
        return Response({'msg': results}, status=status.HTTP_201_CREATED)


class CreateGroups(APIView):
    def post(self, request, format=None):
        serializer = CreateGroupsSerializer(
            data=request.data, context={'user': request.user})
        results = serializer.create(request.data)
        return Response({'msg': results}, status=status.HTTP_201_CREATED)


class CreateProjects(APIView):
    def post(self, request, format=None):
        serializer = CreateProjectSerializer(
            data=request.data, context={'user': request.user})
        results = serializer.create(request.data)
        return Response({'msg': results}, status=status.HTTP_201_CREATED)


class BlogGet(APIView):
    def post(self, request, format=None):
        serializer = BlogGetSerializer(
            data=request.data, context={'user': request.user})
        results = serializer.create(request.data)
        return Response(results, status=status.HTTP_201_CREATED)
