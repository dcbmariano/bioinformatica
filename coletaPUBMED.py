from bs4 import BeautifulSoup
import requests

# #pega a lista de genes
with open('genes_id.csv') as lista_genes:
	genes = lista_genes.read().split("\n")

i = 0

for g in genes:
	i+=1
	print(i)
	
	id = g

	# Site que será coletado
	site = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&rettype=fasta&id="+id

	# Coleta os dados do site
	html = requests.get(site)
	#print(html.text)

	w = open('fasta/'+id+'.fasta','w')
	w.write(html.text)
	w.close()



# uniprot_gene = {}

# for g in genes:
# 	uniprot_gene[g] = ''


# with open('todos.csv') as tradutor:
# 	linhas = tradutor.readlines()
# 	tamanho = len(linhas)
# 	for linha in linhas:

# 		i += 1
# 		if i%1000000==0:
# 			print(str(int(i/1000)),'/',str(int(tamanho/1000)))

# 		linha = linha.strip().replace("\n","")
# 		celula = linha.split('\t')

# 		ncbi = celula[0]
# 		uniprot = celula[1]

# 		if ncbi in genes:
# 			uniprot_gene[ncbi] = uniprot

# 		# if i > 100:

# w = open('saida.tsv','w')
# for i in uniprot_gene:
# 	w.write(i + '\t' + uniprot_gene[i] + "\n")


