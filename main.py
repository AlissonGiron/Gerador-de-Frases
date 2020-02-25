import re
import random
import os

allfiles = os.listdir("brown/dataset")

file = open("brown/dataset/" + random.choice(allfiles), "r") 

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
    word = random.sample(words[tipo], 1)[0].strip()
    
    if(word == "``" or word == "\"\"" or word == "''"):
        continue

    if(tipo != "." and tipo != "," and tipo != ":"):
        word = " " + word

    fraseFinal.append(word)

print("".join(i.capitalize() for i in "".join(fraseFinal).strip().split(". ")))