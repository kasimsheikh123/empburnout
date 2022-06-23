from flask import Flask,render_template,request
import pickle
import numpy as np
model = pickle.load(open('./static/Burnout.pkl','rb'))

app= Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    data1 = float(request.form['a'])
    data2 = float(request.form['b'])
    data3 = float(request.form['c'])
    data4 = float(request.form['d'])
    data5 = float(request.form['e'])
    data6 = float(request.form['f'])
    features = np.array([data1,data2,data3,data4,data5,data6])
    pred = model.predict([features])[0]
    pred = round(pred,4)*100

    def statement():
        if pred <= 0:
            return 0
        return pred



    return render_template('index.html',statement = statement())
if __name__=='__main__':
    app.run()
