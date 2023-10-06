import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.obter_menu(source_path)

    def obter_menu(self, caminho_arquivo):
        menu = set()

        with open(caminho_arquivo, "r") as menu_csv:
            menu_dict = csv.reader(menu_csv)

            for linha in menu_dict:
                prato = linha["dish"]
                preco = float(linha["price"])
                ingrediente = linha["ingredient"]
                qtd_ingrediente = int(linha["recipe_amount"])

                if prato in menu:
                    prato_atual = menu[prato]
                else:
                    prato_atual = Dish(prato, preco)
                    menu[prato] = prato_atual

                ingrediente_atual = Ingredient(ingrediente)

                prato_atual.add_ingredient_dependency(
                    ingrediente_atual, qtd_ingrediente
                )

        return menu
