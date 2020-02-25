# Gerador de Frases
 Linguagens Formais e Autômatos


Tarefa da aula de laboratório com objetivo de gerar frases com algum sentido em Inglês.

Foi criado um script em python que analisa e gera frases baseadas no dataset de palavras BROWN CORPUS https://en.wikipedia.org/wiki/Brown_Corpus

BROWN CORPUS é uma coleção de 500 frases e aproximadamente 1 milhão de palavras da lingua inglesa retiradas de livros escritos em 1961. Foi realizada uma análise pelos autores desse documento em cada uma das palavras e tags especificas foram criadas para descrevê-las, a lista completa de tags e seus significados pode ser encontrada em https://web.archive.org/web/20080706074336/http://www.scs.leeds.ac.uk/ccalas/tagsets/brown.html

O algoritmo desenvolvido itera por todas as frases do dataset realizando duas ações:
    - Extrai para um dicionário em memória a listagem de todas as palavras encontradas, agrupadas por suas tags
    - Extrai para uma matriz a sequencia de tags de cada uma das frases existentes

Após isso, o algoritmo escolhe aleatoriamente uma das frases do dataset e copia suas tags, replicando assim sua estrutura gramatical.
Com as tags em mãos, o algoritmo gera uma frase nova com a mesma estrutura gramatical da antiga, mas aplica sobre elas palavras diferentes, escolhidas também de forma aleatória do dicionário mantido em memória.

Em resumo, o algoritmo utiliza as próprias palavras encontradas no documento e suas tags para gerar frases novas em cima de regras gramaticais seguidas por frases reais.