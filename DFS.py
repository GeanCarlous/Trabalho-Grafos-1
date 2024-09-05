def loadlista(filename='GD.txt'):
    global lista_adj, N
    lista_adj = []
    N = 0
    
    with open(filename, 'r') as arquivo:
        lista = arquivo.readlines() # ler todas as linhas e salva em
   
    if len(lista) < 2:
        print("Erro o arquivo tem que ter no mínimo 2 linhas!")

    for i in range(len(lista)):
        linha = lista[i].split()
        if i == 0:
            N = int(linha[0])
            num_arestas = int(linha[1])
            lista_adj = [[] for _ in range(N)]
            Ori = linha[2]
        else:        
            if Ori == "D":
                lista_adj[int(linha[0])-1].append(int(linha[1])-1)
            
            elif Ori == "N":
                lista_adj[int(linha[0])-1].append(int(linha[1])-1)
                lista_adj[int(linha[1])-1].append(int(linha[0])-1)
            
            else:
                print("Formato da orientação está errado!")
                break
    
    #print(lista_adj)
            
#variaveis globais
lista_adj = []
N = 0
mark = 0
cor = []
d = []
f = []


#PARTE DO DFSSSSSSSSSSSSSS TEORIA


# def DFS_VISIT(u: int, lista_adj: list):
#     global mark, cor, d, f
#     cor[u] = "CINZA"
#     mark = mark + 1
#     d[u] = mark
#     for v in lista_adj[u]:
#         if cor[v] == "BRANCO":
#             DFS_VISIT(v, lista_adj)
#     #Quando sai do for, significa que todos os vértices foram visitados, então pinta de preto e marca.
#     cor[u] = "PRETO"
#     mark = mark +1
#     f[u] = mark

def DFS_VISIT_PILHA(u: int):
    global mark, cor, d, f
    
    pilha = [u] #inicia a pilha com o nó inicial
    visitados = set()
    
    while pilha:
        u = pilha [-1]
        
        #um if pra verificar se está branco e deixar cinza
        if cor[u] == "BRANCO":
            cor[u] = "CINZA"
            mark += 1
            d[u] = mark
            visitados.add(u)
        
        #verifica e explora os vizinhos n visitados
        adj_br = [v for v in lista_adj[u] if cor[v] == "BRANCO"]
        
        if adj_br:
            for v in adj_br:
                pilha.append(v)
        else:
            cor[u] = "PRETO"
            mark += 1
            f[u] = mark
            #como esta preto retira do topo da pilha e ajusta
            pilha.pop()
            while pilha and cor[pilha[-1]] == "PRETO":
                pilha.pop()
            
def DFS():
    global mark, cor, d, f
    
    cor = ["BRANCO"]*N
    d = [0]*N
    f = [0]*N
    
    graus = [len(adj) for adj in lista_adj]
    vertices = list(range(N))
    vertices.sort(key=lambda x: graus[x], reverse=True)
    mark = 0
    
    for u in vertices:
        if cor[u] == "BRANCO":
            DFS_VISIT_PILHA(u)
#carrega a lista de adacencia
loadlista()

if lista_adj and N:
    #exec pelo vertice de maior grau
    DFS()
    print("Tempo que ficou cinza(d):",d)
    print("-------------------------------------------")
    print("Tempo que ficou preto(f):",f)