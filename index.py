import logging
import os
from flask import render_template, Flask
from public.routes import ClientRoutes
from zenaura.server import DevServer

app = Flask(__name__, static_folder="public", template_folder="public")

DEVSERVER = DevServer(app, port=5001, debug=True)

@DEVSERVER.app.route(ClientRoutes.bar.value)
@DEVSERVER.app.route(ClientRoutes.home.value)
@DEVSERVER.app.route(ClientRoutes.line.value)
@DEVSERVER.app.route(ClientRoutes.bubble.value)
@DEVSERVER.app.route(ClientRoutes.dougnut.value)
@DEVSERVER.app.route(ClientRoutes.pie.value)
@DEVSERVER.app.route(ClientRoutes.area.value)
@DEVSERVER.app.route(ClientRoutes.radar.value)
@DEVSERVER.app.route(ClientRoutes.scatter.value)
def root():
    try:
        return render_template("index.html")
    except Exception as e:
        logging.info(f"Error rendering template: {e}")
        return "An error occurred.", 500

if __name__ == "__main__":
    DEVSERVER.run()


