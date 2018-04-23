from rest_framework import status, response, views, generics
from api.serializers.kelas import CategorySerializer, OpenClassSerializer, NewOpenClassSerializer
from kelas.models import Category, OpenClass
from accounts.models import User
from profiles.models import Profile
from django.db.models import Q


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class OpenClassView(generics.ListCreateAPIView):
    serializer_class = NewOpenClassSerializer
    queryset = OpenClass.objects.all()

    def get_queryset(self):
        queryset = super(OpenClassView, self).get_queryset()

        special = self.request.query_params.get('special', None)
        username = self.request.query_params.get('user', None)

        if special == 'home':
            followings = Profile.objects.filter(user__followers=self.request.user)
            queryset = queryset.filter(Q(partner=self.request.user.profile) | Q(partner__in=followings))

        if username:
            queryset = queryset.filter(partner__user__username=username)

        return queryset


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        open_class = self.perform_create(serializer)

        new_serializer = OpenClassSerializer(serializer.instance)
        headers = self.get_success_headers(new_serializer.data)
        return response.Response(new_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = OpenClassSerializer(page, context={'request': request}, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = OpenClassSerializer(queryset, context={'request': request}, many=True)
        return response.Response(serializer.data)
