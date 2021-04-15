from django.db import models
from django.contrib.auth import get_user_model
import uuid

CustomUser = get_user_model()

# Create your models here.


class CommonInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="%(app_label)s_%(class)s_creator")
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    modified_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="%(app_label)s_%(class)s_modifier")

    comment = models.TextField(blank=True)

    class Meta:
        abstract = True

