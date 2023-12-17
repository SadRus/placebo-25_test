from rest_framework.serializers import ModelSerializer

from .models import Department, Role


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ['title', 'parent', 'organization']

    def create(self, validated_data):
        department = Department.objects.create(**validated_data)
        return department


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ['name', 'department']

    def create(self, validated_data):
        role = Role.objects.create(**validated_data)
        return role
