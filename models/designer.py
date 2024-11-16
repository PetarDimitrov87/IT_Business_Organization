from models import Employee

class Designer(Employee):
    """Derived Employee class."""
    def __init__(self, first_name : str, last_name : str, base_salary : float, experience : int, eff_coeff : float):
        super().__init__(first_name, last_name, base_salary, experience)
        if not isinstance(eff_coeff, float):
            raise TypeError("Efficiency coefficient must be a floating-point number.")
        self.eff_coeff = eff_coeff
        if not (0 <= eff_coeff <= 1):
            raise ValueError("Efficiency coefficient must be between 0 and 1.")
        self.eff_coeff = eff_coeff

    def calculate_salary(self) -> int:
        salary = super().calculate_salary()
        salary *= self.eff_coeff

        return round(salary)

    def to_dictionary(self):
        data = super().to_dict()
        data["eff_coeff"] = self.eff_coeff
        data["type"] = "Designer"
        return data

    @classmethod
    def from_dictionary(cls, data):
        return cls(
            data["first_name"],
            data["last_name"],
            data["base_salary"],
            data["experience"],
            data["eff_coeff"]
        )