from nltk.tokenize import sent_tokenize
def read_file(file):
    with open(file, 'r', encoding='utf-8', newline='') as p:
        text = p.read()
        sentences = sent_tokenize(text)
    return sentences
