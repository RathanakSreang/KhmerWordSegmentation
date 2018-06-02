#!/usr/bin/python
# -*- coding: utf-8 -*-

import trie
from codecs import open, decode

model = trie.Trie()
# model.load_from_pickle("data/trained")

input_file_path = "data/sea.txt"
with open(input_file_path, "r") as f:
  words = f.read().split("\n")
print("Training start")
for word in words:
  if not bool(word.strip()):
    continue

  print(word)
  model.insertWord(word)

model.save_to_pickle("train_data")
print("Training completed")
