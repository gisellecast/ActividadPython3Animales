import animales

#menu
#while
#decisiones
#dibujos
#clase

menu = {
    '1': 'Erizo',
    '2': 'Nutria',
    '0': 'Exit',
}

class Animal():
    erizo=0
    nutria=0

    animales_lista = {
        1: animales.erizo,
        2: animales.nutria
    }

    def __init__(self,erizo,nutria):
       self.erizo = erizo
       self.nutria = nutria

    def mostrar_animal(self,op):
        print(self.animales_lista[op])


# Ejecución principal
if __name__ == '__main__':
    for k,i in menu.items():
        print(f'{k}:{i}')


    op = int(input('Elige cuál animal quieres ver: ')) #building function



    while True:
        if op == 0:
            #El usuario quiere dejar de jugar
            print("Adiós, vuelve pronto a jugar")
            break
        elif op == 1:
            #Imprimir animal
            print(animales.erizo)
        elif op == 2:
            print(animales.nutria)
        else:
            #Opción inválida
            print('Opción inválida, vuelve a intentarlo')
            for k,i in menu.items():
                print(f'{k}:{i}')

        op = int(input('Elige cuál animales quieres ver: '))
