# Create dictionary of course numbers and room numbers
room_dict = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

# Create dictionary of course numbers and instructors
instructor_dict = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

# Create dictionary of course numbers and meeting times
meeting_dict = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# Prompt user for course number
course = input("Enter a course number: ")

# Look up room number, instructor, and meeting time based on course number
if course in room_dict:
    room_num = room_dict[course]
    instructor = instructor_dict[course]
    meeting_time = meeting_dict[course]
    print(f"Room number: {room_num}")
    print(f"Instructor: {instructor}")
    print(f"Meeting time: {meeting_time}")
else:
    print("Invalid course number.")

