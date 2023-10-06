import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.obter_menu()

    def obter_menu(self):
        with open(self.source_path, "r", newline="") as menu_csv:
            menu_dict = csv.DictReader(menu_csv)

            for linha in menu_dict:
                prato = linha["dish"]
                preco = float(linha["price"])
                ingrediente = linha["ingredient"]
                qtd_ingrediente = int(linha["recipe_amount"])

                if prato not in self.dishes:
                    prato_atual = Dish(prato, preco)
                    self.dishes[prato] = prato_atual
                    self.dishes.add(prato_atual)
                else:
                    prato_atual = self.dishes[prato]

                ingrediente_atual = Ingredient(ingrediente)
                prato_atual.add_ingredient_dependency(
                    ingrediente_atual, qtd_ingrediente
                )
