#import the necesssary dependencies

from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
import pickle


# initializing a flask app
app = Flask(__name__)

#route to display homepage

@app.route('/',method=['GEt'])
@cross_origin()
def homepage():
    return render_template(index.html)

# route to show the prediction in web UI

@app.route('/predict',method=['POST','GET'])
@cross_origin()
def index():
    if request.method =='POST':
        try:
            CRIM = int(request.form['CRIM'])
            ZN = int(request.form['ZN'])
            INDUS = int(request.form['INDUS'])
            CHAS = int(request.form['CHAS'])
            NOX = int(request.form['NOX'])
            RM = int(request.form['RM'])
            AGE = int(request.form['AGE'])
            DIS = int(request.form['DIS'])
            RAD = int(request.form['RAD'])
            TAX = int(request.form['TAX'])
            PTRATIO = int(request.form['PTRATIO'])
            B =int(request.form['B'])
            LSTAT = int(request.form['LSTAT'])

            filename = 'finalized_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])
            print('prediction is', prediction)
           # showing the prediction results in a UI
           
if __name__=="__main__":
    app.run(debug = True)

