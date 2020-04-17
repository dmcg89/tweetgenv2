import sys, random

from flask import Flask, jsonify, render_template
from flask_cors import CORS
# from app import app

from sentence import construct_phrase, dict_of_hists, pickle_ds
from dictogram import Dictogram
from cleanup import iterate_files, get_word_list
import json
app = Flask(__name__, instance_relative_config=True)
CORS(app)

master_dict = pickle_ds()

@app.route('/')
@app.route('/index')
def index():
    song = []
    for _ in range(10):
        song.append(' '.join(construct_phrase(master_dict[0], master_dict[1], random.randint(1,8)*2)))
    # my_json_string = json.dumps(song)

    # return render_template("base.html", title='Home Page',words=song)
    return json.dumps(song)
    # return song


# if __name__ == '__main__':
#     word_list = iterate_files()
#     histogram = Dictogram(word_list)
#     master_dict = dict_of_hists(histogram, word_list)
#     for _ in range(10):
#         sentence(word_list, master_dict, random.randint(1,8)*2)
