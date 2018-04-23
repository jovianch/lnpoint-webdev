from rest_framework import serializers
from api.serializers.accounts import UserSerializer
from api.serializers.custom import StringListField
from kelas.models import OpenClass, Tag, Category

class TagSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        return obj.name

    class Meta:
        model = Tag
        fields = ('name', )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')

class OpenClassSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = OpenClass
        fields = ('id', 'user', 'name', 'description', 'category', 'tags', 'location_latitude', \
                  'location_longitude', 'location_name', 'location_description', \
                  'is_active', 'fee', 'maximum_guest')


class NewOpenClassSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=128)
    tags = StringListField()

    def validate(self, attrs):
        request = self.context.get('request')

        attrs['user'] = request.user
        return attrs

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        category = validated_data.pop('category')

        open_class = OpenClass.objects.create(**validated_data)

        for tag_name in tags:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            open_class.tags.add(tag)

        open_class.category = category
        open_class.save()

        return open_class

    class Meta:
        model = OpenClass
        fields = ('name', 'description', 'category', 'tags', 'location_latitude', \
                  'location_longitude', 'location_name', 'location_description', \
                  'is_active', 'fee', 'maximum_guest')
