from rest_framework import serializers

from .models import Property, PropertyDocument, PropertyPhoto


class PropertyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyPhoto
        fields = "__all__"


class PropertyDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyDocument
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    photos = PropertyPhotoSerializer(many=True, read_only=True)
    documents = PropertyDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = "__all__"
