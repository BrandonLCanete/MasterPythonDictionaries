# Employee 1
employee_object_one = {
    "employee_id" : 1,
    "employee_name" : "Arthur Morgan",
    "employee_job_title" : "Designer",
    "employee_department" : "IT",
    "employee_salary" : "20,000.00",
    "employee_schedule_work" : "Monday to Friday"
}
# Employee 2
employee_object_two = {
    "employee_id" : 2,
    "employee_name" : "Henry Goose",
    "employee_job_title" : "Developer",
    "employee_department" : "IT",
    "employee_salary" : "30,000.00",
    "employee_schedule_work" : "Monday to Saturday"
}
# Employee 3
employee_object_three = {
    "employee_id" : 3,
    "employee_name" : "Jeffrey Morrey",
    "employee_job_title" : "Advertiser",
    "employee_department" : "HR",
    "employee_salary" : "25,000.00",
    "employee_schedule_work" : "Monday to Thursday"
}
# Employee 4
employee_object_four = {
    "employee_id" : 4,
    "employee_name" : "Godfrey Huther",
    "employee_job_title" : "Engineer",
    "employee_department" : "Construction",
    "employee_salary" : "35,000.00",
    "employee_schedule_work" : "Monday to Friday"
}
# Employee 5
employee_object_five = {
    "employee_id" : 5,
    "employee_name" : "Angeline Grace",
    "employee_job_title" : "Secretary",
    "employee_department" : "HR",
    "employee_salary" : "33,000.00",
    "employee_schedule_work" : "Monday to Saturday"
}

# Hold the employee dictionaries to employees variable
employees = [employee_object_one,employee_object_two,employee_object_three,employee_object_four,employee_object_five]
# Loop through the dictionaries
for employee in employees:
    # Print the data
    print(f"Employee Name: {employee.get('employee_name')}, Employee Job Title: {employee.get('employee_job_title')}, Employee Department: {employee.get('employee_department')}, Employee Salary : {employee.get('employee_salary')}, Employee Schedule Work: {employee.get('employee_schedule_work')}")
