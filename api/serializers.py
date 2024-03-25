from rest_framework import serializers
from api.models import Company


class CompanySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        company_id = serializers.ReadOnlyField()
        model = Company
        fields = "__all__"
        