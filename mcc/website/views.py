from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Position
from .models import Student
from .models import Submission

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
    return render(request, 'applicants.html', {"applicants": applicants})