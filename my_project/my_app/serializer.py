from rest_framework.serializers import ModelSerializer
from .models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeSerializer
        fields = ["id", "name"]
#facebook
