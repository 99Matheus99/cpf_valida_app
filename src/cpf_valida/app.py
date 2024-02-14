"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class cpf_valida(toga.App):

    def startup(self):

        # definindo as caixas
        main_box = toga.Box(style=Pack(direction=COLUMN)) # será uma coluna
        name_box = toga.Box(style=Pack(direction=ROW)) # será uma linha

        # definindo os widgets
        cpf_label = toga.Label('Digite o cpf: ')
        self.name_input = toga.TextInput() # utiliza o "self" pois a classe já tem esse método
        
        button = toga.Button('validar', on_press=self.valida_cpf) 


        # adicionando o conteúdo
        name_box.add(cpf_label)
        name_box.add(self.name_input)
        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def valida_cpf(self, widget): # função que valida o cpf (função "handler")
        print(f'vc digitou {self.name_input.value}')

def main(): 
    return cpf_valida()
