from flask import Flask,request,render_template
import joblib
from sklearn.tree import DecisionTreeClassifier
from csv import writer
import pandas as pd

# List that we want to add as a new row
List = [6, 'William', 5532, 1, 'UAE']
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def getPredict():
    msg=""
    if request.method == 'POST':
        gender = request.form.get('gender')
        age = request.form.get('age')
        print(f'{gender} ,age:{age}')
        model=joblib.load('our_pridction.joblib')
        predictions= model.predict([[age,gender]])
        msg=predictions[0]
        with open('music.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([age,gender,msg])

    return render_template("predict.html",msg=msg)

@app.route("/fit", methods=['GET'])
def learn():
    music_dt  =pd.read_csv( 'music.csv')
    X=music_dt.drop(columns=['genre']) # sample features ,[Age,Gender]
    Y=music_dt['genre'] # sample output ['genere']
    
    model = DecisionTreeClassifier()
    model.fit(X,Y) # load features and sample data
    joblib.dump(model, 'our_pridction.joblib') #binary file
    msg ="Thank you - now i'm smarter!!!"
    return render_template("smart.html",msg=msg)

@app.route("/real", methods=['GET', 'POST'])
def realgenare():
    msg=""
    if request.method == 'POST':
        gender = request.form.get('gender')
        age = request.form.get('age')
        genare = request.form.get('genare')
        print(f'{gender} ,age:{age}')
        with open('music.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([age,gender,genare])

    return render_template("realgenare.html",msg=msg)


app.run(debug=True)