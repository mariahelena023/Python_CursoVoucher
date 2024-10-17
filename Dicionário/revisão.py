notas = {}

notas["Nota 1"] = float(input("Insira a primeira nota: "))
notas["Nota 2"] = float(input("Insira a segunda nota: "))
notas["Nota 3"] = float(input("Insira a terceira nota: "))
notas["Nota 4"] = float(input("Insira a quarta nota: "))

media_notas = (notas["Nota 1"] + notas["Nota 2"] + notas["Nota 3"] + notas["Nota 4"]) / 4

print("")
print("---NOTAS E SUAS  MÉDIAS---")
print("")
print(f"Notas dos alunos: {notas}")
print(f"Essa é a média das notas: {media_notas}")

