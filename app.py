from flask import Flask, render_template, redirect, url_for, request
import math
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/answer/<roots>")
def answer(roots):
    return render_template("answer.html",value=roots)


@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        c = float(request.form["c"])
        D = (b*b)-(4*a*c)
        if a == 0:
            ans1 = (-1*c)/b
            answerValue = "This is not a quadratic equation and the value for x is " + str(ans1)
            return redirect(url_for("answer", roots=answerValue))
        elif D >= 0:
            ans1 = ((-1*b)+(math.sqrt(D)))/(2*a)
            ans2 = ((-1*b)-(math.sqrt(D)))/(2*a)
            answerValue = "The roots are " + str(ans1) + " and " + str(ans2)
            return redirect(url_for("answer",roots=answerValue))
        else:
            a1 = (-1 * b) /(2*a)
            a2 = math.sqrt(-1*D) / (2 * a)
            ans1=str(a1) + "+" + str(a2) + "i"
            ans2=str(a1) + "-" + str(a2) + "i"
            answerValue = "The imaginary roots are " + ans1 + " and " + ans2
            return redirect(url_for("answer", roots=answerValue))



if __name__ == "__main__":
    app.run()