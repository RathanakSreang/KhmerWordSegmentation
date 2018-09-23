#!/usr/bin/python
# -*- coding: utf-8 -*-

import trie
from codecs import open, decode
model = trie.Trie()
model.load_from_pickle("train_data")

# kh_str = "អ្នកចេះនិយាយភាសាខ្មែរទេ?"
kh_str = "ចំណេះ​ដឹង​វិទ្យាសាស្ត្រ​ជា​ចំណុច​គាំទ្រ​ដ៏​សំខាន់​មួយ​ក្នុង​ការ​អភិវឌ្ឍ​សេដ្ឋកិច្ច​សង្គម។ "

words = []
word = ''
for ch in kh_str:
  word += ch

  if model.searchWord(word.strip()):
    words.append(word)
    print(word.strip())
    word = ''
