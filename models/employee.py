class Employee():
    """Abstract class for employees."""
    def __init__(self, first_name: str, last_name: str, base_salary: float, experience: int):
        # It would be better to move all validations to separate methods.
        # Each validator method has a single responsibility
        # Easier to maintain and modify validation rules
        self._validate_name(first_name, "First name")
        self._validate_name(last_name, "Last name")
        self._validate_salary(base_salary)
        self._validate_experience(experience)

        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        self.experience = experience

    @staticmethod
    def _validate_name(name: str, field: str) -> None:
        """Validate that a name contains only letters."""
        if not name.isalpha():
            raise TypeError(f"{field} must contain letters only.")

    @staticmethod
    def _validate_salary(salary: Union[int, float]) -> None:
        """Validate that salary is a positive number."""
        if not isinstance(salary, (int, float)):
            raise TypeError("Base salary must be a number.")
        if salary <= 0:
            raise ValueError("Base salary must be greater than zero.")

    @staticmethod
    def _validate_experience(experience: int) -> None:
        """Validate that experience is a non-negative integer."""
        if not isinstance(experience, int):
            raise TypeError("Experience must be a whole number.")
        if experience < 0:
            raise ValueError("Experience must be non-negative.")

    def calculate_salary(self) -> int:
        salary = self.base_salary

        # Using if 2 <= self.experience <= 5 is better than if self.experience in range(2, 6) for two main reasons:
        # Type Flexibility: Comparison operators work with both integers and floats, which makes code more future-proof (e.g., if we need to support 2.5 years of experience)
        # Performance: range() creates a sequence in memory, while comparison operators just perform direct value comparison, making it more memory efficient
        if 2 <= self.experience <= 5:
            salary += 200
        elif self.experience > 5:
            salary = salary * 1.2 + 500

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