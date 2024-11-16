import pytest
from models import *

@pytest.mark.department_creation_tests
class TestDepartmentCreation:
    @pytest.fixture()
    def test_create_empty_department(self):
        department = Department()

        assert department.managers is not None
        assert len(department.managers) == 0

    def test_add_one_manager_to_department(self):
        department = Department()

        department.managers = [Manager("Hristo", "Ivanov", 10000, 20)]

        assert len(department.managers) == 1

@pytest.mark.department_managers_tests
class TestDepartmentAddManager:
    @pytest.fixture()
    def test_add_one_valid_manager(self):
        department = Department(name = "Software Development")
        manager = Manager("Boris", "Hristov", 10000, 20)

        department.add_manager(manager)

        assert len(department.managers) == 1
        assert department.managers[0] == manager

    @pytest.fixture()
    def test_add_invalid_manager(self):
        department = Department(name = "IT Whizzards")
        manager = Designer("Kristiana", "Stoyanova", 3000, 1)

        department.add_manager(manager)

        assert type(manager) is not Manager
        assert len(department.managers) == 0

    @pytest.fixture()
    def test_remove_valid_manager(self):
        department = Department(name = "Dev team 1")
        manager = Manager("Marin", "Bogdanov", 8000, 15)

        department.add_manager(manager)

        assert len(department.managers) == 1

        department.remove_manager(manager)

        assert len(department.managers) == 0

    @pytest.fixture()
    def test_remove_invalid_manager(self):
        department = Department(name = "Design team 2")
        manager = Manager("Ralitsa", "Blagoeva", 4000, 3)

        department.add_manager(manager)

        assert len(department.managers) == 1

        invalid_manager = Manager("ivan", "Dimitrov", 6000, 5)

        try:
            department.remove_manager(invalid_manager)
        except ValueError as error:
            assert str(error) == "The manager is not in the department."