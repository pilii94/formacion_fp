# importación de paquetes
from flask import Flask,render_template,request,url_for


import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/",methods=['POST'])
def predict():
	# Path al dataset
	filename = "merged_comments.csv"
	df= pd.read_csv(filename)
	df_data = df[["CONTENT","CLASS"]]
	# Features y Labels
	df_x = df_data['CONTENT']
	df_y = df_data.CLASS
    # Parte de Machine Learning
	corpus = df_x
	cv = CountVectorizer()
	X = cv.fit_transform(corpus) # Entrenamiento de la transformación del texto
	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, df_y, test_size=0.33, random_state=42)
	# Clasificador Naive Bayes 
	from sklearn.naive_bayes import MultinomialNB
	clf = MultinomialNB()
	clf.fit(X_train,y_train) # Entrenamiento del modelo (podemos guardarlo si queremos reutilizarlo)
	clf.score(X_test,y_test)
	#Uso del modelo guardado ya entrenado
	# ytb_model = open("naivebayes_spam_model.pkl","rb")
	# clf = joblib.load(ytb_model)

	if request.method == 'POST':
		comment = request.form['comment']
		data = [comment]
		vect = cv.transform(data).toarray()
		my_prediction = clf.predict(vect) ##predecimos con el modelo
	return render_template('results.html',prediction = my_prediction,comment = comment)
	


if __name__ == '__main__':
	app.run(host="127.0.0.1",port=8081,debug=True)