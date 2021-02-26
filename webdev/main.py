from flask import Flask,render_template,url_for,request,redirect,session
from datetime import timedelta
import Content

mydata=Content.content()
app=Flask(__name__)
app.secret_key="helo"
app.permanent_session_lifetime=timedelta(days=5)
@app.route("/")
def home():
        return render_template("home.html")
@app.route("/dashbord")
def dashbord():
        return render_template("dashbord.html" ,mydata=mydata,)


if __name__=="__main__":
        app.run(debug=True)


