from django.db import models
from django.contrib.auth import get_user_model
from safedelete.models import SafeDeleteModel

User = get_user_model()


class Leave(SafeDeleteModel):
    SICK_LEAVE = 0
    EMERGENCY_LEAVE = 1
    TYPES = (
        (SICK_LEAVE, 'Sick Leave'),
        (EMERGENCY_LEAVE, 'Emergency Leave'),
    )

    day = models.DateField('Leave Day Date', auto_now_add=True)
    type = models.PositiveSmallIntegerField(choices=TYPES)
    user = models.ForeignKey(User, related_name='leave_days', on_delete=models.PROTECT)

    def __str__(self):
        return "{0.user} has a {0.get_type_display} on {0.date}".format(self)
