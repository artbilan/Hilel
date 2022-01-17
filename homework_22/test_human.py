
def test_name(human):
    assert "John" == human.name


def test_gender(human):
    assert "male" == human.gender


def test_change_name(human):
    assert "Adam" != human.name


def test_def_change_gender(human):
    assert "male" == human.gender

