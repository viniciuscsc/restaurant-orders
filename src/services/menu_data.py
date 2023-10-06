import csv
from src.models.dish import Dish, Recipe


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes: set = self.obter_menu()

    def obter_menu(self) -> None:
        with open(self.source_path, "r", newline="") as menu_csv:
            menu_dict = csv.DictReader(menu_csv)
            prato_atual: Dish = None
            receita_atual = Recipe()

            for linha in menu_dict:
                prato = linha["dish"]
                preco = linha["price"]
                ingrediente = linha["ingredient"]
                qtd_ingrediente = linha["recipe_amount"]
            
            if prato_atual == None or prato_atual.name != prato:
                prato_atual = Dish(prato, preco)
                self.dishes.add
