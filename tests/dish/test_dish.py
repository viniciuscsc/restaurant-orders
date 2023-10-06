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
    mussarela = Ingredient("queijo mussarela")

    lasanha.add_ingredient_dependency(massa_lasanha, 500)
    lasanha.add_ingredient_dependency(mussarela, 400)

    massa_ravioli = Ingredient("massa de ravioli")
    carne = Ingredient("carne")

    ravioli.add_ingredient_dependency(massa_ravioli, 300)
    ravioli.add_ingredient_dependency(carne, 200)

    # é possível obter a quantidade de ingrediente adicionado
    assert lasanha.recipe.get(massa_lasanha) == 500
    assert lasanha.recipe.get(mussarela) == 400

    assert ravioli.recipe.get(massa_ravioli) == 300
    assert ravioli.recipe.get(carne) == 200

    # "get_restrictions" retorna um set de restricoes
    restricoes_massa_lasanha = massa_lasanha.restrictions
    restricoes_mussarela = mussarela.restrictions

    restricoes_lasanha = restricoes_massa_lasanha.union(restricoes_mussarela)
    assert lasanha.get_restrictions() == restricoes_lasanha

    restricoes_massa_ravioli = massa_ravioli.restrictions
    restricoes_carne = carne.restrictions

    restricoes_ravioli = restricoes_massa_ravioli.union(restricoes_carne)
    assert ravioli.get_restrictions() == restricoes_ravioli

    # "get_ingredients" retorna um set de ingredientes
    ingredientes_lasanha = {massa_lasanha, mussarela}
    assert lasanha.get_ingredients() == ingredientes_lasanha

    ingredientes_ravioli = {massa_ravioli, carne}
    assert ravioli.get_ingredients() == ingredientes_ravioli
