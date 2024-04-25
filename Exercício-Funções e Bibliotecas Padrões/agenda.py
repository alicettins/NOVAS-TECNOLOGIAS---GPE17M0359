import csv

agenda = {}
lista_dados = ["nome", "telefone", "email", "data de nascimento"]
arquivo_csv = "agenda.csv"

def salva_contato(contato):
    agenda[contato[0]] = contato
    print(f"Contato de {contato[0]} foi salvo com sucesso!")

def altera_contato(nome):
    contato = agenda[nome]
    for i, parametro in enumerate(lista_dados):
        if input(f"Quer alterar o {parametro.capitalize()}? Y ou N.").upper() == 'Y':
            contato[i] = input(f"Qual novo {parametro.capitalize()}: ")
    apaga_contato(nome)
    salva_contato(contato)
    print(f"O contato {nome} foi alterado: {contato}!")

def apaga_contato(nome):
    if nome in agenda:
        contato = agenda.pop(nome)
        print(f"O contato {nome} foi apagado com sucesso!")
        return contato
    else:
        print(f"O contato {nome} não existe na agenda!")

def busca_contato(nome):
    if nome in agenda:
        return agenda[nome]
    else:
        print(f"O contato {nome} não existe na agenda!")

def lista_contatos(contatos):
    print(f"A agenda tem {len(contatos)} contatos")
    for contato in contatos.values():
        print(contato)

def salvar_agenda_csv():
    with open(arquivo_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(lista_dados)  
        for contato in agenda.values():
            writer.writerow(contato)

def carregar_agenda_csv():
    try:
        with open(arquivo_csv, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader) 
            for row in reader:
                contato = row
                agenda[contato[0]] = contato
        print("Agenda carregada com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo de agenda encontrado. Começando com agenda vazia.")

carregar_agenda_csv()

while True:
    ope = int(input("""
        *****************************************************
        **                                                 **
        **                  Agenda Pessoal                 **
        **                                                 **
        **                                                 **
        **                                                 **
        **           1 - Salvar Contato                    **
        **           2 - Alterar Contato                   **
        **           3 - Buscar Contato                    **
        **           4 - Apagar Contato                    **
        **           5 - Listar Contatos                   **
        **                                                 **
        **                                                 **
        **  pressione 0 para sair                          **
        *****************************************************

    """))

    if ope == 1:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        datanasc = input("Data de Nascimento: ")
        salva_contato([nome, telefone, email, datanasc])
    elif ope == 2:
        nome = input("Qual contato quer alterar? ")
        if nome in agenda:
            altera_contato(nome)
        else:
            print(f"O contato {nome} não existe na agenda!")
    elif ope == 3:
        nome = input("Qual contato: ")
        busca_contato(nome)
    elif ope == 4:
        nome = input("Qual contato: ")
        apaga_contato(nome)
    elif ope == 5:
        lista_contatos(agenda)
    elif ope == 0:
        salvar_agenda_csv()
        break
    else:
        print("Operação inválida!")
