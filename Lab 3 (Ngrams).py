def compute_ngrams(toks, n = 2):
    """Returns an n-gram dictionary based on the provided list of tokens."""
    ngram_dict = dict() # creating dictionary thats initialized to nothing
    for x in range(0, len(toks) - n + 1):#looping through arrays of words
        if toks[x] not in ngram_dict.keys():
            ngram_dict[toks[x]] = list()
        l = list()
        for y in range(0, n - 1):
            l.append(toks[x + y + 1])
        ngram_dict[toks[x]].append(tuple(l))
    
    return ngram_dict
    
    
import random
print(random.choice(['lions', 'tigers', 'bears']))
print(random.choice(range(100)))
print(random.choice([('really', 'like'), ('like', 'cake')]))


import random
def gen_passage(ngram_dict, length=100):
    passage = []
    randomKey = random.choice(sorted(ngram_dict.keys()))
    newRandomKeysList = []
    passage.append(randomKey)
   
    while len(passage) < length:
        newRandomKeysList = []
        if  randomKey in ngram_dict.keys():
            for tup in ngram_dict[randomKey]:
                newRandomKeysList.append(tup[0])
                if len(tup) > 1:
                    newRandomKeysList.append(tup[1])
        
            randomKey = random.choice(newRandomKeysList)
        else:
            randomKey = random.choice(sorted(ngram_dict.keys()))

        passage.append(randomKey)
    return " ".join(str(x) for x in passage)
    
