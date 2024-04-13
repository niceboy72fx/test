from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.db.models.base import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            return ValueError(_("please enter a valid email address"))
        
    def create_user(self, email, first_name, last_name, password, **extra_field):
        if email:
            self.email_validator(email)
        else:
            raise ValidationError(_("please enter a valid email address"))
        if not first_name and last_name:
            raise ValidationError(_("please fill the first name and last name"))
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user
            