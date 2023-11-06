from django.contrib import admin
from .models import Position
from .models import Student
from .models import Submission

admin.site.register(Position)
admin.site.register(Student)
admin.site.register(Submission)
