lista = [3,54,"gato",23,45]

print(len(lista)) #quantos itens tem dentro de uma lista 
print(lista) #mostrar o que tem dentro da lista 

elemento = lista[2] #tirar a posição da lista

print(elemento)

x = 3
y = 2

elemento1 = lista[3-2] #você pode definir valores em posições de listas e tirar suas posições através de contas 


print(elemento1)

lista2 = [3,4,5,6,"casa",7,[1,2,3,4]] #podemos fazer listas dentros de outras listas, e uma lista dentro de outra lista oculpa só uma posição
print(lista2[4][1]) #assim podemos tirar a posição que esta dentro de uma palavra na lista 

lista3 = [1,2,3,4]
print(1 in lista3) # nesse caso só mostará no programa se o "1" estiver dentro da lista indicada

print(lista + lista2) #irá mostrar os termos dentro das listas somadas

lista4 = [1,2,3,4,5,6]
print(max(lista4)) #tirará o valor máximo da lista
print(max(lista4)) #tirará o valor minimo da lista

print(lista4[0:4]) #pegará a posição onde você verificou

lista5 = [1,2,3,4]

lista5 [0] = "oi"

print(lista5) #assim você pode mudar algo em determinada posição na lista 

