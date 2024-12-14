class Employee:
    def __init__(self, employee_id, name, organization):
        self.employee_id = employee_id
        self.name = name
        self.organization = organization
        self.attendance = []

    def mark_attendance(self, attendance):
        self.attendance.append(attendance)

    def get_attendance_percentage(self):
        if len(self.attendance) == 0:
            return 0
        return (self.attendance.count(True) / len(self.attendance)) * 100

def add_employee():
    employee_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    organization = input("Enter organization: ")
    employees.append(Employee(employee_id, name, organization))
    print("Employee added successfully!")

#True is indicated as present, while false is indicated as absent.

def mark_attendance():
    employee_id = input("Enter employee ID: ")
    for employee in employees:
        if employee.employee_id == employee_id:
            attendance = input("Enter attendance (True/False): ").lower()
            if attendance == "true":
                employee.mark_attendance(True)
            elif attendance == "false":
                employee.mark_attendance(False)
            else:
                print("Invalid attendance input.")
            print("Attendance marked successfully!")
            return
    print("Employee not found.")

def display_all_attendance():
    for employee in employees:
        print(f"Employee ID: {employee.employee_id}")
        print(f"Name: {employee.name}")
        print(f"Organization: {employee.organization}")
        print(f"Attendance: {employee.attendance}")
        print(f"Attendance Percentage: {employee.get_attendance_percentage()}%")
        print("--------------------------")

def calculate_attendance_percentage():
    total_attendance = 0
    total_days = 0
    for employee in employees:
        total_attendance += employee.attendance.count(True)
        total_days += len(employee.attendance)
    if total_days == 0:
        print("No attendance records found.")
    else:
        print(f"Class Attendance Percentage: {(total_attendance / total_days) *  100}%")

employees = []

while True:
    print("\nEmployee Attendance Tracker Menu:")
    print("1. Add Employee")
    print("2. Mark Attendance")
    print("3. Display All Attendance")
    print("4. Calculate Attendance Percentage")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        mark_attendance()
    elif choice == '3':
        display_all_attendance()
    elif choice == '4':
        calculate_attendance_percentage()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")


<!---
BSECEQUILO30/BSECEQUILO30 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
