from offer import Offer
from position import Position
from interview import Interview
from president import President
from mccTeamMember import MccTeamMember
from candidate import Candidate
from student import Student
from submission import Submission

student1 = Student(1, "John", "Doe", "john@example.com", "123-456-7890")
student2 = Student(2, "Jane", "Smith", "jane@example.com", "987-654-3210")
student3 = Student(3, "Alice", "Johnson", "alice@example.com", "555-123-4567")
student4 = Student(4, "Bob", "Brown", "bob@example.com", "111-222-3333")
student5 = Student(5, "Eva", "Williams", "eva@example.com", "777-888-9999")

students = [student1, student2, student3, student4, student5]

for student in students:
    print(f"Student {student.id}:", student.get_first_name(), student.get_last_name(), student.get_email(), student.get_phone_number())

Position(1, "Business Analyst", "Analyze business processes and data", "Filled"),
Position(2, "Sales Manager", "Manage sales team and strategies", "Filled"),
Position(3, "Financial Analyst", "Analyze financial data and trends", "Filled"),
Position(4, "Marketing Coordinator", "Coordinate marketing campaigns", "Open"),
Position(5, "Human Resources Specialist", "Manage HR functions and employee relations", "Open")

positions = [position1, position2, position3, position4, position5]

for position in positions:
    print(f"Position {position.id}:", position.get_name(), position.get_description(), "Status:", position.get_status())

submission1 = Submission(1, 1, "Relevant experience 1", "2023-01-11")
submission2 = Submission(2, 2, "Relevant experience 2", "2023-01-12")
submission3 = Submission(3, 3, "Relevant experience 3", "2023-01-13")
submission2 = Submission(2, 3, "Relevant experience 2.1", "2023-01-12")
submission4 = Submission(4, 4, "Relevant experience 4", "2023-01-14")
submission4 = Submission(5, 5, "Relevant experience 5", "2023-01-15")

submissions = [submission1, submission2, submission3, submission4, submission5]

for submission in submissions:
    student = submission.get_student()
    position = submission.get_position()
    print(f"Submission {submission.id}: Student {student.id} - {student.get_first_name()} {student.get_last_name()} for Position {position.id}: {position.get_name()}. Status: {submission.get_status()}")

mcc_team_member1 = MccTeamMember(1, 1, 1)
mcc_team_member2 = MccTeamMember(2, 2, 2)
mcc_team_member3 = MccTeamMember(3, 3, 3)

mcc_team_members = [mcc_team_member1, mcc_team_member2, mcc_team_member3]

for mcc_team_member in mcc_team_members:
    print(f"Mcc Team Member {mcc_team_member.get_submission_id()} - Offer {mcc_team_member.get_offer_id()} for Position {mcc_team_member.get_position_id()}")
