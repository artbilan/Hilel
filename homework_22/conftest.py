import pytest
from human import Human


@pytest.fixture()
def human():
    human = Human("John", 23, "male")
    yield human



