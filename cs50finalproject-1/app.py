import os

from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///monsters.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

#Character into database
@app.route("/characters")
def charbuild():
    if request.method == "POST":
        # Save
        
        charname = request.form.get("charname")
        race = request.form.get("race")
        charclass = request.form.get("class")
        level = request.form.get("level")
        playername = request.form.get("playername")
        ca = request.form.get("ca")
        hp = request.form.get("hp")
        pp = request.form.get("pp")
        str = request.form.get("str")
        dex = request.form.get("dex")
        con = request.form.get("con")
        int = request.form.get("int")
        wis = request.form.get("wis")
        cha = request.form.get("cha")
        character = list((charname, race, charclass, level, playername, ca, hp, pp, str, dex, con, int, wis, cha))
    
        if len(character) != 14:
            message = "Error saving, try again"
            return render_template("charcreation.html", apology=message)
    
        message = "Character saved succesfully"
        save = 1
        #db.execute("INSERT INTO characters(playername, charname, race, class, level, ca, hp, pp, str, dex, con, int, wis, cha) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", playername, charname, race, charclass, level, ca, hp, pp, str, dex, con, int, wis, cha)
        if save != None: 
            return render_template("load.html", message=message)
        #auto-load created character   
        apology = "Unsupported format"
        return render_template("charcreation.html", apology=apology)
    else:
        message = "Let's create a character"
        return render_template("charcreation.html", message=message)

#TO DO
@app.route("/monsterindex")
def monsterindex():
    if request.method == "POST":
        s

    else:
        return render_template("monstertable.html")

#TO DO
@app.route("/statblocks")
def statblocks():
    return render_template("statblocks.html")


#TO DO
@app.route("/about")
def about():
    return render_template("about.html")

#TO DO
@app.route("/load")
def load():
    if request.method == "POST":
        return render_template("load.html")

    else:
        return render_template("load.html")
