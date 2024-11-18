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
    # No need to override this method
    # If the method does exactly the same thing, there's no need to override it - the parent's method will work correctly with the child class.
    def from_dictionary(cls, data):
        return cls(
            data["first_name"],
            data["last_name"],
            data["base_salary"],
            data["experience"]
        )