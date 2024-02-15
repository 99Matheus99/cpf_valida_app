"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import re


class cpf_valida(toga.App):

    def startup(self):

        # definindo as caixas
        main_box = toga.Box(style=Pack(direction=COLUMN)) # será uma coluna
        name_box = toga.Box(style=Pack(direction=ROW)) # será uma linha

        # definindo os widgets
        cpf_label = toga.Label('Digite o cpf: ', style=Pack(padding=(0,5)))
        self.name_input = toga.TextInput(style=Pack(padding=1)) # utiliza o "self" pois a classe já tem esse método
        
        button = toga.Button('validar', on_press=self.valida_cpf, style=Pack(padding=5)) 


        # adicionando o conteúdo
        name_box.add(cpf_label)
        name_box.add(self.name_input)
        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def valida_cpf(self, widget): # função que valida o cpf (função "handler")
        def validacao ():
            # PRIMEIRO DIGITO VERIFICADOR
            soma = digito1 = 0
            for n in range(0,9):
                soma += int(self.name_input.value[n]) * (10 - n)
            resto = soma % 11
            if(resto < 2):
                digito1 = 0
            else:
                digito1 = 11 - resto

            # SEGUNDO DIGITO VERIFICADOR
            soma = digito2 = 0
            for n in range(0,10):
                soma += int(self.name_input.value[n]) * (11 - n)
            resto = soma % 11
            if(resto < 2):
                digito2 = 0
            else:
                digito2 = 11 - resto

            # PARTE DA ANÁLISE
            if digito1 == int(self.name_input.value[9]) and  digito2 == int(self.name_input.value[10]):
                return True
            else:
                return False
    
        try:
            result = validacao()
        except Exception:
            self.main_window.error_dialog('Erro', 'Entrada inválida')


        if result == True:
            self.main_window.info_dialog('resultado', 'O cpf é válido!')
        else:
            self.main_window.info_dialog('resultado', 'O cpf é inválido!')
def main(): 
    return cpf_valida()
