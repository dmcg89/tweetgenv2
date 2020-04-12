import sys, random

from flask import Flask, jsonify, render_template
# from app import app

from sentence import sentence, dict_of_hists, pickle_ds
from dictogram import Dictogram
from cleanup import iterate_files, get_word_list
app = Flask(__name__, instance_relative_config=True)

master_dict = pickle_ds()

@app.route('/')
@app.route('/index')
def index():

    # for _ in range(10):
    #     sentence(master_dict[0], master_dict[1], random.randint(1,8)*2)
    song = []
    for _ in range(10):
        # phrase = sentence(word_list, master_dict, random.randint(1,8)*2)
        # song += ' '.join(phrase) + '\n'
        song.append(' '.join(sentence(master_dict[0], master_dict[1], random.randint(1,8)*2)))
    # word_file = 'text2.txt'
    # text =  open(word_file).read()
    # translator = str.maketrans('', '', string.punctuation)
    # text = text.lower()
    # words_from_text = (text.translate(translator)).split()
    # # sorts words alphabetically
    # words_from_text = sorted(words_from_text)
    # hist = histogram(words_from_text)
    # sentence = []
    # for i in range(10):
    #     select_word = weighted_random_select(hist, words_from_text)
    #     sentence.append(select_word)
    # print(sentence)
    # words = " ".join(sentence)
    # print(song)

    return render_template("base.html", title='Home Page',words=song)


# if __name__ == '__main__':
#     word_list = iterate_files()
#     histogram = Dictogram(word_list)
#     master_dict = dict_of_hists(histogram, word_list)
#     for _ in range(10):
#         sentence(word_list, master_dict, random.randint(1,8)*2)
