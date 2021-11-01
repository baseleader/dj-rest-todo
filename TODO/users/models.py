from django.db import models
from django.contrib.auth import get_user_model


class User(get_user_model()):
    user_email = models.EmailField(unique=True)
