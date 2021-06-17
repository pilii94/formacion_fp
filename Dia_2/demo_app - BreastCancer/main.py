# importación de paquetes
from flask import Flask,render_template,request


import pandas as pd
import numpy as np


#Importamos librerías
from sklearn.svm import SVC
import pickle



app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/",methods=['POST'])
def predict():
	
    #  Machine Learning
	
	# Cargamos el clasificador
	
	loaded_model = pickle.load(open('svc_brca_model.sav', 'rb'))

	
	#Cogemos los datos proporcionados para predecir
	
	if request.method == 'POST':
		clump_thickness = request.form['clump_thickness']

		cell_size_uniformity = request.form['cell_size_uniformity']

		cell_shape_uniformity = request.form['cell_shape_uniformity']

		marginal_adhesion = request.form['marginal_adhesion']

		epithelial_cell_size = request.form['epithelial_cell_size']

		bare_nuclei = request.form['bare_nuclei']

		bland_chromatin = request.form['bland_chromatin']

		normal_nucleoli = request.form['normal_nucleoli']

		mitoses = request.form['mitoses']
		
		
		data = {'clump_thickness':[clump_thickness], 'cell_size_uniformity':[cell_size_uniformity],'cell_shape_uniformity':[cell_shape_uniformity],'marginal_adhesion':[marginal_adhesion],
		'epithelial_cell_size':[epithelial_cell_size],'bare_nuclei':[bare_nuclei],'bland_chromatin':[bland_chromatin],'normal_nucleoli':[normal_nucleoli],'mitoses':[mitoses]} 
		given_data = pd.DataFrame(data) 
		given_data.apply(pd.to_numeric)

		print(given_data)

		my_prediction = loaded_model.predict(given_data) ##predecimos con el modelo
	return render_template('results.html',prediction = my_prediction)
	


if __name__ == '__main__':
	app.run(host="127.0.0.1",port=8080,debug=True)