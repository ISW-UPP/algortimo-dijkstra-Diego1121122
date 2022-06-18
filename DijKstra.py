class Arista:
    def __init__(self, vertice_inicial, vertice_final, peso):
        self.vertice_inicial = vertice_inicial
        self.vertice_final = vertice_final
        self.peso = peso
        
class Camino:
    def __init__(self, ari, peso):
        self.ari = ari
        self.peso = peso

def dijkstra(origen, destino, arista, ari):

    caminos = []
    if(len(ari) != 0):
        for arista in ari:
            camino = Camino([], 0)

            for arista_recorrida in ari:
                if(arista_recorrida.vertice_inicial == origen):
                    camino.ari.append(arista_recorrida)
                    camino.peso = camino.peso + arista_recorrida.peso

                    if(arista_recorrida.vertice_final == destino):
                        caminos.append(camino)
                        break
                    else:
                        origen = arista_recorrida.vertice_final
                        
        menor = caminos[0]
        for camino in caminos:
            if(camino.peso < menor.peso):
                menor = camino

        print("Camino mas corto")
        print(f"Acomulado ->> {menor.peso}")
        print(f"Iteraciones ->> {len(menor.ari)}")

        for arista in menor.ari:
            print(f"{arista.vertice_inicial} -> {arista.vertice_final}")
            print(f"Peso ->> {arista.peso}")

    else:
        print("No hay vertices")

entrada_menu = 1
vertices = []
ari = []
respuesta = input("Quieres Entrar al Menu? ->> (Si/No)")

while respuesta == "Si" :  

    print('''
1.- Insertar nodos
2.- Insertar arista
3.- Mostrar grafo
4.- Mostrar arista
5.- Mostrar nodos
6.- Dijkstra
7.- Salir''')
    entrada_menu = int(input("\n Elige una opcion:  "))

    
    if entrada_menu == 1:
        numero_de_vertices = int(input("Ingresa la cantidad de vertices"))

        for i in range(0, numero_de_vertices):   
            print(f"Vertice ->> {i+1}")
            letra = input("Letra ->>  ")
            vertices.append(letra)

    
    elif entrada_menu == 2:
        verticeUno = input("Vertice inicial:")
        verticeDos = input("Vertice final:")
        peso = int(input("Peso:"))
        ari.append(Arista(verticeUno, verticeDos, peso))
        print("La arista se agrego correctamente")
        
    
    elif entrada_menu == 3:
        for arista in ari:
            print(f"Vertice {arista.vertice_inicial} apunta a vertice {arista.vertice_final}")

    
    elif entrada_menu == 4:
        for arista in ari:
            print(f"{arista.vertice_inicial}  ->  {arista.vertice_final}")

    
    elif entrada_menu == 5:
        print("Vertices:",', '.join(vertices))

    
    elif entrada_menu == 6:
        origen = input("Nodo Origen: ")
        destino = input("Destino: ")   
        dijkstra(origen, destino, arista, ari)

    
    elif entrada_menu == 7:
        print("Adios...")
        break