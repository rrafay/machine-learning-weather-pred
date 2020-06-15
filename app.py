import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('weather_prediction_.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET', 'POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 1)
    
    for key, value in request.form.items():
        val = ("{1}".format(key, value))
        
    return render_template('index.html', prediction_text='Temperature for ' + val +' dew points is ' + ' {}°F'.format(output))




if __name__ == "__main__":
    app.run(port= 4455,debug=True) 