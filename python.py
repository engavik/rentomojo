from flask import Flask, render_template, request
import mysql.connector

app = Flask("MyApp")

conn = mysql.connector.connect(
         user='',
         password='',
         host='',
         database='')

cur = conn.cursor()

@app.route("/")
def home():
    query = ("SELECT id, name, email FROM db")
    cur.execute(query)
    list = cur.fetchall()
    return render_template("phonebook_home.html")

@app.route("/new_contact")
def new_friend():
     return render_template("new_contact.html")

@app.route("/new_friend", methods=['POST'])
def submit_new_friend():
    name=request.form.get('name')
    email=request.form.get('email')
    website=request.form.get('website')
    about=request.form.get('about')
    query = "insert into db (name,website,email,about) values ('%s','%s','%s', '%s')" % (name,website,email,about)
    cur.execute(query)
    conn.commit()
    return render_template("new_friend.html")

@app.route("/new_friend", methods=['POST'])
def edit_contact():
    name=request.form.get('name')
    email=request.form.get('email')
    website=request.form.get('website')
    about=request.form.get('about')
    query = "insert into db (name,website,email,about) values ('%s','%s','%s', '%s')" % (name,website,email,about)
    cur.execute(query)
    conn.commit()
    return render_template("edit_contact.html")


if __name__ == "__main__":
    app.run(debug=True)

cur.close()
conn.close()