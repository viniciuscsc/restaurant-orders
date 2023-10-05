from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_ingredient():
    # a classe pode ser instanciada
    ingrediente = Ingredient("queijo mussarela")
    assert isinstance(ingrediente, Ingredient)
