students = {
    "Alex": 90,
    "Barbara": 85,
    "John": 70,
    "Michael": 60
}

average = sum(students.values()) / len(students)

for name, score in students.items():
    if score > average:
        print(name)