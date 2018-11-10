#!/usr/bin/python
# -*- coding: utf-8 -*-

import trie
from codecs import open, decode
model = trie.Trie()
model.load_from_pickle("train_data")

# print(model.searchWord('')) # should False
# print(model.searchWord('គ្រុយ')) # should be True
# print(model.searchWord('គ្រុ')) # should be False
# print(model.searchWordPrefix('គ្រុ')) # should be True
print(model.searchWordPrefix('សួ')) # should be False
