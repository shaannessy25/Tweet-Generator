from flask import Flask, render_template, request, redirect, url_for
from sample import main_sample
from histogram import histogram_dict
from markov2 import run_generator
import dictogram
import os

app = Flask(__name__)

@app.route('/')
def index():
    sentence_text = run_generator()
    return render_template('base.html', sentence_text=sentence_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))


