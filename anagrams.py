import configparser
import os
import time
from itertools import permutations
from flask import redirect, Flask, request, render_template

app = Flask(__name__, static_url_path='/static')

# # Read a list of English words
# with open("words.txt") as word_file:
#     english_words = set(word.strip().lower() for word in word_file)
MIN_WORD_SIZE = 2
class Node(object):
    def __init__(self, letter='', final=False, depth=0):
        self.letter = letter
        self.final = final
        self.depth = depth
        self.children = {}
    def add(self, letters):
        node = self
        for index, letter in enumerate(letters):
            if letter not in node.children:
                node.children[letter] = Node(letter, index==len(letters)-1, index+1)
            node = node.children[letter]
    def anagram(self, letters):
        tiles = {}
        for letter in letters:
            tiles[letter] = tiles.get(letter, 0) + 1
        min_length = len(letters)
        return self._anagram(tiles, [], self, min_length)
    def _anagram(self, tiles, path, root, min_length):
        if self.final and self.depth >= MIN_WORD_SIZE:
            word = ''.join(path)
            length = len(word.replace(' ', ''))
            if length >= min_length:
                yield word
            path.append(' ')
            for word in root._anagram(tiles, path, root, min_length):
                yield word
            path.pop()
        for letter, node in self.children.items():
            count = tiles.get(letter, 0)
            if count == 0:
                continue
            tiles[letter] = count - 1
            path.append(letter)
            for word in node._anagram(tiles, path, root, min_length):
                yield word
            path.pop()
            tiles[letter] = count

def load_dictionary(path):
    result = Node()
    for line in open(path, 'r'):
        word = line.strip() #.lower()
        result.add(word)
    return result

words = load_dictionary('words.txt')
#words = load_dictionary('sowpods.txt')
#words = load_dictionary('wordsEn.txt')

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
    letters = request.form['text']
    #letters = letters.lower()
    ns_letters = letters.replace(' ', '')
    
    # # new
    # anagram_list = get_anagrams(letters)
    # count = 0
    # for word in anagram_list:
    #     print(word)
    #     if word == ns_letters:
    #         continue
    #     wordlist = word.split()
    #     links = ""
    #     for w in wordlist:
    #         links = links + '<a href= http://www.dictionary.com/browse/' + w + '?s=t>' + w + '</a> &nbsp'

    #     return_list.append({'word': links, 'english':'yes'})
    #     count += 1
    # print('%d results.' % count)
    # duration = str(time.time() - start_time)
    # print("Duration: " + duration)
    # return render_template('index2.j2', files=return_list, anagram=letters)

    #old:
   
    count = 0
    for word in words.anagram(ns_letters):
 #   for word in get_anagrams(ns_letters):
        print(word)
        if word == ns_letters:
            continue
        wordlist = word.split()
        links = ""
        for w in wordlist:
            links = links + '<a href= http://www.dictionary.com/browse/' + w + '?s=t>' + w + '</a> &nbsp'

        return_list.append({'word': links, 'english':'yes'})
        count += 1
    print('%d results.' % count)
    duration = str(time.time() - start_time)
    print("Duration: " + duration)
    return render_template('index2.j2', files=return_list, anagram=letters)




 
def get_anagrams(anagram):
    
    import urllib.request
    from collections import defaultdict
    words_from_file = urllib.request.urlopen('file:///Users/dlalonde/code/demo/words.txt').read().split()
    return_list = []
    anagram = defaultdict(list) # map sorted chars to anagrams
    for word in words_from_file:
        anagram[tuple(sorted(word))].append( word )
 
    count = max(len(ana) for ana in anagram.itervalues())
    for ana in anagram.itervalues():
        if len(ana) >= count:
            print (ana)
            return_list.append(ana)
    return return_list

    # import urllib.request
    # from collections import defaultdict
    # #words = urllib.request.urlopen('http://www.puzzlers.org/pub/wordlists/unixdict.txt').read().split()
    # words_from_file = []
    # for line in open("words.txt", 'r'):
    #     word = line.strip() #.lower()
    #     words_from_file.append(word)
    
    # anagram = defaultdict(list) # map sorted chars to anagrams
    # return_list = []
    # for word in words_from_file:
    #     anagram[tuple(sorted(word))].append( word )   
    #     start_time = time.time()
    #     count = max(len(ana) for ana in anagram.values())
    #     for ana in anagram.values():
    #         if len(ana) >= count:
    #             w = [x.decode() for x in ana]
    #             print (w)
    #             return_list.append(w)
    #     duration = str(time.time() - start_time)
    #     print("Duration with defaultdict: " + duration)
    #     return return_list



    # perms = [''.join(p) for p in permutations(anagram)]
    # perm_dict = {}
    # for i in perms:
    #     if i == anagram:
    #         continue
    #     perm_dict[i] = is_english_word(i)
    # for i in perm_dict:
    #     #print("checking: " + i)
    #     if perm_dict[i]:
    #         link = '<a href= http://www.dictionary.com/browse/' + i + '?s=t>' + i + '</a>'
    #         return_list.append({'word': link, 'english':'yes'})
    #         #print("word found: " + i)
    #     else:

    #         if not request.form.get('dictonly'):
    #             return_list.append({'word': i, 'english':'no'})
    
    # #print(str(return_list))
    # duration = str(time.time() - start_time)
    # print("Duration: " + duration)
    # return render_template('index2.j2', files=return_list)
    # #return render_template('simple.j2', files=return_list)
##########################################

