from django.contrib import admin
from .models import Position
from .models import Student
from .models import Candidate
from .models import Submission
from .models import Interview
from .models import Availability
from .models import Offer

admin.site.register(Position)
admin.site.register(Student)
admin.site.register(Candidate)
admin.site.register(Submission)
admin.site.register(Interview)
admin.site.register(Availability)
admin.site.register(Offer)
