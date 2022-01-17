

def test_name(human):
    assert human.name == "John"


def test_gender(human):
    assert human.gender == "male"


def test_change_name(human):
    assert human.name == "John"


def test_change_gender(human):
    assert human.gender == "male"


def test_age_int(human):
    assert type(human.age) is int


def test_grow_add_one_point(human):
    assert human.age + 1 == 24


def test_symbol_in_name_is_alpha(human):
    assert True is str(human.name).isalpha()


def test_first_symbol_is_upper(human):
    assert True is str(human.name[0]).isupper()


def test_second_and_other_symbols_is_lower(human):
    assert str(human.name[1:]).islower() is True


def test_name_less_than_255_symbols(human):
    assert len(human.name) < 255


def test_gender_less_than_255_symbols(human):
    assert len(human.gender) <= 6

