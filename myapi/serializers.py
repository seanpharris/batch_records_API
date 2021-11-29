from rest_framework import serializers
from .models import BatchJob


class BatchJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchJob # this is the model that is being serialized
        fields = ('batch_number', 'submitted_at', 'nodes_used')