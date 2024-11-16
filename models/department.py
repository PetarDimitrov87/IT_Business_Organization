from models import Manager
from json import JSONDecodeError
import json

class Department:
    """Class for department containing a list of managers."""
    def __init__(self, name : str, managers : list[Manager] = None):
        self.name = name
        if managers is not None:
            self.managers = managers
        else:
            self.managers = []

    def add_manager(self, manager : Manager):
        if manager in self.managers:
            raise ValueError("The manager is already in the department.")
        else:
            self.managers.append(manager)

    def remove_manager(self, manager : Manager):
        if manager not in self.managers:
            raise ValueError("The manager is not in the department.")
        else:
            self.managers.remove(manager)

    def give_salary(self):
        for manager in self.managers:
            print(f"{manager.first_name} {manager.last_name} received {round(manager.calculate_salary())} money.")
            for __ in manager.team:
                print(f"{manager.first_name} {manager.last_name} received "
                      f"{round(manager.calculate_salary())} money.")

    def serialize_employees(self, filename):
        with open(filename, "w") as file:
            json.dump([manager.to_dictionary() for manager in self.managers], file, indent = 3)

        message = f"Data saved to {filename}."
        print(message)

    def deserialize_employees(self, filename = "data/list_of_employees.json"):
        try:
            with open(filename, "r") as file:
                employees = json.load(file)
                self.managers = [Manager.deserialize_employee(data) for data in employees]
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except JSONDecodeError as error:
            print(f"Error decoding JSON from file '{filename}': {error}.")