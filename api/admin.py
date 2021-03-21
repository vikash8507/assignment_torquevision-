from django.contrib import admin
from api.models import Member, ActivityPeriod

# Register models in admin panel
admin.site.register(Member)
admin.site.register(ActivityPeriod)
