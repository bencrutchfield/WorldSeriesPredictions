import logging
from flask import Flask, request, render_template
import datetime
import decimal
import pymysql
import json
import config
from flask_cors import CORS
import sql

app = Flask(__name__)

CORS(app)

#### ROUTES ####

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/2016')
def stats_16():
    result = sql.player_16()
    return result

@app.route('/2017')
def stats_17():
    result = sql.player_17()
    return result

@app.route('/2018')
def stats_18():
    result = sql.player_18()
    return result

@app.route('/sep')
def stats_sep():
    result = sql.sep()
    return result

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

#### ROUTE ENDS #####

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    #app.run(host='0.0.0.0', port=8080, debug=True, processes=4, threaded=True)
    app.run(threaded=True,debug=True)
    #app.run(host='127.0.0.1', port=8080, debug=True)
## [END app] ##
