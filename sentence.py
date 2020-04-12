from dictogram import Dictogram
from cleanup import get_word_list, iterate_files
from sample import weighted_random_select
import pickle, sys, random, os.path
# from string import isspace

def dict_of_tuple_dicts(word_list, markov_order = 2):
  """Constructs a dictionary with words from corpus as keys
  and a histogram of following words as values"""
  master_dict = {}
  # Token to determine start/stop of new phrase.  1 for start, 0
  # for neutral, -1 for stop
  token = 0
  for line in word_list:
    if line.isspace(): continue
    words = line.split()
    # print(words)
    for indx, word in enumerate(words):
      if indx == 0: queue = []
      if indx < markov_order:
        queue.append(word)
        token = 1
      else:
        queue.append(word)
        word_select = queue.pop(0)
        if indx == len(words) - 1:
          print('end token')
          token = -1
        # print(len(queue))
        dict_of_tuple_entry(master_dict, word_select, tuple(queue), token)
        if token == 1: token = 0
        if indx == len(words) - 1:
          print('break')
          break

  return master_dict

def dict_of_tuple_entry(master_dict, word_select, words, token):
  """Constructs a histogram for word_select that counts word tuples
      and is an inner dictionary of master_dict"""
  if word_select in master_dict.keys():
    freq_dict = master_dict[word_select]
    if words in freq_dict.keys():
      count = freq_dict[words][0] + 1
      # sets start/stop token to existing token if not 0, else sets to passed token
      # Attempts to maximize posibilities for start/stop tokens
      new_token = freq_dict[words][1] if freq_dict[words][1] != 0 else token
      freq_dict[words] = (count, token)
    else:
      freq_dict[words] = (1, token)
  else:
    master_dict[word_select] = {}
    master_dict[word_select][words] = (1, token)
  # return master_dict

def construct_phrase(word_list, master_dict, sen_length = 10):
  """Constructs a phrase using markov chain"""
  # Select random word from corpus to begin phrase
  sentence = []
  word_select = word_list[random.randint(0, len(word_list) - 1)]
  # Append word to start phrase construction
  sentence.append(word_select)
  for i in range(sen_length):
    words = weighted_random_select(master_dict.get(word_select))
    [sentence.append(word) for word in words]
    word_select = words[len(words) - 1]
  print(f"sentence: {(' ').join(sentence)}")
  return (' ').join(sentence)
# def new_words(frequency_hist):
#   """Selects a new word, based on the frequency the word follows word_select"""

#   return weighted_random_select(frequency_hist)

def dict_of_hists_entry(select_word, word_list):
    words_after_list = []
    for index in range(len(word_list)-1):
        if select_word == word_list[index]:
            words_after_list.append(word_list[index+1])
    select_word_hist = Dictogram(words_after_list)
    return select_word_hist

def dict_of_hists(histogram, word_list):
    master_dict = {}
    for word in histogram:
        entry = dict_of_hists_entry(word, word_list)
        master_dict[word] = entry
    return master_dict

def pickle_ds(corpus_file='./lyrics', filename = "masterdict.pkl"):
    """Checks if there is an existing master dict, if not, creates one"""
    if os.path.isfile(filename):
        print ("Data scructure pickled, fetching pickle")
        with open(filename, 'rb') as handle:
            master_dict = pickle.load(handle)
        with open('word_list.pkl', 'rb') as f:
            word_list = pickle.load(f)
    elif corpus_file is not None:
        print ("Creating new dictionary")
        word_list = iterate_files(corpus_file)
        master_dict = dict_of_tuple_dicts(word_list)
        with open(filename, 'wb') as handle:
            pickle.dump(master_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('word_list.pkl', 'wb') as f:
           pickle.dump(word_list, f)
    return word_list, master_dict

if __name__ == '__main__':
  # if len(sys.argv) == 2:
  #     # use corpus file as sys.argv if
  #     word_list, master_dict = pickle_ds(sys.argv[1])
  # else:
  #     # testing purposes
  # text = "one fish two fish red fish blue fish \n \
  #         one fish two fish red fish blue fish \n \
  #         one fish two fish red fish blue fish \n \
  #         one fish two fish red fish blue fish \n \
  #         one fish two fish red fish blue fish" 
  # word_list = text.splitlines()
  # master_dict = dict_of_tuple_dicts(word_list)
  # word_list, master_dict = pickle_ds()
  word_list, master_dict = pickle_ds(sys.argv[1])
  print(master_dict)
  # print(construct_phrase(word_list, master_dict))


    # master_dict = pickle_ds()
    # for _ in range(10):
    #     sentence(master_dict[0], master_dict[1], random.randint(1,8)*2)
    # if len(sys.argv) == 3:
    #     sentence(word_list, master_dict, sys.argv[3])
    # else:
    #     sentence(word_list, master_dict)

    # print(master_dict)
