from django.db import models
import string
import random

# Generate random string id for Member


def generate_id():
    id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
    return id


# Member model
class Member(models.Model):
    id = models.CharField(max_length=10, primary_key=True, default=generate_id)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)

    def __str__(self):
        return self.real_name


# Activity Period model
class ActivityPeriod(models.Model):
    member = models.ForeignKey(
        Member, related_name="activity_periods", on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.member.real_name
