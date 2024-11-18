from models import Employee
from models import Developer
from models import Designer

class Manager(Employee):
    """Derived Employee class."""
    def __init__(self, first_name : str, last_name : str, base_salary : float, experience : int, team : list[Developer, Designer] = None):
        super().__init__(first_name, last_name, base_salary, experience)
        if team is not None:
            self.team = team
        else:
            self.team = []

    def calculate_salary(self) -> int:
        salary = super().calculate_salary()
        team_size = len(self.team)

        if 5 < team_size <= 10:
            salary += 200
        # here it would be better use elif
        # It's more efficient - if the first condition is true, it won't check the second condition unnecessarily
        if team_size > 10:
            salary += 300

        dev_count = 0

        for member in self.team:
            if isinstance(member, Developer):
                dev_count += 1

        if dev_count > team_size / 2:
            salary *= 1.1

        return salary

    def add_team_member(self, member):
        if isinstance(member, (Developer, Designer)):
            self.team.append(member)
        else:
            raise TypeError("Only developers and designers can be members of the team.")
        # here it would be better check if Developer or Designer with certain first and last name already presents in team
        if member in self.team:
            raise ValueError("The member is already in the team.")

    def remove_team_member(self, member):
        if member not in self.team:
            raise ValueError("The member is not in the team.")
        else:
            self.team.remove(member)

    def __str__(self):
        base = super().__str__()
        length = len(self.team)

        return f"{base} They manage a team of {length} developers and designers."

    def to_dictionary(self):
        data = super().to_dictionary()
        data["team"] = [member.to_dictionary() for member in self.team]

        return data

    @classmethod
    def from_dictionary(cls, data):
        manager = cls(
            data["first_name"],
            data["last_name"],
            data["base_salary"],
            data["experience"]
        )
        manager.team = [cls.deserialize_employee(member_data) for member_data in data["team"]]

        return manager

    def deserialize_employee(data):
        if data["type"] == "Developer":
            return Developer.from_dictionary(data)
        elif data["type"] == "Designer":
            return Designer.from_dictionary(data)
        elif data["type"] == "Manager":
            return Manager.from_dictionary(data)
        else:
            raise ValueError(f"Unknown employee type: {data['type']}")