import json


def employee_list():
    with open('database\\employee.json', 'r') as f:
        employeeList = json.load(f)

    return employeeList


def employee_list_search(_id):
    employeeList = employee_list()
    return employeeList[_id]


def employee_list_update(updatedList):
    with open('database\\employee.json', 'w') as f:
        f.write(json.dumps(updatedList, indent=4))


class Employee:

    def __init__(self, employeeDetails: dict):
        self.id = employeeDetails["id"]
        self.ic = employeeDetails["name"]
        self.name = employeeDetails["name"]
        self.phone = employeeDetails["phone"]
        self.email = employeeDetails["email"]
        self.username = employeeDetails["username"]
        self.password = employeeDetails["password"]
        self.role = 0
        self.details = {
            "id": self.id,
            "ic": self.ic,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    def __repr__(self):
        return f'{self.details}'

    def add(self):
        employeeList = employee_list()
        employeeList.update({
            self.id: self.details
        })
        employee_list_update(employeeList)
