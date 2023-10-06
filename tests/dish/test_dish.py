from src.models.dish import Dish  # noqa: F401, E261, E501


def test_dish():
    # a classe pode ser instanciada
    lasanha = Dish("lasanha", 20)
    assert isinstance(lasanha, Dish)

    # "name" é igual ao passado no construtor
    assert lasanha.name == "lasanha"
