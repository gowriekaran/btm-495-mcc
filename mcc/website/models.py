from django.db import models
from django.conf import settings
from django.utils import timezone

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
        return f"Position: {self.id} - Name: {self.name} - Description: {self.description} - Status: {self.status}"

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    studentID = models.CharField(max_length=10)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"ID: {self.id} - Student ID: {self.studentID}, Name: {self.firstName} {self.lastName}, Email: {self.email}, Phone Number: {self.phoneNumber}"
    
class Submission(models.Model):
    id = models.AutoField(primary_key=True)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    selectedPositionID = models.ForeignKey(Position, on_delete=models.CASCADE)
    experience = models.TextField()
    dateSubmitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission: {self.id}, [{self.studentID}] - [{self.selectedPositionID}] - Experience: {self.experience} - Date Submitted: {self.dateSubmitted}"

class Candidate(Student):
    CANDIDATE = 'Candidate'
    INTERVIEW = 'Interview'
    OFFERED = 'Offered'
    REJECTED = 'Rejected'
    HIRED = 'Hired'

    STATUS_CHOICES = [
        (CANDIDATE, 'Candidate'),
        (INTERVIEW, 'Interview'),
        (OFFERED, 'Offered'),
        (REJECTED, 'Rejected'),
        (HIRED, 'Hired'),
    ]

    submissionID = models.ForeignKey(Submission, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=CANDIDATE)

    def __str__(self):
        return f"Candidate: {self.id} - [{self.submissionID} - {self.status}"

class Interview(models.Model):
    SCHEDULING = "Scheduling"
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"

    STATUS_CHOICES = [
        (SCHEDULING, 'Scheduling'),
        (SCHEDULED, 'Scheduled'),
        (COMPLETED, 'Completed'),
    ]

    id = models.AutoField(primary_key=True)
    candidateID = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    dateTime = models.DateTimeField(null=True)
    location = models.TextField(null=True)
    feedback = models.TextField(null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=SCHEDULING)

    def __str__(self):
        return f"Interview: {self.id} - [{self.candidateID}] - {self.dateTime} - {self.location} - {self.feedback} - {self.status}"

class Availability(models.Model):
    id = models.AutoField(primary_key=True)
    interviewID = models.ForeignKey(Interview, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        project_timezone = timezone.get_current_timezone()
        localized_time = timezone.localtime(self.dateTime, project_timezone)

        return f"Availability: {self.id} - [{self.interviewID}] - {localized_time.strftime('%Y-%m-%d %H:%M:%S')} - {self.isApproved}"