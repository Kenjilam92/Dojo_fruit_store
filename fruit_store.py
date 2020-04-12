from flask import Flask, render_template, request, redirect
from datetime import datetime
app=Flask(__name__)

@app.route('/')
def  shopping():
    return render_template('shopping.html')
@app.route('/checkout', methods=['POST'])
def checkout():
    time= datetime.now()
    checkouttime=time.strftime("%B %d, %Y %I:%M:%S %p")
    name_html=request.form['name']
    s_id_html=request.form['s_ID']
    Strawberry_html=request.form['Strawberry']
    Raspberry_html=request.form['Raspberry']
    Apple_html=request.form['Apple']
    if Strawberry_html=='': 
        Strawberry_html=0
    if Raspberry_html=='': 
        Raspberry_html=0
    if Apple_html=='': 
        Apple_html=0
    return render_template ('checkout.html',name = name_html,s_id = s_id_html,Strawberry = int(Strawberry_html),Raspberry = int(Raspberry_html),Apple = int(Apple_html),time=checkouttime)
    return render_template('checkout.html')
if __name__=='__main__':
    app.run(debug=True)