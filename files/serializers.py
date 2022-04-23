from rest_framework import serializers
from files.models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file', 'name', 'is_folder', 'created', 'modified', 'size']
