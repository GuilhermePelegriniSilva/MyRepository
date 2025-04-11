import re
def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    wal=float(input("Entre o tamanho médio de palavra:"))
    ttr=float(input("Entre a relação Type-Token:"))
    hlr=float(input("Entre a Razão Hapax Legomana:"))
    sal=float(input("Entre o tamanho médio de sentença:"))
    sac=float(input("Entre a complexidade média da sentença:"))
    pal=float(input("Entre o tamanho médio de frase:"))
    return [wal,ttr,hlr,sal,sac,pal]
def le_textos():
    textos=[];i=1
    while True:
        texto=input(f"Digite o texto {i} (aperte enter para sair):")
        if texto=="":break
        textos.append(texto);i+=1
    return textos
def separa_sentencas(texto):
    sentencas=re.split(r'[.!?]+',texto)
    if sentencas[-1]=='':del sentencas[-1]
    return sentencas
def separa_frases(sentenca):
    return re.split(r'[,:;]+',sentenca)
def separa_palavras(frase):
    return frase.split()
def calcula_tamanho_medio_palavra(palavras):
    return sum(len(palavra)for palavra in palavras)/len(palavras)
def calcula_type_token(palavras):
    return len(set(palavras))/len(palavras)
def calcula_hapax_legomana(palavras):
    frequencia={palavra:palavras.count(palavra)for palavra in palavras}
    palavras_unicas=sum(1 for palavra in frequencia if frequencia[palavra]==1)
    return palavras_unicas/len(palavras)
def calcula_tamanho_medio_sentenca(sentencas):
    return sum(len(sentenca)for sentenca in sentencas)/len(sentencas)
def calcula_complexidade_sentenca(sentencas):
    return sum(len(separa_frases(sentenca))for sentenca in sentencas)/len(sentencas)
def calcula_tamanho_medio_frase(sentencas):
    frases=[frase for sentenca in sentencas for frase in separa_frases(sentenca)]
    return sum(len(frase)for frase in frases)/len(frases)
def calcula_assinatura(texto):
    sentencas=separa_sentencas(texto)
    frases=[frase for sentenca in sentencas for frase in separa_frases(sentenca)]
    palavras=[palavra for frase in frases for palavra in separa_palavras(frase)]
    wal=calcula_tamanho_medio_palavra(palavras)
    ttr=calcula_type_token(palavras)
    hlr=calcula_hapax_legomana(palavras)
    sal=calcula_tamanho_medio_sentenca(sentencas)
    sac=calcula_complexidade_sentenca(sentencas)
    pal=calcula_tamanho_medio_frase(sentencas)
    return [wal,ttr,hlr,sal,sac,pal]
def compara_assinatura(as_a,as_b):
    return sum(abs(as_a[i]-as_b[i])for i in range(6))/6
def avalia_textos(textos,ass_cp):
    assinaturas=[calcula_assinatura(texto)for texto in textos]
    similaridades=[compara_assinatura(assinatura,ass_cp)for assinatura in assinaturas]
    return similaridades.index(min(similaridades))+1
assinatura=le_assinatura()
textos=le_textos()
print(f"O autor do texto {avalia_textos(textos,assinatura)} está infectado com COH-PIAH.")