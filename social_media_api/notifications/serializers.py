from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    target_content_type = serializers.ReadOnlyField(source='target_content_type.model')

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'target_content_type', 'target_object_id', 'timestamp', 'is_read']
