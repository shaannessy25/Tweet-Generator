from flask import Flask, render_template, request, redirect, url_for
from sample import main_sample
from histogram import histogram_dict
from pymongo import MongoClient
from bson.objectid import ObjectId
import markov2
import dictogram
import os

app = Flask(__name__)

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/create-lryic-gen')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
lyric = db['lyric']

@app.route('/')
def index():
    """Return Homepage"""
    lyric_list = {
        'lyric' : markov2.run_generator()
    }
    lyric_id = lyric.insert_one(lyric_list).inserted_id
    lyric_text = lyric.find_one({'_id': ObjectId(lyric_id)})['lyric']  
    return render_template('base.html', lyric_id = lyric_id, lyric_text = lyric_text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))





    # sentence_size = 20
    # sentence_list = list()
    # text = 'lyrics.txt'
    # for _ in range(0, sentence_size):
    #     sentence_list.append(main_sample(text))
    # sentence_str = " ".join(sentence_list)
    # return render_template('base.html', sentence=sentence_str)