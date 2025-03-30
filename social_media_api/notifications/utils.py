from django.contrib.contenttypes.models import ContentType
from .models import Notification


def create_notification(recipient, actor, verb, target):
    """Create a notification for the recipient."""
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target_object_id=target.id,
        target_content_type=ContentType.objects.get_for_model(target),
    )
