from collections import Counter
import re

with open("./wiki_han.txt","r") as f:
    test_str = f.read().replace("."," ")
    test_str = re.sub("[^가-힣 ]","",test_str)

t_token = test_str.split()
ngram_count = Counter([])

n_gram = [2, 3, 4, 5]
n_score = [0.2, 0.8, 1.2, 1.5]

#n-gram
def short_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

#score
for gram, score in zip(n_gram, n_score):
    for split_text in t_token:
        res = short_ngrams(split_text, gram)
        for gram_text in res:
            ngram_count["".join(gram_text)] += score

for word, freq in ngram_count.most_common(10):
    print(word, round(freq,4))