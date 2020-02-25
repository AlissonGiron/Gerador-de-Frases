import re
import random

file = open("brown/dataset/cj57","r") 

frases = []
tiposFrase = []
words = {}

lineValue = ""

for line in file:
    line = line.strip()

    if(line == ""):
        if(lineValue != ""):
            frases.append(lineValue)
            lineValue = ""
    else:
        lineValue += " " + line


for frase in frases:
    tipos = re.findall("\/([^ ]+)", frase)
    tiposFrase.append(tipos)

    for tipo in tipos:
        if tipo not in words.keys():
            words[tipo] = set()
        
        searchString = "([^ ]+)\/" + re.escape(tipo)
        words[tipo].update(re.findall(searchString, frase))

tipoFraseSelection =  random.choice(tiposFrase)

fraseFinal = []

for tipo in tipoFraseSelection:
    fraseFinal.append(random.sample(words[tipo], 1)[0])

print(" ".join(fraseFinal))