import os
import pandas as pd
import pyautogui as pg


def data_siape(dt):
    meses_siape = {
    '01': 'JAN',
    '02': 'FEV',
    '03': 'MAR',
    '04': 'ABR',
    '05': 'MAI',
    '06': 'JUN',
    '07': 'JUL',
    '08': 'AGO',
    '09': 'SET',
    '10': 'OUT',
    '11': 'NOV',
    '12': 'DEZ'
}
    dia = str(dt)[8:10]
    mes = meses_siape.get((str(dt)[5:7]))
    ano = str(dt)[:4]
    data = f'{dia}{mes}{ano}'
    return data

def listar_pcas(planilha):
    plan_pcas = pd.read_excel(planilha, None)
    lista_de_sheets = []
    for aba in plan_pcas.keys():
        lista_de_sheets.append(aba)
    return lista_de_sheets


# menu
def menu(lista_de_pcas):
    try:
        print("\nInforme em qual PCA os períodos serão lançados:\n ")
        #lista_de_pcas = ['PCA_HISTORICO', 'PCA_ENCERRADO', 'PCA_VIGENTE'] # virá da lista de abas existentes na planilha
        for i, pca in enumerate(lista_de_pcas):
            print(f'Opção {i+1} - {pca}')
        opcao = input("\nInforme o número da opção desejada: ")
        posica_lista = '0' if int(opcao) < 1 else (int(opcao) - 1)
        pca_escolhido = lista_de_pcas[posica_lista]

        # listar informações sobre o PCA escolhido para confirmação do usuário:

        # data de inicio e fim do pca
        # número do SEI
        # se é vigente ou não vigente
        # posição que ele se encontra na lista apresentada pelo HOD.
        
        # ***Essas informações serão lançadas na planilha de controle dos PCAS.


        print("\nO PCA escolhido foi: ", pca_escolhido) # colocar um retrono aqui
    except:
        os.system('cls')
        print(f'"{opcao}" Não está na lista de opções, escolha uma opção válida!')
        menu()
