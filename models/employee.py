class Employee():
    """Abstract class for employees."""
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int):
        if not first_name.isalpha():
            raise TypeError("First name must contain letters only.")
        self.first_name = first_name

        if not last_name.isalpha():
            raise TypeError("First name must contain letters only.")
        self.last_name = last_name

        if not isinstance(base_salary, (int, float)):
            raise TypeError("Base salary must be a number.")
        if base_salary <= 0:
            raise ValueError("Base salary must be greater than zero.")
        self.base_salary = base_salary

        if not isinstance(experience, int):
            raise TypeError("Experience must be a whole number.")
        if experience < 0:
            raise ValueError("Experience must be greater than zero.")
        self.experience = experience

    def calculate_salary(self) -> int:
        salary = self.base_salary

        if self.experience in range(2, 6):
            salary += 200
        elif self.experience > 5:
            salary *= 1.2 + 500

        return round(salary)

    def __str__(self):
        return (f"{self.first_name} {self.last_name} is a {type(self).__name__} "
                f"with a salary of {self.calculate_salary()} and {self.experience} of experience.")

    def to_dictionary(self):
        return {
            "type": self.__class__.__name__,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "base_salary": self.base_salary,
            "experience": self.experience
        }

    @classmethod
    def from_dictionary(cls, data):
        return cls(
            data["first_name"],
            data["last_name"],
            data["base_salary"],
            data["experience"]
        )