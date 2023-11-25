from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Position
from .models import Student
from .models import Candidate
from .models import Submission
from .models import Interview
from .models import Availability
from django.http import JsonResponse


def home(request):
    return render(request, 'home.html', {})

def admin_hub(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('admin-hub')
        else:
            messages.success(request, "There was an error logging in!")
            return redirect('admin-hub')
    else:
        return render(request, 'admin-hub.html', {})

def student_hub(request):
    positions = Position.objects.filter(status='Open').order_by('id')
    return render(request, 'student-hub.html', {"positions": positions})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out! Goodbye :)")
    return redirect('home')


@login_required
def positions(request):
    positions = Position.objects.all().order_by('id')
    return render(request, 'positions.html', {"positions": positions})

@login_required
def add_position(request):
    if request.method == 'POST':
        if 'add_button' in request.POST:
            name = request.POST['positionName']
            description = request.POST['positionDescription']
            status = request.POST['positionStatus']

            position = Position(name=name, description=description, status=status)
            position.save()
            messages.success(request, "Record was added!")
        elif 'cancel_button' in request.POST:
            messages.success(request, "Record add was cancelled!")
    return redirect('positions')

@login_required
def delete_position(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            instance = Position.objects.get(pk=id)
            instance.delete()
            messages.success(request, "Record was deleted!")
        except Position.DoesNotExist:
            messages.success(request, "Error: Record does not exist. Delete failed!")
    return redirect('positions')

@login_required
def edit_position(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            position = Position.objects.get(pk=id)
            edit_position = True
            positions = Position.objects.all().order_by('id')
            context = {'position': position,
                       'edit_position': edit_position, "positions": positions}
            messages.success(request, "Record is being edited!")
            return render(request, 'positions.html', context)
        except Position.DoesNotExist:
            messages.success(
                request, "Error: Record does not exist. Edit failed!")
    return redirect('positions')

@login_required
def update_position(request):
    if request.method == 'POST':
        if 'update_button' in request.POST:
            id = request.POST.get('id')
            try:
                position = Position.objects.get(pk=id)
                position.name = request.POST['positionName']
                position.description = request.POST['positionDescription']
                position.status = request.POST['positionStatus']
                position.save()
                messages.success(request, "Record was updated!")
            except Position.DoesNotExist:
                messages.success(
                    request, "Error: Update failed!")
        elif 'cancel_button' in request.POST:
            messages.success(request, "Record update was cancelled!")
    return redirect('positions')

def new_applicant(request):
    if request.method == 'POST':
        studentID = request.POST['student_id']
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']
        phoneNumber = request.POST['phone_number']
        positionID = request.POST['position']
        experience = request.POST['experience']

        student = Student.objects.filter(studentID=studentID).first()
        if student is None:
            student = Student(studentID=studentID, firstName=firstName, lastName=lastName, email=email, phoneNumber = phoneNumber)
            student.save()
            student = Student.objects.filter(studentID=studentID).first()
      
        position = Position.objects.filter(id=positionID).first()

        submission = Submission(studentID=student, selectedPositionID=position, experience=experience)
        submission.save()
        messages.success(request, "Record was added!")

        submissions = Submission.objects.filter(studentID=student)
    return redirect('thank-you')

def view_student_applications(request):
    studentID = request.POST['old_student_id']
    lastName = request.POST['old_last_name']

    student = Student.objects.filter(Q(studentID=studentID) & Q(lastName=lastName)).first()
    submissions = Submission.objects.filter(studentID=student)
    candidates = Candidate.objects.all().order_by('id')

    for submission in submissions:
        matching_candidate = candidates.filter(
            submissionID__studentID=submission.studentID,
            submissionID__selectedPositionID=submission.selectedPositionID
        ).first()

        if matching_candidate:
            submission.candidate_status = matching_candidate.status

            if(matching_candidate.status == "Interview"):
                interviewID = Interview.objects.get(candidateID=matching_candidate)
                submission.interviewID = interviewID
                if(interviewID.status == "Scheduled"):
                    availability = Availability.objects.filter(Q(isApproved=True) & Q(interviewID=interviewID)).first()
                    submission.availability = availability
        else:
            submission.candidate_status = "Application Received"

    return render(request, 'applications.html', {"student": student, "submissions": submissions})

def applications(request):
    student = request.GET.get('student', None)
    if student is not None:
        return render(request, 'applications.html', {"student": student})
    return redirect('student-hub')

def thank_you(request):
    return render(request, 'thank-you.html')

@login_required
def applicants(request):
    applicants = Submission.objects.all().order_by('id')
    candidates = Candidate.objects.all().order_by('id')

    for applicant in applicants:
        matching_candidates = candidates.filter(
            submissionID__studentID=applicant.studentID,
            submissionID__selectedPositionID=applicant.selectedPositionID
        )

        applicant.isCandidate = matching_candidates.exists()

    return render(request, 'applicants.html', {"applicants": applicants})

@login_required
def add_candidate(request):
    if request.method == 'POST':
        ID = request.POST['ID']
        submissionID = request.POST['submissionID']

        student = Student.objects.get(id=ID)
        submission = Submission.objects.get(id=submissionID)

        candidate = Candidate.objects.create(
            studentID=student.studentID,
            firstName=student.firstName,
            lastName=student.lastName,
            email=student.email,
            phoneNumber=student.phoneNumber,
            submissionID=submission
        )

        candidate.save()
        messages.success(request, "Record was added!")
    return redirect('applicants')

@login_required
def candidates(request):
    candidates = Candidate.objects.all().order_by('id')
    return render(request, 'candidates.html', {"candidates": candidates})

@login_required
def interviews(request):
    interviews = Interview.objects.all().order_by('id')
    availabilities = Availability.objects.all().order_by('id')

    for interview in interviews:
        matching_availability = availabilities.filter(
            interviewID__id=interview.id,
            isApproved=True
        ).first()

        interview.details = "Waiting for Candidate to share availabilities."

        if matching_availability:
            interview.details = matching_availability.dateTime

    return render(request, 'interviews.html', {"interviews": interviews, "availabilities": availabilities})

@login_required
def add_interview(request):
    if request.method == 'POST':
        ID = request.POST['ID']
        candidate = Candidate.objects.get(id=ID)
        candidate.status = 'Interview'
        candidate.save()

        interview = Interview(candidateID=candidate)
        interview.save()
        messages.success(request, "Record was added!")
    return redirect('candidates')

@login_required
def cancel_interview(request):
    if request.method == 'POST':
        ID = request.POST['ID']
        candidate = Candidate.objects.get(id=ID)
        candidate.status = 'Candidate'
        candidate.save()

        interview = Interview.objects.get(candidateID=candidate)
        availabilities = Availability.objects.filter(interviewID=interview.id)
        for availability in availabilities:
            availability.delete()
        interview.delete()
        messages.success(request, "Record was deleted!")
    return redirect('interviews')

def add_availability(request):
    if request.method == 'POST':
        studentID = request.POST['old_student_id']
        lastName = request.POST['old_last_name']

        student = Student.objects.filter(Q(studentID=studentID) & Q(lastName=lastName)).first()
        submissions = Submission.objects.filter(studentID=student)

        ID = request.POST['interviewID']
        interview = Interview.objects.get(id=ID)

        interview.requestMoreAvailability = False
        interview.save()

        time = request.POST['interviewTime']
        date = request.POST['interviewDate']

        datetime = f'{date}T{time}'

        availability = Availability(interviewID=interview, dateTime=datetime)
        availability.save()
        messages.success(request, "Record was added!")
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@login_required
def select_availability(request):
    if request.method == 'POST':
        interviewID = request.POST['interviewID']
        availabilityID = request.POST['availabilityID']

        interview = Interview.objects.get(id=interviewID)
        availability = Availability.objects.get(id=availabilityID)

        interview.status = "Scheduled"
        interview.save()
        
        availability.isApproved = True
        availability.save()
        messages.success(request, "Record was updated!")
        return redirect('interviews')

@login_required
def request_more_availability(request):
    if request.method == 'POST':
        interviewID = request.POST['interviewID']

        interview = Interview.objects.get(id=interviewID)

        interview.requestMoreAvailability = True
        interview.save()
        
        messages.success(request, "Record was updated!")
        return redirect('interviews')