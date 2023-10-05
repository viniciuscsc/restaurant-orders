from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_ingredient():
    # a classe pode ser instanciada
    ingrediente = Ingredient("queijo mussarela")
    assert isinstance(ingrediente, Ingredient)

    # "name" é igual ao passado no construtor
    assert ingrediente.name == "queijo mussarela"

    # "restrictions" tem valores corretos para o ingrediente do construtor
    restricoes = {"LACTOSE", "ANIMAL_DERIVED"}
    assert ingrediente.restrictions == restricoes
