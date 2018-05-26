#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file use to read charaters in Khmer word

word = "ស្រែចាម"
ch = "្"
for x in word.decode('utf-8'):
  print(x.encode('utf-8'))

print(word.decode('utf-8')[1].encode('utf-8'))
print(word.decode('utf-8')[1].encode('utf-8') == ch)
