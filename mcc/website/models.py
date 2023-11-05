from django.db import models

class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"Position: {self.id} - {self.name} - {self.description} - {self.status}"