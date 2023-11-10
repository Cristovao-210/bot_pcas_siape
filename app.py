import os

# menu
def menu():
    try:
        print("\nInforme em qual PCA os períodos serão lançados:\n ")
        lista_de_pcas = ['PCA_HISTORICO', 'PCA_ENCERRADO', 'PCA_VIGENTE'] # virá da lista de abas existentes na planilha
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


menu()


    

    