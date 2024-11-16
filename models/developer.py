from models import Employee

class Developer(Employee):
    """Derived Employee class."""
    def __init__(self, first_name, last_name, base_salary, experience):
        super().__init__(first_name, last_name, base_salary, experience)

    def to_dictionary(self):
        data = super().to_dictionary()
        data["type"] = "Developer"
        return data

    @classmethod
    def from_dictionary(cls, data):
        return cls(
            data["first_name"],
            data["last_name"],
            data["base_salary"],
            data["experience"]
        )