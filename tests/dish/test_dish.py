import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


def test_dish():
    # a classe pode ser instanciada
    lasanha = Dish("lasanha", 25.5)
    outra_lasanha = Dish("lasanha", 25.5)
    ravioli = Dish("ravioli", 20.5)

    assert isinstance(lasanha, Dish)

    # "name" e "price" são iguais ao passado no construtor
    assert lasanha.name == "lasanha"
    assert lasanha.price == 25.5

    assert outra_lasanha.name == "lasanha"
    assert outra_lasanha.price == 25.5

    assert ravioli.name == "ravioli"
    assert ravioli.price == 20.5

    # comparacao entre pratos diferentes
    assert lasanha != ravioli
    assert hash(lasanha) != hash(ravioli)

    # comparacao entre pratos iguais
    assert lasanha == outra_lasanha
    assert hash(lasanha) == hash(outra_lasanha)

    # TypeError para "price" não float
    with pytest.raises(TypeError):
        Dish("lasanha", "25.5")

    # ValueError para "price" negativo
    with pytest.raises(ValueError):
        Dish("lasanha", -25.5)

    # é possivel adicionar ingredientes ao prato
    massa_lasanha = Ingredient("massa de lasanha")
    massa_ravioli = Ingredient("massa de ravioli")

    lasanha.add_ingredient_dependency(massa_lasanha, 500)
    ravioli.add_ingredient_dependency(massa_ravioli, 300)
