import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes: set = self.obter_menu()

    def obter_menu(self) -> None:
        with open(self.source_path, "r", newline="") as menu_csv:
            menu_dict = csv.DictReader(menu_csv)
            prato_atual: Dish = None

            for linha in menu_dict:
                nome_prato = linha["dish"]
                preco = float(linha["price"])
                nome_ingrediente = linha["ingredient"]
                qtd_ingrediente = int(linha["recipe_amount"])

            if prato_atual is None or prato_atual.name != nome_prato:
                prato_atual = Dish(nome_prato, preco)
                self.dishes.add(prato_atual)

            ingrediente = Ingredient(nome_ingrediente)

            prato_atual.add_ingredient_dependency(ingrediente, qtd_ingrediente)
