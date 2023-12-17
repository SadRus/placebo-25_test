from rest_framework.serializers import ModelSerializer

from .models import Department


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ['title', 'parent', 'organization']

    def create(self, validated_data):
        department = Department.objects.create(**validated_data)
        return department
