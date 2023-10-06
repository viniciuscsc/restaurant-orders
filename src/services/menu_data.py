import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.carregar_dados_menu()

    def carregar_dados_menu(self):
        with open(self.source_path, "r", newline="") as menu_csv:
            leitor_menu = csv.DictReader(menu_csv)

            for linha in leitor_menu:
                nome_prato = linha["dish"]
                preco_prato = float(linha["price"])
                nome_ingrediente = linha["ingredient"]
                quantidade_receita = int(linha["recipe_amount"])

                prato_existente = None
                for prato in self.dishes:
                    if prato.name == nome_prato:
                        prato_existente = prato
                        break

                if prato_existente is None:
                    novo_prato = Dish(nome_prato, preco_prato)
                    self.dishes.add(novo_prato)
                    prato_existente = novo_prato

                ingrediente = Ingredient(nome_ingrediente)
                prato_existente.add_ingredient_dependency(
                    ingrediente, quantidade_receita
                )
