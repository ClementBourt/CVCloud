from flask import Flask
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    cv_url=url_for('static',filename='cv_Bourtguize_Ramel_Clement.pdf')
    return f'<a href = {cv_url}>CV lin</a>'