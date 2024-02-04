# import flask
# #abhi handle the request

from flask import Flask, render_template, redirect,request,url_for
import mysql.connector as sql
app = Flask(__name__)
con=sql.connect(host="localhost",port=3310,user="root",passwd="",database="test")

# @app.route('/')
# def index():
#     return redirect(url_for("login"))

@app.route('/',methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        q= "INSERT INTO nice VALUES('{}')".format(user)
        cur=con.cursor()
        cur.execute(q)
        con.commit()
        return render_template("test.html")
    else:
        return render_template("index.html")

# kadia : problem troubleshoot compleated.
#use static path fot @app.route to prevent errors and pass usrname data to function coressponding to it
# @app.route("/<usr>")
# def user(usr):
#     q="INSERT INTO nice VALUES('{}')".format(usr)
#     #return q
#     cur=con.cursor()
#     cur.execute(q)
#     con.commit()
    #return f"<h1>{usr}</h1>"

if __name__=='main':
    app.run()
