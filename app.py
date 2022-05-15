from flask import Flask, session, render_template, request, redirect, g, url_for
from flask_cors import CORS
import controllers.front_controller as fc
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

# Establish all routes handled by Flask
fc.route(app)
cors = CORS(app)


if __name__ == '__main__':
    app.run(debug=True)
