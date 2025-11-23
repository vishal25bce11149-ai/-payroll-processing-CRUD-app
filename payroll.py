import json
import os

class PayrollSystem:
    def __init__(self, filename="employees.json"):
        self.filename = filename
        self.employees = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return {}
        return {}
    
    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.employees, file, indent=4)
    
    def add_employee(self):
        print("\n--- Add New Employee ---")
        emp_id = input("Enter Employee ID: ") 
        if emp_id in self.employees:
            print("Employee ID already exists!")
            return
        name = input("Enter Employee Name: ")
        try:
            basic_salary = float(input("Enter Basic Salary: "))
            hours_worked = float(input("Enter Hours Worked: "))
            hourly_rate = float(input("Enter Hourly Rate: "))
        except ValueError:
            print("Invalid input! Please enter numeric values for salary/hours/rate.")
            return
        gross_salary = basic_salary + (hours_worked * hourly_rate)
        self.employees[emp_id] = {
            'name': name,
            'basic_salary': basic_salary,
            'hours_worked': hours_worked,
            'hourly_rate': hourly_rate,
            'gross_salary': gross_salary
        }
        self.save_data()
        print(f"Employee {name} added successfully!")
    
    def view_employees(self):
        print("\n--- Employee List ---")
        if not self.employees:
            print("No employees found!")
            return
        for emp_id, details in self.employees.items():
            print(f"ID: {emp_id}")
            print(f"Name: {details['name']}")
            print(f"Basic Salary: ₹{details['basic_salary']:.2f}")
            print(f"Hours Worked: {details['hours_worked']}")
            print(f"Hourly Rate: ₹{details['hourly_rate']:.2f}")
            print(f"Gross Salary: ₹{details['gross_salary']:.2f}")
            print("-" * 30)
    
    def search_employee(self):
        print("\n--- Search Employee ---")
        emp_id = input("Enter Employee ID to search: ")
        if emp_id in self.employees:
            details = self.employees[emp_id]
            print(f"\nEmployee Found:")
            print(f"ID: {emp_id}")
            print(f"Name: {details['name']}")
            print(f"Basic Salary: ₹{details['basic_salary']:.2f}")
            print(f"Hours Worked: {details['hours_worked']}")
            print(f"Hourly Rate: ₹{details['hourly_rate']:.2f}")
            print(f"Gross Salary: ₹{details['gross_salary']:.2f}")
        else:
            print("Employee not found!")
    
    def update_employee(self):
        print("\n--- Update Employee ---")
        emp_id = input("Enter Employee ID to update: ") 
        if emp_id not in self.employees:
            print("Employee not found!")
            return
        details = self.employees[emp_id]
        print(f"Current details for {details['name']}:")
        print(f"1. Name: {details['name']}")
        print(f"2. Basic Salary: ₹{details['basic_salary']:.2f}")
        print(f"3. Hours Worked: {details['hours_worked']}")
        print(f"4. Hourly Rate: ₹{details['hourly_rate']:.2f}")
        try:
            choice = input("\nEnter field number to update (1-4), or 'all' to update all: ")
            if choice == '1' or choice.lower() == 'all':
                details['name'] = input("Enter new name: ") 
            if choice == '2' or choice.lower() == 'all':
                details['basic_salary'] = float(input("Enter new basic salary: "))
            if choice == '3' or choice.lower() == 'all':
                details['hours_worked'] = float(input("Enter new hours worked: "))
            if choice == '4' or choice.lower() == 'all':
                details['hourly_rate'] = float(input("Enter new hourly rate: "))
            details['gross_salary'] = details['basic_salary'] + (details['hours_worked'] * details['hourly_rate'])
            self.employees[emp_id] = details
            self.save_data()
            print("Employee details updated successfully!")
        except ValueError:
            print("Invalid input! Please enter numeric values where required.")
    
    def delete_employee(self):
        print("\n--- Delete Employee ---")
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in self.employees:
            name = self.employees[emp_id]['name']
            confirm = input(f"Are you sure you want to delete {name}? (y/n): ")
            if confirm.lower() == 'y':
                del self.employees[emp_id]
                self.save_data()
                print(f"Employee {name} deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("Employee not found!")
    
    def calculate_payroll_summary(self):
        print("\n--- Payroll Summary ---")
        if not self.employees:
            print("No employees found!")
            return
        total_salary = 0
        employee_count = len(self.employees)
        print(f"Total Employees: {employee_count}")
        print("\nIndividual Salaries:")
        print("-" * 40)
        for emp_id, details in self.employees.items():
            salary = details['gross_salary']
            total_salary += salary
            print(f"{details['name']}: ₹{salary:.2f}")
        print("-" * 40)
        print(f"Total Payroll: ₹{total_salary:.2f}")
        if employee_count > 0:
            print(f"Average Salary: ₹{total_salary/employee_count:.2f}")
    
    def display_menu(self):
        print("\n" + "="*50)
        print("        PAYROLL PROCESSING SYSTEM")
        print("="*50)
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Payroll Summary")
        print("7. Exit")
        print("="*50)

def main():
    payroll = PayrollSystem()
    while True:
        payroll.display_menu()
        try:
            choice = input("\nEnter your choice (1-7): ")
            if choice == '1':
                payroll.add_employee()
            elif choice == '2':
                payroll.view_employees()
            elif choice == '3':
                payroll.search_employee()
            elif choice == '4':
                payroll.update_employee()
            elif choice == '5':
                payroll.delete_employee()
            elif choice == '6':
                payroll.calculate_payroll_summary()
            elif choice == '7':
                print("Thank you for using Payroll Processing System!")
                break
            else:
                print("Invalid choice! Please enter a number between 1-7.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()