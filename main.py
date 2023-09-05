
employee_table = [
{"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
{"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
{"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
{"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
{"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000}
]

print("Search options:")
print("1. Age")
print("2. Name")
print("3. Salary")
choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    age = int(input("Enter age to search: "))
    result = [emp for emp in employee_table if emp["Age"] == age]
elif choice == 2:
    name = input("Enter name to search: ")
    result = [emp for emp in employee_table if emp["Name"].lower() == name.lower()]
elif choice == 3:
    salary_op = input("Enter salary operator (<, >, <=, >=): ")
    salary = int(input("Enter salary to search: "))
    
    if salary_op == "<":
        result = [emp for emp in employee_table if emp["Salary (PM)"] < salary]
    elif salary_op == ">":
        result = [emp for emp in employee_table if emp["Salary (PM)"] > salary]
    elif salary_op == "<=":
        result = [emp for emp in employee_table if emp["Salary (PM)"] <= salary]
    elif salary_op == ">=":
        result = [emp for emp in employee_table if emp["Salary (PM)"] >= salary]
    else:
        print("Invalid operator")
        
else:
    print("Invalid choice")
    

if len(result) == 0:
    print("No matching records found")
else:
    print("Matching records:")
    for emp in result:
        print(f"Employee ID: {emp['Employee ID']}, Name: {emp['Name']}, Age: {emp['Age']}, Salary (PM): {emp['Salary (PM)']}")
