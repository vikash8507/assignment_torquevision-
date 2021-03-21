from api.models import Member, ActivityPeriod
from faker import Faker
import random
import pytz

# This method generate fake data for models
fake = Faker()
    # Timezones
TIME_ZONES = ['Europe/Paris', 'Africa/Kampala', 'Asia/Colombo', 'Asia/Riyadh',
                'Africa/Luanda', 'Europe/Vienna', 'Asia/Calcutta', 'Asia/Dubai', 'Europe/London'
            ]

def generating_data():
    # Delete previous data
    Member.objects.all().delete()

    # Generate 10 members data
    for _ in range(5):
        # Real name of member
        real_name = fake.name()

        # TIME_ZONE for member
        index = random.randint(0, len(TIME_ZONES)-1)
        tz = TIME_ZONES[index]

        # Create member object
        member = Member(
            real_name=real_name,
            tz=tz
        )

        # Save member data
        member.save()

        # Generate 3 different activity period for every member
        for _ in range(3):

            time_zone = pytz.timezone(tz)

            # End time
            end_time = fake.date_time(tzinfo=time_zone)

            # Start time
            start_time = fake.date_time(tzinfo=time_zone)

            # Correct way start time and end time
            if(start_time > end_time):
                temp = start_time
                start_time = end_time
                end_time = temp

            # Create activity period object
            activity = ActivityPeriod(
                member=member,
                start_time=start_time,
                end_time=end_time,
            )

            # Save activity period data
            activity.save()
