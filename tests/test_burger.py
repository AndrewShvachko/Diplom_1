import pytest
from unittest.mock import Mock


class TestBurger:
    
    def test_set_buns(self, burger, bun):
         burger.set_buns(bun)
         assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient):
         burger.add_ingredient(ingredient)
         assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, ready_burger):
         ready_burger.remove_ingredient(0)
         assert len(ready_burger.ingredients) == 0

    def test_remove_wrong_index(self, burger):
          with pytest.raises(IndexError):
               burger.remove_ingredient(0)

    def test_move_ingredient(self, ready_burger):
          ing2 = Mock()
          ready_burger.add_ingredient(ing2)
          first_ing = ready_burger.ingredients[0]
          ready_burger.move_ingredient(0, 1)
          assert ready_burger.ingredients[1] == first_ing

    def test_get_price_no_bun_raises_error(self, burger, ingredient):
         burger.add_ingredient(ingredient)
         with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_no_bun_raises_error(self, burger, ingredient):
         burger.add_ingredient(ingredient)
         with pytest.raises(AttributeError):
              burger.get_receipt()            
    
    def test_get_receipt_shows_bun_name(self, ready_burger, bun, ingredient):     
         receipt = ready_burger.get_receipt()
         expected_receipt = f'(==== {bun.get_name()} ====)\n'\
                           f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n' \
                           f'(==== {bun.get_name()} ====)\n\n' \
                           f'Price: {ready_burger.get_price()}'
         assert receipt == expected_receipt

         
         
    def test_get_receipt_shows_ingredient_name(self, ready_burger, bun, ingredient):
         receipt = ready_burger.get_receipt()         
         expected_receipt = f'(==== {bun.get_name()} ====)\n'\
                           f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n' \
                           f'(==== {bun.get_name()} ====)\n\n' \
                           f'Price: {ready_burger.get_price()}'
         assert receipt == expected_receipt

    def test_get_receipt_no_ingredients(self, burger, bun):
         burger.set_buns(bun)
         receipt = burger.get_receipt()         
         expected_receipt = f'(==== {bun.get_name()} ====)\n'\
                           f'(==== {bun.get_name()} ====)\n\n' \
                           f'Price: {burger.get_price()}'
         assert receipt == expected_receipt

    def test_get_price_with_different_combinations(self, ready_burger, bun, ingredient):
         expected_price = bun.get_price() * 2 + ingredient.get_price()
         assert ready_burger.get_price() == expected_price

    def test_get_receipt_shows_ingredient_type(self, ready_burger, bun, ingredient):
         receipt = ready_burger.get_receipt()         
         expected_receipt = f'(==== {bun.get_name()} ====)\n'\
                           f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n' \
                           f'(==== {bun.get_name()} ====)\n\n' \
                           f'Price: {ready_burger.get_price()}'
         assert receipt == expected_receipt
  