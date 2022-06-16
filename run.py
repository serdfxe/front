from tkinter import TRUE
from flask import Flask, render_template
from config import *

app = Flask(__name__)

@app.route('/<s>', methods=["GET", "POST"])
def main_route(s):
    return render_template("main.html", sidebar_components=sidebar_components, current=s, url_for_sidebar_components=url_for_sidebar_components, content=content[s])

app.debug = True

app.run()