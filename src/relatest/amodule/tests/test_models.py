from ..models import MyModel
from datetime import datetime, UTC


def test_mymodel():
    mymodel = MyModel("Steven", 53)
    assert mymodel.name == "Steven"
    assert mymodel.age == 53
    year = datetime.now(UTC).year - mymodel.age
    assert str(mymodel) == f"Steven ({year})"
