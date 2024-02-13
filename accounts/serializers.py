from django.contrib.auth.models import Permission,Group
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
    


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(read_only=True)
    class Meta:
        model = Group
        fields = '__all'
     
