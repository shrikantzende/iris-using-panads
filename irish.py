from flask import *
import pandas as pd
app = Flask(__name__)

@app.route('/')
def de():
    return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def dd():
    df=pd.read_csv("Iris.csv")
    da=pd.DataFrame(df)
    setMIN=(df[df.Species=='Iris-setosa'].min())
    setMAX=(df[df.Species=='Iris-setosa'].max())
    verMIN=(df[df.Species=='Iris-versicolor'].min())
    verMAX=(df[df.Species=='Iris-versicolor'].max())
    virMIN = (df[df.Species == 'Iris-virginica'].min())
    virMAX = (df[df.Species == 'Iris-virginica'].max())
    sl=float(request.form.get('sl'))
    sw=float(request.form.get('sw'))
    pl=float(request.form.get('pl'))
    pw=float(request.form.get('pw'))
    if sl>=setMIN[1] and sw<=setMAX[2] and pl>=setMIN[3] and pw<=setMAX[4]:
        return render_template('result.html',a='setosa')
    elif sl>=verMIN[1] and sw<=verMAX[2] and pl>=verMIN[3] and pw<=verMAX[4]:
        return render_template('result.html',a='versicolor')
    elif sl>=virMIN[1] and sw<=virMAX[2] and pl>=virMIN[3] and pw<=virMAX[4]:
        return render_template('result.html',a='virginica')
    return render_template('result.html',sl=sl,sw=sw,pl=pl,pw=pw)

if __name__=="__main__":
    app.run()
