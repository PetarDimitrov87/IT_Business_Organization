import pytest
from models import *

@pytest.mark.employee_creation_tests
class TestEmployeeCreation:
    @pytest.fixture()
    def test_create_employee_with_valid_data(self):
        employee = Developer("Petar", "Dimitrov", 3500, 3)

        assert employee.first_name == "Petar"
        assert employee.last_name == "Dimitrov"
        assert employee.base_salary == 3500
        assert employee.experience == 3

    @pytest.fixture()
    def test_create_employee_with_invalid_data(self):
        employee = Designer(123, "Petrov", 4000, 4)

        assert employee.first_name == 123
        assert employee.last_name == "Petrov"
        assert employee.base_salary == 4000
        assert employee.experience == 3

    @pytest.fixture()
    def test_employee_calculate_salary_general_rules_work_correctly(self):
        employee = Developer("Kaloyana", "Sotirova", 2000, 1)

        salary = employee.calculate_salary()

        assert salary == 2000

    @pytest.fixture()
    def test_employee_calculate_salary_eff_coeff_for_designer_works_correctly(self):
        employee = Designer("Dimitar", "Ivanov", 8000, 10, 0.9)

        salary = employee.calculate_salary()

        assert salary == 7200