from flask import Flask, flash, request, render_template
from flames import flames
app = Flask(__name__)
app.config['SECRET_KEY']="ThisIsMe"
first_name = ""
second_name = ""
@app.route('/', methods = ["GET", "POST"]) 
def index():
    if request.method == "POST":
        first_name = request.form.get("fname") 
        second_name = request.form.get("sname") 
        status = flames(first_name, second_name)
        emoji = status.split(" ")
        status = emoji[0]
        return render_template('result.html',status=status, emoji=emoji[1], first_name=first_name, second_name=second_name) 
    return render_template('index.html')
