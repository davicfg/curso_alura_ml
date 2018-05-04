from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB
X, Y = carregar_acessos()

modelo = MultinomialNB()

modelo.fit(X, Y)

resultado = modelo.predict([[1,0,1],[0,1,0],[1,0,0],[1,1,0],[1,1,1]]))


