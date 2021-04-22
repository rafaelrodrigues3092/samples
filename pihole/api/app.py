from flask import Flask, redirect, url_for, render_template, request, flash
import os
import json

app = Flask(__name__)

app.secret_key = os.environ.get('APP_SECRET_KEY')
PORT = int(os.environ.get('PORT', 5000))

@app.route('/', methods=['GET'])
def index():
    #return redirect(url_for('new_checkout'))
    return json.dumps({'Message':'Hello World'})


@app.route('/checkouts/new', methods=['GET'])
def new_checkout():
    return "Hi World"


@app.route('/pihole/on', methods=['POST'])
def turn_on_pihole():
    return "pihole on"


@app.route('/pihole/off', methods=['POST'])
def turn_off_pihole():
    return "pihole off"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)
