
# Day 2 - Python Fundamentals Practice
# OUBT Bootcamp | Author: Likhith Sasank Uppalapati Venkata

numbers = [1,2,3,4,5]

squares = [x**2  for x in numbers]
print(squares)


def print_hello(dev):
    return f"Hello, {dev}! Welcome to our OUBT Bootcamp."

print(print_hello("Likhith"))


student = {"name":"Likhith","Week":1,"topic":"Python for Data engineering"}

for (key,value) in student.items():
    print(f"{key}:{value}")


def get_grade(marks):
    if marks >= 90:
        return 'First Class'
    elif marks >= 75:
        return 'Second Class'
    elif marks >= 60:
        return 'Third Class'
    else:
        return 'Fail'
    

print(get_grade(99))

import csv

data =[
    ["Name","Score"],
    ["Likhith",95],
    ["Sasank",85],
    ["Venkata",70]
]


with open('data/raw/scores.csv', 'w',newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("CSV file created successfully in data/raw/scores.csv")


invoices = [
    ["InvoiceId","Amount","Status"],
    ["Likhith",75000,"Paid"],
    ["Seth",55000,"Pending"]
]

with open('data/raw/invoices.csv','w',newline="") as file:
    writer = csv.writer(file)
    writer.writerows(invoices)
print("CSV file created successfully in data/raw/invoices.csv")




try:
    result= 10/0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


employee = [{"name":"Likhith","age":25,"salary":80000},
            {"name":"Sasank","age":27,"salary":75000},
            {"name":"Venkata","age":30,"salary":90000}
]

highly_paid_devs = [emp for emp in employee if emp["salary"] > 75000]
print(f"highly paid developers are :{highly_paid_devs}")

for(employee) in highly_paid_devs:
    print(f"{employee['name']} with salary {employee['salary']}")



