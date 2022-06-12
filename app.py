from flask import flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = flask(__name__)

@app.route('/')
def main():
    return render_template('formfilling.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['dur']
    data2 = request.form['def']
    data3 = request.form['rew']
    data4 = request.form['tot']
    data5 = request.form['age']
    data6 = request.form['mal']
    arr = np.array({[data1, data2, data3, data4, data5, data6]})
    pred = model.predict(arr)
    return render_template('after.html', data = pred)

if __name__ == "__main__":
    app.run(debug=True)