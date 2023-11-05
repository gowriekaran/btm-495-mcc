from django.db import models

class Position(models.Model):
    VACANT = 'Vacant'
    OPEN = 'Open'
    SHORTLIST = 'Shortlist'
    INTERVIEW = 'Interview'
    OFFERED = 'Offered'
    FILLED = 'Filled'

    STATUS_CHOICES = [
        (VACANT, 'Vacant'),
        (OPEN, 'Open'),
        (SHORTLIST, 'Shortlist'),
        (INTERVIEW, 'Interview'),
        (OFFERED, 'Offered'),
        (FILLED, 'Filled'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=VACANT)

    def __str__(self):
        return f"Position: {self.id} - {self.name} - {self.description} - {self.status}"
