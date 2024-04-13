from django.db import models
from module.account.models import User

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    user = models.ManyToOneRel(User, blank=True, null=True, on_delete = models.SET_NULL)