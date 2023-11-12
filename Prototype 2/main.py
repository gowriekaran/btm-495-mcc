from offer import Offer
from position import Position
from interview import Interview
from president import President
from mccTeamMember import MccTeamMember
from candidate import Candidate
from student import Student
from submission import Submission

import os

os.system('cls' if os.name == 'nt' else 'clear')

print("##### STUDENTS #####")

student1 = Student(1, "John", "Doe", "john@example.com", "123-456-7890")
student2 = Student(2, "Jane", "Smith", "jane@example.com", "987-654-3210")
student3 = Student(3, "Alice", "Johnson", "alice@example.com", "555-123-4567")
student4 = Student(4, "Bob", "Brown", "bob@example.com", "111-222-3333")
student5 = Student(5, "Eva", "Williams", "eva@example.com", "777-888-9999")

students = [student1, student2, student3, student4, student5]

for student in students:
    print(f"Student {student.get_id()}:", student.get_student_id(), student.get_first_name(), student.get_last_name(), student.get_email(), student.get_phone_number())

print("\n##### POSITIONS #####")

position1 = Position("Business Analyst", "Analyze business processes and data", "Filled")
position2 = Position("Sales Manager", "Manage sales team and strategies", "Filled")
position3 = Position("Financial Analyst", "Analyze financial data and trends", "Filled")
position4 = Position("Marketing Coordinator", "Coordinate marketing campaigns", "Open")
position5 = Position("Human Resources Specialist", "Manage HR functions and employee relations", "Open")

positions = [position1, position2, position3, position4, position5]

for position in positions:
    print(f"Position {position.get_id()}:", position.get_name(), position.get_description(), "Status:", position.get_status())

print("\n##### SUBMISSIONS #####")

submission1 = Submission(1, 1, "Relevant experience 1", "2023-01-11")
submission2 = Submission(2, 2, "Relevant experience 2", "2023-01-12")
submission3 = Submission(3, 3, "Relevant experience 3", "2023-01-13")
submission4 = Submission(2, 3, "Relevant experience 2.1", "2023-01-12")
submission5 = Submission(4, 4, "Relevant experience 4", "2023-01-14")
submission6 = Submission(5, 5, "Relevant experience 5", "2023-01-15")

submissions = [submission1, submission2, submission3, submission4, submission5, submission6]

for submission in submissions:
    print(f"Submission {submission.get_id()}: Student {submission.get_student_id()} for Position {submission.get_position_id()}. Experience: {submission.get_experience()}. Date submitted: {submission.get_date_submitted()}")

print("\n##### CANDIDATES #####")

candidate1 = Candidate(student1, submission1.get_id())
candidate2 = Candidate(student2, submission4.get_id())

candidates = [candidate1, candidate2]

for candidate in candidates:
    print(f"Candidate {candidate.get_id()}: Student {candidate.get_student_id()} and Submission {candidate.get_submission_id()} - ", candidate.get_first_name(), candidate.get_last_name(), candidate.get_email(), candidate.get_phone_number())

print("\n##### INTERVIEWS #####")

interview1 = Interview(candidate1.get_id(),"2023-02-01", "10:00 AM", "JMSB")
interview2 = Interview(candidate2.get_id(),"2023-02-01", "11:30 AM", "JMSB")

interviews = [interview1, interview2]

for interview in interviews:
    print(f"Interview {interview.get_id()}: Candidate {interview.get_candidate_id()} on {interview.get_date()} at {interview.get_time()} @ {interview.get_location()}")

print("\n##### OFFERS #####")

offer1 = Offer("$24/hr", candidate1.get_id(), submission1.get_position_id())
offer2 = Offer("$28/hr", candidate2.get_id(), submission4.get_position_id())

offers = [offer1, offer2]

for offer in offers:
    print(f"Offer {offer.get_id()}: Candidate {offer.get_candidate_id()} for Position {offer.get_position_id()} - {offer.get_details()}")

print("\n##### MCC TEAM MEMBERS #####")

mcc_team_member1 = MccTeamMember(student1, 1)
mcc_team_member2 = MccTeamMember(student2, 2)

mcc_team_members = [mcc_team_member1, mcc_team_member2]

for mcc_team_member in mcc_team_members:
    print(f"Mcc Team Member {mcc_team_member.get_id()}: Position {mcc_team_member.get_position_id()} - ", mcc_team_member.get_first_name(), mcc_team_member.get_last_name(), mcc_team_member.get_email(), mcc_team_member.get_phone_number())
