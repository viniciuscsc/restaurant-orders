from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_ingredient():
    # a classe pode ser instanciada
    mussarela = Ingredient("queijo mussarela")
    assert isinstance(mussarela, Ingredient)

    # "name" é igual ao passado no construtor
    assert mussarela.name == "queijo mussarela"

    # "restrictions" tem valores corretos para o ingrediente do construtor
    restricoes_mussarela = {"LACTOSE", "ANIMAL_DERIVED"}
    assert mussarela.restrictions == restricoes_mussarela

    # o método mágico __repr__ funcione como esperado
    repr_mussarela = "Ingredient('queijo mussarela')"
    assert repr(mussarela) == repr_mussarela

    #  o método mágico __eq__ funcione como esperado
    outra_mussarela = Ingredient("queijo mussarela")
    assert repr(mussarela) == repr(outra_mussarela)
