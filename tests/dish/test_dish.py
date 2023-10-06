from src.models.dish import Dish  # noqa: F401, E261, E501


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
