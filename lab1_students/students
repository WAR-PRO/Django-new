#!/usr/bin/env python

students = [
    {
        "surname" : "Ivanov",
        "ratings" : [4, 4, 5, 4, 5, 5, 5, 5]
    },
    {
        "surname" : "Petrov",
        "ratings" : [4, 5, 3, 3, 4, 4, 5, 4]
    },
    {
        "surname" : "Sidorov",
        "ratings" : [3, 3, 4, 4, 4, 4, 3, 4]
    },
    {
        "surname" : "Karpov",
        "ratings" : [5, 4, 5, 5, 5, 5, 5, 5]
    },
    {
        "surname" : "Serebryakov",
        "ratings" : [4, 4, 3, 4, 4, 5, 4, 4]
    },
    {
        "surname" : "Romanov",
        "ratings" : [3, 3, 4, 3, 3, 4, 4, 3]
    },
    {
        "surname" : "Geizenberg",
        "ratings" : [4, 4, 4, 5, 5, 4, 5, 5]
    },
    {
        "surname" : "Tarasov",
        "ratings" : [4, 4, 5, 4, 4, 4, 4, 5]
    },
    {
        "surname" : "Pyetukhov",
        "ratings" : [5, 5, 4, 3, 5, 4, 5, 5]
    },
    {
        "surname" : "Voronin",
        "ratings" : [4, 4, 5, 4, 4, 5, 4, 5]
    }
]

def CountAverageRating(student):
    summ = 0
    for rating in student["ratings"]:
        summ += rating
    return float(summ) / float(len(student["ratings"]))

def FilterStudents(students, averageRating):
    filteredStudents = []
    for student in students:
        if CountAverageRating(student) >= averageRating:
            filteredStudents.append(student)
    return filteredStudents

def GetRatingsStr(student):
    result = ""
    for rating in student["ratings"]:
        result += str(rating) + " "
    return result

print("Input average rating:");
targetAverage = float(input());
filteredStudents = FilterStudents(students, targetAverage);
print("Students with average rating higher than entered average rating:")
for student in filteredStudents:
    print(student["surname"].rjust(15) + ": " + str(student["ratings"]).strip('[]'))
