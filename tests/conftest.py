import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def burger():
     return Burger()

@pytest.fixture(params=[
    ("краторная булка", 50),
    ("флюоресцентная булка", 100), 
    ("безглютеновая булка", 75)
])
def bun(request):
     bun = Mock()
     bun.get_name.return_value = request.param[0]
     bun.get_price.return_value = request.param[1]
     return bun

@pytest.fixture(params=[
    ("соус spicy", "SAUCE", 90),
    ("соус фирменный", "SAUCE", 50),
    ("грибы", "FILLING", 30),
    ("сыр", "FILLING", 50),
    ("котлета", "FILLING", 100),
    ("салат", "FILLING", 20)
])
def ingredient(request):
     ingredient = Mock()
     ingredient.get_name.return_value = request.param[0]
     ingredient.get_type.return_value = request.param[1]
     ingredient.get_price.return_value = request.param[2]
     return ingredient

@pytest.fixture
def ready_burger(burger, bun, ingredient):
     burger.set_buns(bun)
     burger.add_ingredient(ingredient)
     return burger
