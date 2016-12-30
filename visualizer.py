from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import pickle
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

### You'll need: 
### - language model: language_model.pickle
### - student data: team1words.pickle

def plot_with_labels(low_dim_embs, labels, filename='tsne.png'):
  assert low_dim_embs.shape[0] >= len(labels), "More labels than embeddings"
  plt.figure(figsize=(18, 18))  # in inches
  for i, label in enumerate(labels):
    x, y = low_dim_embs[i, :]
    plt.scatter(x, y)
    plt.annotate(label,
                 xy=(x, y),
                 xytext=(5, 2),
                 textcoords='offset points',
                 ha='right',
                 va='bottom')

  plt.savefig(filename)

# def plot_with_groups(low_dim_embs, labels, filename='tsne.png'):
#   assert low_dim_embs.shape[0] >= len(labels), "More labels than embeddings"
#   plt.figure(figsize=(18, 18))  # in inches
#   for i, label in enumerate(labels):
#     x, y = low_dim_embs[i, :]
#     plt.scatter(x, y)
#     plt.annotate(label,
#                  xy=(x, y),
#                  xytext=(5, 2),
#                  textcoords='offset points',
#                  ha='right',
#                  va='bottom')

#   plt.savefig(filename)

## These are from word2vec
with open('language_model.pickle', 'rb') as f:  language = pickle.load(f)
final_embeddings = language['embedding']
dictionary = language['dictionary']
assert(final_embeddings.shape[0] == len(dictionary))
print('dictionary size: ', len(dictionary))

## Load student data
with open('team1words.pickle', 'rb') as f:  # Python 3: open(..., 'rb')
  data = pickle.load(f)

# words to visualize
words_in_data = [word for (grnum, word) in data]
words_in_data = set(words_in_data)  # unique set
valid_words = [word for word in words_in_data if word in dictionary]
invalid_words = [word for word in words_in_data if word not in dictionary]

print("** words not in dictionary:", valid_words)
print("** words not in dictionary:", invalid_words)

word2group = {word:[] for word in valid_words}
for word in valid_words:
    for (gnum, wordj) in data:
        if word==wordj:
            word2group[word].append(gnum)


words_to_visualize = [word for word in word2group if len(word2group[word])<8]


index = [dictionary[word] for word in words_to_visualize]
labels = words_to_visualize
# labels = [','.join(str(x) for x in word2group[word]) for word in words_to_visualize]

tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000)
low_dim_embs = tsne.fit_transform(final_embeddings[index, :])

# import pdb; pdb.set_trace()
plot_with_labels(low_dim_embs, labels, "dl4design2.png")