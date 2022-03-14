from flask import Flask, render_template
import sys
def create_app():
    app= Flask(__name__)

    @app.route("/")
    def hello_pybo():
        return render_template("hello.html")
    

    return app
