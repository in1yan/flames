from flask import Flask, request, render_template, redirect, url_for
from flamesFinder.flames import flames
from datetime import datetime
exceptions = [
    "iniyan",
    "vignesh",
    "anees",
    "malar",
    "vinayagam",
    "malar vizhi",
    "malarvizhi",
    "sanjitha",
    "sangitha",
    "sanjeetha"
]
def check_uni(string):
    for x in string:
        if ord(x)>= 97 and ord(x)<=122:
            pass
        elif ord(x) == 32:
            pass
        else:
            return False
            break
    return True
    
def flamer(first_name, second_name):
        url = f"{request.host_url}s={first_name}/{second_name}"
        if first_name == "admin" and second_name == "pass":
            return redirect("/admin")

        elif first_name == "pass" and second_name == "admin":
            return redirect("/pass")
        elif first_name == second_name:
            status ="" 

        else:
            status = flames(first_name,second_name).split(" ")
            emoji = status[1]
            if first_name not in exceptions and second_name not in exceptions and check_uni(first_name) and check_uni(second_name):
                pass
            else:
                status[0] = "Sorry!"
                emoji = ""
            return render_template(
                "result.html",
                status=status[0],
                emoji=emoji,
                first_name=first_name,
                second_name=second_name,
                url=url,
            )

