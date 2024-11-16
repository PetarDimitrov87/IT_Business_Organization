import pytest
from models import *

@pytest.mark.manager_creation_tests
class TestManagerCreation:
    @pytest.fixture()
    def test_create_manager_with_valid_data(self):
        manager = Manager("Atanas", "Petrov", 6000, 5)

        assert manager.first_name == "Atanas"
        assert manager.last_name == "Petrov"
        assert manager.base_salary == 6000
        assert manager.experience == 5
        assert manager.team == []

    @pytest.fixture()
    def test_create_manager_with_invalid_data(self):
        manager = Manager("Todor", True, 8000, 20)

        assert manager.first_name == "Todor"
        assert manager.last_name == True
        assert manager.base_salary == 8000
        assert manager.experience == 20
        assert manager.team == []

@pytest.mark.manager_team_members_tests
class TestManagerAddAndRemoveTeamMembers:
    @pytest.fixture()
    def test_add_team_member_with_valid_data(self):
        manager = Manager("Silviya", "Georgieva", 9000, 12)

        developer = Developer("Rumen", "Slaveykov", 4000, 3)

        manager.add_team_member(developer)

        assert len(manager.team) == 1
        assert manager.team.__contains__(developer)

    @pytest.fixture()
    def test_add_team_member_of_invalid_type(self):
        manager = Manager("Vasil", "Yavorov", 7000, 6)

        designer = Manager("Borislav", "Krumov", 5000, 4)

        try:
            manager.add_team_member(designer)
        except TypeError as error:
            assert str(error) == "Only developers and designers can be members of the team."

    @pytest.fixture()
    def test_add_existing_team_member(self):
        manager = Manager("Zdravka", "Valkova", 10000, 10)

        developer = Developer("Ivan", "Petkov", 4000, 2)

        manager.add_team_member(developer)

        try:
            manager.add_team_member(developer)
        except ValueError as error:
            assert str(error) == "The member is already in the team."

    @pytest.fixture()
    def test_remove_team_member_correctly_removes_the_team_member(self):
        manager = Manager("Kiril", "Ivanov", 5000, 4)

        designer = Designer("Dimitrina", "Atanasova", 4000, 3, 1)

        manager.add_team_member(designer)
        assert len(manager.team) == 1

        manager.remove_team_member(designer)
        assert len(manager.team) == 0

    @pytest.fixture()
    def test_remove_team_member_correctly_doesnt_remove_non_existing_team_member(self):
        manager = Manager("Svilen", "Pavlov", 7000, 6)

        developer = Developer("Yana", "Tsvetanova", 4000, 3)
        designer = None

        manager.add_team_member(developer)

        try:
            manager.remove_team_member(designer)
        except ValueError as error:
            assert str(error) == "The member is not in the team."