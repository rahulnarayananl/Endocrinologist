from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort,jsonify
import os
from google.cloud import firestore
import diabetes


app = Flask(__name__) #creating the Flask class object   
 
@app.route('/login') #decorator drfines the   
def login():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = (r'C:\Users\rahul narayanan\Downloads\online-diabetes-predicto-6655e-firebase-adminsdk-3psrf-7a74ac94ce.json')
    db = firestore.Client()
    ref = db.collection(u'Users').document(u'#name')
    doc=ref.get()
    a=doc.to_dict()
    my_dict = {"B":float(a['Plasma']), "C":float(a['BP']),"D":float(a['Triceps']), "E":float(a['Insulin']), "F": float(a['BMI'])}
    output = diabetes.check_input(my_dict)   
    if output==0:
        #print(output)
        return render_template('false.html')
    else:
        return render_template('true.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/openForm')
def openForm():
    return render_template('form.html')

# @app.route('/index',methods=['POST','GET'])
# def index():
#     return render_template('login.html')
        

# @app.route('/login',methods=['POST','GET'])
# def login():
#     data=request.form.to_dict()
#     print("DAta: ",data)
#     plasma=data['plasma']
#     bp=data['bp']
#     bmi=data['bmi']
#     triceps=data['triceps']
#     insulin=data['insulin']
#     print("data1:",data)
#     res={"status":"0","error":"null"}
#     return jsonify(result=res)
if __name__ =='__main__':  
    app.run(debug = True)  
