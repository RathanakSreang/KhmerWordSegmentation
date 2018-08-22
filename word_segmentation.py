#!/usr/bin/python
# -*- coding: utf-8 -*-

import trie
from codecs import open, decode
model = trie.Trie()
model.load_from_pickle("train_data")

kh_str = "អ្នកចេះនិយាយភាសាខ្មែរទេ?"

words = []
word = ''
for ch in kh_str:
  word += ch

  if model.searchWord(word.strip()):
    words.append(word)
    print(word.strip())
    word = ''
