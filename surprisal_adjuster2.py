import re
def read_file(file):
    with open(file, 'r', encoding='utf-8', newline='') as p:
        tokens = []
        scores = []
        for line in p:
            line = line.replace('\n', '')
            line = line.split('<eos>')[0]
            line = re.sub(r'\s*<bos>\s+', '', line)
            line = re.sub(r'^\s*[0-9\.]+\s+', '', line)
            line = re.sub(r'^\s*', '', line)
            line = line.split('inf')[0]
            if re.match(r'[^0-9]+', line):
                tokens.append(line.split())
            else:
                scores.append(line.split())
    return tokens, scores

def sp_words_with_scores(data):
    """
    Reconstruct words from subword tokens and aggregate their scores per sentence.
    
    The function expects tokenized sentences where words may be split into
    subword pieces (e.g., SentencePiece-style tokens where a leading marker
    indicates the start of a new word). It merges subword tokens back into
    full words and sums the associated scores for all tokens that belong
    to the same word.
    
    Special handling:
    - Tokens starting with "Ôûü" are treated as the beginning of a new word
      (after correcting possible encoding artifacts).
    - Punctuation marks (., !, ?, :, ;) are kept as separate tokens with
      their own scores.
    - Tokens whose score is '-' or non-numeric are skipped.
    - Encoding artifacts such as "├ö├╗├╝" are normalized to "Ôûü".
    
    Args:
        data (tuple[list[list[str]], list[list[str]]]):
            A tuple containing:
            - data[0]: list of sentences, each a list of token strings.
            - data[1]: list of sentences, each a list of token scores
              (as strings) aligned with the tokens.
    
    Returns:
        list[list[tuple[str, float]]]:
            A list of sentences. Each sentence is a list of (word, score)
            tuples where:
            - word (str): the reconstructed word or punctuation symbol.
            - score (float): the sum of scores for all tokens forming that word.
    """
    sentences = []
    punct = {".", ",", "!", "?", ":", ";"}  # punctuation to keep separate

    for sent_tokens, sent_scores in zip(data[0], data[1]):
        words = []
        w = ""
        s = 0.0

        for t, sc in zip(sent_tokens, sent_scores):
            # normalize encoding artifact
            t = t.replace("Ôûü", "▁")
            if sc == '-' or re.match(r'[^0-9]+', sc):
                continue
            else:
                sc = float(sc)

            # if the token is punctuation, finish current word and append punctuation separately
            if t in punct:
                if w:
                    words.append((w, s))
                    w = ""
                    s = 0.0
                words.append((t, sc))
                continue

            # start new word if token starts with ▁
            if t.startswith("▁"):
                if w:
                    words.append((w, s))
                w = t[1:]
                s = sc
            else:
                w += t
                s += sc

        if w:
            words.append((w, s))

        sentences.append(words)

    return sentences

def basic_stats(sentences):
    '''
    Make basic statistics
    ''' 
    types = set()
    tokens = []
    for t in sentences:
        for tt in t:
            types.add(tt[0])
            tokens.append(tt[1])
    return f'Types = {len(types)}, Tokens = {len(tokens)}'
