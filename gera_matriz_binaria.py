humano = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"

boi = "MVLSAADKGNVKAAWGKVGGHAAEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGAKVAAALTKAVEHLDDLPGALSELSDLHAHKLRVDPVNFKLLSHSLLVTLASHLPSDFTPAVHASLDKFLANVSTVLTSKYR"

chimpanze = "MVHFTAEEKAAVTSLWSKMNVEEAGGEALGRLLVVYPWTQRFFDSFGNLSSPSAILGNPKVKAHGKKVLTSFGDAIKNMDNLKPAFAKLSELHCDKLHVDPENFKLLGNVMVIILATHFGKEFTPEVQAAWQKLVSAVAIALAHKYH"


# PARTE 1- armazena todas as k combinações 
def combinador(k, letras):
  if k == 0:
    return ['']
    
  combinacoes = []
  combinacoes_anteriores = combinador(k - 1, letras)
    
  for letra in letras:
    for combinacao_anterior in combinacoes_anteriores:
      combinacoes.append(letra + combinacao_anterior)

  return combinacoes


# PARTE 2 - cria uma matriz vazia
def cria_matriz_zeros(combinacoes):
  matriz = {}
  for i in combinacoes:
    matriz[i] = 0

  return matriz

# PARTE 3 - preenche a matriz esparsa 
def preenche_matriz_binaria(entrada, matriz):
  n = len(entrada)

  matriz_backup = matriz.copy()

  for i in range(0, n-k+1):
    k_mer = entrada[i:i+k]
    matriz_backup[k_mer] = 1

  return matriz_backup


# dados de entrada
k = 2
combinacoes = combinador(k, "ACDEFGHIKLMNPQRSTVWY")
matriz = cria_matriz_zeros(combinacoes)

# cria as matrizes
matriz_humano = preenche_matriz_binaria(humano, matriz)
matriz_boi = preenche_matriz_binaria(boi, matriz)
matriz_chimpanze = preenche_matriz_binaria(chimpanze, matriz)

# imprimindo as matrizes
#print(matriz_humano)    # {'AA': 1, 'AC': 0, 'AD': 0, 'AE': 0, 'AF': 1, 'AG': 1, [...]
#print(matriz_boi)       # {'AA': 1, 'AC': 0, 'AD': 1, 'AE': 1, 'AF': 0, 'AG': 0, [...]
#print(matriz_chimpanze) # {'AA': 1, 'AC': 0, 'AD': 0, 'AE': 1, 'AF': 1, 'AG': 1, [...]

matrix = []

matrix.append(list(matriz_humano.values()))
matrix.append(list(matriz_boi.values()))
matrix.append(list(matriz_chimpanze.values()))

# print("Linhas:", len(matrix), "\nColunas:", len(matrix[0]))
# Linhas: 3 
# Colunas: 400


# Requirements
import numpy as np
from scipy.linalg import svd
import matplotlib.pyplot as plt

# A = np.array(matrix)
A = matrix

[U, S, V] = svd(A)

print(S.shape, V.shape, U.shape)

# s = S
# s = s*(1/np.sum(s))

# import matplotlib.pyplot as plt
# fig = plt.figure()
# fig.suptitle('Gráfico de POSTO')
# plt.plot(s)
# plt.show()



# somatorio = 0
# total = sum(S)
# posto_ideal_nao_descoberto = True

# for i in range(len(S)):
#   percentual = 100*S[i]/total
#   somatorio += percentual
#   print("Posto: ", i+1, " (", round(percentual), "% do total) => (acumulado de ", round(somatorio), "%)", sep="")

#   if somatorio > 70 and posto_ideal_nao_descoberto:
#     posto_ideal_nao_descoberto = False
#     print("Posto ideal:", i+1)

# exit()

s = S
s = s*(1/np.sum(s))
fig = plt.figure()
fig.suptitle('Gráfico de POSTO')
plt.plot(s)
plt.show()


S_2d = S[0:2]
U_2d = U[0:2, :]

matrix_reduzida = S_2d*U_2d.transpose()
# matrix_reduzida = np.dot(S_2d, U_2d.transpose())

legenda = ['Humano', 'Boi', "Chimpanze"]

fig = plt.figure()
fig.suptitle('Hemoglobinas')


dados = matrix_reduzida.transpose()
x = dados[0]
y = dados[1]

plt.scatter(x, y, s=500)

for i, especie in enumerate(legenda):
  plt.annotate(especie, (x[i], y[i]))


# plt.show()


def distancia(x1,y1,x2,y2):
  return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

dist_h_b = distancia(x[0], y[0], x[1], y[1])
dist_h_c = distancia(x[0], y[0], x[2], y[2])
dist_b_c = distancia(x[1], y[1], x[2], y[2])

print("Humano x boi:", int(dist_h_b))
print("Humano x chimpanze:", int(dist_h_c))
print("boi x chimpanze:", int(dist_b_c))


porco = "SLTKAERTIIGSMWTKISSQADTIGTETLERLFASYPQAKTYFPHFDLNPGSAQLRAHGSKVLAAVGEAVKSIDNVSAALAKLSELHAYVLRVDPVNFKFLSHCLLVTLASHFPADLTAEAHAAWDKFLTIVSGVLTEKYR"
matriz_porco = preenche_matriz_binaria(porco, matriz)
matriz_porco = list(matriz_porco.values())

V_2d = V[0:2, :]

ponto_porco = np.dot(V_2d, matriz_porco)

# Plotando novo item
plt.scatter(ponto_porco[0], ponto_porco[1], s=500)
plt.annotate("Porco", (ponto_porco[0], ponto_porco[1]))
plt.show()

print("Porco x Boi:", int(distancia(ponto_porco[0], ponto_porco[1], x[1], y[1])))





# Testing function "kmer"
# mfkmer = BioSVD.kmer(seqs,3,'a')

# # Testing function "svd"
# [U, S, V] = BioSVD.svd(mfkmer)

# # Testing function "factor"
# s = BioSVD.factor(S,'plot')

# # Testing function "extractFactor"
# mfkmer_3 = BioSVD.extractFactor(S,V,3)