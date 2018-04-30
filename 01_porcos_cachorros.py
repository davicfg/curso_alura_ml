#p == porto e c == cachorro
# [gordinho, tem perna curta, faz som de cachorro]

p1 = [1,1,0]
p2 = [1,1,0]
p3 = [1,1,0]
c1 = [1,1,1]
c2 = [0,1,1]
c3 = [0,1,1]

dados = [p1, p2, p3, c1, c2, c3]

marcacoes = [1, 1, 1, -1, -1, -1]

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]
teste = [misterioso1, misterioso2, misterioso3]
r_esperado = [-1, 1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)


resultado = modelo.predict(teste);

diferencas = resultado - r_esperado
acertos = [d for d in diferencas if d==0]
total_acertos = len(acertos)
total_elementos = len(teste)

taxa_acerto = 100.0 * total_acertos/total_elementos

print(taxa_acerto)

