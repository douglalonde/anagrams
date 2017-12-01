import configparser
import os
import time
from itertools import permutations
from flask import redirect, Flask, request, render_template

app = Flask(__name__, static_url_path='/static')

# Read a list of English words
with open("words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

# Check if a string is a word
def is_english_word(word):
    return word.lower() in english_words

@app.route('/')
def index():
    return_list = []
    return render_template('index2.j2', files=return_list)
    
@app.route('/', methods=['POST'])
def my_form_post():
    start_time = time.time()
    return_list = []
    anagram = request.form['text']
    perms = [''.join(p) for p in permutations(anagram)]
    perm_dict = {}
    for i in perms:
        if i == anagram:
            continue
        perm_dict[i] = is_english_word(i)
    for i in perm_dict:
        #print("checking: " + i)
        if perm_dict[i]:
            link = '<a href= http://www.dictionary.com/browse/' + i + '?s=t>' + i + '</a>'
            return_list.append({'word': link, 'english':'yes'})
            #print("word found: " + i)
        else:

            if not request.form.get('dictonly'):
                return_list.append({'word': i, 'english':'no'})
    
    #print(str(return_list))
    duration = str(time.time() - start_time)
    print("Duration: " + duration)
    return render_template('index2.j2', files=return_list)
    #return render_template('simple.j2', files=return_list)


