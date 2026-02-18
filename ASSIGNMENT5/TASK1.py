results = {
    "alice":590,
    "bob":600,
    "john":666,
}

student_name = input("Enter Student Name: ").lower()
if student_name in results:
    print(f"{student_name}'s marks: {results[student_name]}")
else:
    print("Student not found")