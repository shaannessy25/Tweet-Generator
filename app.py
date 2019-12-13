from flask import Flask, render_template, request, redirect, url_for
from sample import main_sample
from histogram import histogram_dict
from pymongo import MongoClient
from bson.objectid import ObjectId
from markov2 import run_generator
import dictogram
import os

app = Flask(__name__)

# host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/sentence-generator')
# client = MongoClient(host=f'{host}?retryWrites=false')
# db = client.get_default_database()
# sentence = db['sentence']

# @app.route('/')
# def index():
#     """Return Homepage"""
#     sentence_list = {
#         'sentence' : run_generator()
#     }
#     sentence_id = sentence.insert_one(sentence_list).inserted_id
#     sentence_text = sentence.find_one({'_id': ObjectId(sentence_id)})['sentence']  
#     return render_template('base.html', sentence_id = sentence_id, sentence_text = sentence_text)


@app.route('/')
def index():
    sentence_text = run_generator()
    return render_template('base.html', sentence_text=sentence_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))





    # sentence_size = 20
    # sentence_list = list()
    # text = 'lyrics.txt'
    # for _ in range(0, sentence_size):
    #     sentence_list.append(main_sample(text))
    # sentence_str = " ".join(sentence_list)
    # return render_template('base.html', sentence=sentence_str)