def texto_para_binario(texto):
	''' converte um texto para binario '''
	binario = bin(int.from_bytes(texto.encode('utf-8', 'surrogatepass'), 'big'))[2:]
	return binario.zfill(8 * ((len(binario) + 7) // 8))

def binario_para_texto(binario):
	''' converte um binario em texto '''
	n = int(binario, 2)
	return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', 'surrogatepass') or '\0'

def polimerase(i):
	''' retorna o nucleotídeo correspondente'''
	if i == '00':
		return 'A'
	elif i == '01':
		return 'T'
	elif i == '10':
		return 'C'
	elif i == '11':
		return 'G'
	else:
		exit()

def antipolimerase(i):
	''' Converte dna em binário '''
	if i == 'A':
		return '00'
	elif i == 'T':
		return '01'
	elif i == 'C':
		return '10'
	elif i == 'G':
		return '11'
	else:
		exit()

def binario_para_dna(binario):
	''' converte binario em dna '''
	dna = ''
	for i in range(0, len(binario), 2):
		dna += polimerase(binario[i:i+2])
	return dna

def dna_para_binario(dna):
	''' converte dna em binario '''
	binario = ''
	for i in range(len(dna)):
		binario += antipolimerase(dna[i])
	return binario


# PLÁGIO-BLAST

# PASSO 1: converter texto em binário
t = '''
texto que desejamos buscar o plágio está aqui
'''

b = texto_para_binario(t)
#print(b)

# PASSO 2: converter binário em sequência de DNA
seq = binario_para_dna(b)
print(seq)

# PASSO 3: retorna a sequência para binario
b2 = dna_para_binario(seq)

# PASSO 4: retorna o binário para texto
t2 = binario_para_texto(b2)
print('O texto original é: ', t2)



