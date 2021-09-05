import model
from flask import Flask, request, render_template,jsonify 


app = Flask(__name__,template_folder="Template")
@app.route('/')
def home():
    return render_template('home.html') 
@app.route('/classify',methods=['POST','GET'])
def classify_type():
    try:
        sepal_len = request.args.get('slen')
        sepal_wid = request.args.get('swid')
        petal_len = request.args.get('plen')
        petal_wid = request.args.get('pwid')
        variety = model.classify(sepal_len, sepal_wid, petal_len, petal_wid)
        return render_template('home.html', variety=variety)
    except:
        return 'Error'
if(__name__=='__main__'):
    app.run(debug=True)