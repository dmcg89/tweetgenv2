import sys, random

from flask import Flask, jsonify, render_template
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

from sentence import sentence, dict_of_hists, pickle_ds
from dictogram import Dictogram
from cleanup import iterate_files, get_word_list

app = Flask(__name__)
api = Api(app, version='1.0', title='Country Song Generator',
         description='Generate new songs using a Markov Chain!',
         )


ns = api.namespace('Song Generator', description='Methods')

master_dict = pickle_ds()

@api.route('/index')
class index(Resource):
    def get(self):
        song = []
        for _ in range(10):
            song.append(' '.join(sentence(master_dict[0], master_dict[1], random.randint(1,8)*2)))
    
        return render_template("base.html", title='Home Page',words=song)

if __name__ == '__main__':
    app.run(debug=True)

