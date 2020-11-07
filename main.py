from flask import Flask, render_template, redirect, url_for, request
import pymysql
app = Flask(__name__)

connection = pymysql.connect(host="localhost", user="root", password="123", db="signups")



@app.route("/")
def template():
    return render_template("template.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method=="POST":
        print(request.form)
        name = request.form["name"]
        email = request.form["email"]
        curs = connection.cursor()
        curs.execute("INSERT INTO signups(name,email)  VALUES(%s,%s)",(name, email))
        connection.commit()
        return  "Thankyou for signing up!"
    return render_template("signup.html")

@app.route("/users")
def users():
      curs = connection.cursor()
      curs.execute("SELECT * FROM signups")
      values = curs.fetchall()
      return render_template("users.html", values=values)
       
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
    #when it's ready to go, swap debug=True to host="0.0.0.0" to make available for all!

#This is Sufian's example code on making a form that posts 
# from flask import Flask, render_template, request
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return render_template('index.html')
# @app.route('/submit', methods=["POST","GET"])
# def submit():
#     if request.method=="POST":
#         print(request.form)
#         fn = request.form['first']
#         ln = request.form['last']
#         f = request.files['filename']
#         f.save(f.filename)
#         return "File stored in the directory of this python program successfully!"
#     return "Hi there"
# if __name__ == '__main__':
#     app.run(debug=True) 
