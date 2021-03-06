from flask import Flask, request, render_template
import test

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def home():
    summ = request.form.get("summoner")
    s = []
    for i in range(1,24):
        s.append(request.form.get("select" + str(i)))
    if (summ is None):
        return render_template("home.html")
    else:
        d = test.getSummonerData(summ)
        l = len(d["champions"])
        every = test.getall()
        return render_template("summonerdata.html",d=d,l=l,summ=summ,names=every,s=s)

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5000)
