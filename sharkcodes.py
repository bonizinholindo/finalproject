#with opoen("agenda.txt", "r", encoding="utf-8")as arquivo:
 #   for linha in arquivo:
  #W      if "Sharkcoders" in linha:
    #        print(linha.rstrip())


def cadastro():
    nome = input("Entre com seu noome: ")
    idade = int(input("Entre com a idade: "))
    with open("Lista.Idades.txt", "a") as file:
        file.write(nome + "\n")
        file.write(str(idade) + "\n")














































































