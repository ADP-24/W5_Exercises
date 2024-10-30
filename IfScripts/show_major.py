student_name = "Abbey Road"
student_major = "MUSIC"

if student_major == "MUSIC":
    major_name = "Arts in Music"
    department_office = "Jude Hall, Room 99"
elif student_major == "BIOL":
    major_name = "Biology"
    deparment_office = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    deparment_office = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    deparment_office = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    deparment_office = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    deparment_office = "Westly Hall, Room 310"
else:
    major_name = "Unknown"
    department_office = "Unknown"

print(f"Student Name: {student_name}")
print(f"Major: {major_name}")
print(f"Department office location: {department_office}")

# Examples used to run the code.

# Student Name: Alice Johnson
# Major: Arts in Music
# Department Office Location: Jude Hall, Room 99

# Student Name: Bob Smith
# Major: Biology
# Department Office Location: Science Bldg, Room 310

# Student Name: Charlie Brown
# Major: Computer Science
# Department Office Location: Sheppard Hall, Room 314

# Student Name: Diana Prince
# Major: English
# Department Office Location: Kerr Hall, Room 201