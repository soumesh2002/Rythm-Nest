from django.db import models
import string
import random
from django.utils import timezone


# generate unique code
def generate_unique_code():
    max_length = 6

    while True:
        code = "".join(random.choices(string.ascii_uppercase, k=max_length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code


class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, unique=True)
    votes_to_skip = models.IntegerField(null=False, unique=True)
    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
