import sys, string, os

def iterate_files(path = "./lyrics"):
    words = ""
    word_total = []
    
    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            print(f'reading {filename}')
            words = get_word_list(path + '/' + filename)
        word_total.append(words)
    return words

def get_word_list(file_name):
    '''Loads words from a file and cleans text of most special characters'''
    print(file_name)
    text =  open(file_name).read()

    # removes punctuation from text and sets all ensures all characters are lower case
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower()
    words = (text.translate(translator)).split()
    return words

if __name__ == '__main__':
    if len(sys.argv) == 2:
        word_list = iterate_files()
    # else:
        # word_list = get_word_list()
    # print(word_list)
