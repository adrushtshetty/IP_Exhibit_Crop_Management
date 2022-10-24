import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
app = Flask(__name__)
model = pickle.load(open('Model.pkl', 'rb'))

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/crop_prediction')
def crop_prediction():
    return render_template("crop_pred.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/shop')
def shop():
    return render_template("shop.html")

@app.route('/seeds')
def seeds():
    return render_template("seeds_shop.html")

@app.route('/seeds1')
def seeds1():
    return render_template("seeds_shop-1.html")

@app.route('/mothbeans')
def moth():
    return render_template("mothbeans.html")

@app.route('/lentil')
def lent():
    return render_template("lentil.html")

@app.route('/blackgram')
def black():
    return render_template("blackgram.html")

@app.route('/pomegranate')
def pomo():
    return render_template("pomegranate.html")

@app.route('/banana')
def ban():
    return render_template("banana.html")

@app.route('/mango')
def man():
    return render_template("mango.html")

@app.route('/grapes')
def grap():
    return render_template("grape.html")

@app.route('/watermelon')
def water():
    return render_template("watermelon.html")

@app.route('/apple')
def apple():
    return render_template("apple.html")

@app.route('/coffee')
def coff():
    return render_template("coffee.html")

@app.route('/coconut')
def coc():
    return render_template("coconut.html")

@app.route('/jute')
def jut():
    return render_template("jute.html")

@app.route('/seeds2')
def seed2():
    return render_template("seeds_shop-2.html")

@app.route('/rice')
def rice():
    return render_template("rice.html")

@app.route('/wheat')
def wheat():
    return render_template("wheat.html")

@app.route('/maize')
def maize():
    return render_template("maize.html")

@app.route('/pigeonpeas')
def pigeonpeas():
    return render_template("pigeonpeas.html")

@app.route('/chickpeas')
def chickpeas():
    return render_template("chickpeas.html")

@app.route('/kidneybeans')
def kidneybeans():
    return render_template("kidenybeans.html")

@app.route('/crop_management')
def manage():
    return render_template("single-news.html")

@app.route('/crop_prediction',methods=['POST'])
def predict():

    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    if prediction[0] == 20:
        output ="Rice"
    elif prediction[0] == 11:
        output ="Maize"
    elif prediction[0] == 3:
        output ="Chickpeas"
    elif prediction[0] == 9:
        output = "Kidneybeans"
    elif prediction[0] == 18:
        output ="Pigeonpeas"
    elif prediction[0] == 13:
        output ="Mothbeans"
    elif prediction[0] == 14:
        output ="Mungbeans"
    elif prediction[0] == 2:
        output ="Blackgram"
    elif prediction[0] == 10:
        output ="Lentil"
    elif prediction[0] == 19:
        output ="Pomegranate"
    elif prediction[0] == 1:
        output ="Bananas"
    elif prediction[0] == 12:
        output ="Mangoes"
    elif prediction[0] == 7:
        output ="Grapes"
    elif prediction[0] == 21:
        output ="Watermelons"
    elif prediction[0] == 15:
        output ="Muskmelons"
    elif prediction[0] == 0:
        output ="Apples"
    elif prediction[0] == 16:
        output ="Oranges"
    elif prediction[0] == 17:
        output ="Papayas"
    elif prediction[0] == 4:
        output ="Coconuts"
    elif prediction[0] == 6:
        output ="Cotton"
    elif prediction[0] == 8:
        output ="Jute"
    elif prediction[0] == 5:
        output ="Coffee"


    return render_template('crop_pred.html', prediction_text='{}'.format(output))

@app.route('/crop_requisites_1')
def bench_1():
    return render_template("bench_1.html")
@app.route('/crop_requisites_2')
def bench_2():
    return render_template("bench_2.html")
@app.route('/crop_requisites_3')
def bench_3():
    return render_template("bench_3.html")
if __name__ == '__main__':
    app.run(debug=True)