from student import Student  # Assuming the Student class is defined in a 'student.py' file

print("Testing Student class; Expecting to not be able to access attribute")

# Create an instance of the Student class
student1 = Student()

# Attempt to access class-level private attributes (should raise an AttributeError)
try:
    print(student1.__studentID)
except AttributeError as e:
    print("AttributeError:", e)

try:
    print(student1.__firstName)
except AttributeError as e:
    print("AttributeError:", e)

try:
    print(student1.__lastName)
except AttributeError as e:
    print("AttributeError:", e)

try:
    print(student1.__email)
except AttributeError as e:
    print("AttributeError:", e)

try:
    print(student1.__phoneNumber)
except AttributeError as e:
    print("AttributeError:", e)