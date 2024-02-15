# import flask
# #abhi handle the request

from flask import Flask, render_template, redirect,request,url_for
import mysql.connector as sql
app = Flask(__name__)
con = sql.connect(host="sql6.freesqldatabase.com", user="sql6682227", password="3Pbj2MkdEP", database="sql6682227")

# @app.route('/')
# def index():
#     return redirect(url_for("login"))

@app.route('/',methods=["POST","GET"])
def signin():
    if request.method == "POST":
        name = request.form["nm"]
        email = request.form["em"]
        passwd = request.form["passwd"]
        q= "INSERT INTO data(Name,Email,Password) VALUES('{}','{}','{}')".format(name,email,passwd)
        cur=con.cursor()
        cur.execute(q)
        con.commit()
        return render_template("login.html")
    else:
        return render_template("index.html")

@app.route('/login/')
def login():
    emailid = request.args.get('email')
    passw = request.args.get('passwd')
    cur= con.cursor()
    s="SELECT * FROM data WHERE Email='{}' AND Password='{}'".format(emailid,passw)
    cur.execute(s)
    data=cur.fetchall()
    if data:
        return "there is data"
    else:
        return "no data "

# yaha paa problem haa error file ma kya error haa check kar laa
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