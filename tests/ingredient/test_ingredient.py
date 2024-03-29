from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


def test_ingredient():
    # a classe pode ser instanciada
    mussarela = Ingredient("queijo mussarela")
    assert isinstance(mussarela, Ingredient)

    # "name" é igual ao passado no construtor
    assert mussarela.name == "queijo mussarela"

    # "restrictions" tem valores corretos para o ingrediente do construtor
    restricoes_mussarela = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert mussarela.restrictions == restricoes_mussarela

    # o método mágico __repr__ funciona como esperado
    repr_mussarela = "Ingredient('queijo mussarela')"
    assert repr(mussarela) == repr_mussarela

    # o método mágico __eq__ funciona como esperado
    outra_mussarela = Ingredient("queijo mussarela")
    assert mussarela == outra_mussarela
    assert repr(mussarela) == repr(outra_mussarela)

    farinha = Ingredient("farinha")
    assert mussarela != farinha
    assert repr(mussarela) != repr(farinha)

    # o método mágico __hash__ funciona como esperado
    assert hash(mussarela) == hash("queijo mussarela")
    assert hash(mussarela) == hash(outra_mussarela)
    assert hash(mussarela) != hash(farinha)
