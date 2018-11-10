#!/usr/bin/python
# -*- coding: utf-8 -*-

import trie
from codecs import open, decode

class WordSegmentation:
  # init Trie class
  def __init__(self, text):
    self.text = text.decode('utf-8')
    self.model = trie.Trie()
    self.model.load_from_pickle("train_data")
    # self.result = []
    self.result_all = []
    # self.leftover = []
    self.startIndex = 0

  def isNumber(self, ch):
    # number letter
    return ch in "0123456789០១២៣៤៥៦៧៨៩"

  def parseNumber(self, index):
    result = ""
    while (index < len(self.text)):
      ch = self.text[index]
      ch = ch.encode('utf-8')
      if self.isNumber(ch):
        result += self.text[index]
        index += 1
      else:
        return result

    return result
  def isEnglish(self, ch):
    return ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

  def parseEnglish(self, index):
    result = ""
    while (index < len(self.text)):
      ch = self.text[index]
      ch = ch.encode('utf-8')
      if (self.isEnglish(ch) or self.isNumber(ch)):
        result += ch;
        index += 1
      else:
        return result
    return result

  def parseTrie(self, index):
    word = ''
    foundWord = ''

    while (index < len(self.text)):
      ch = self.text[index]
      ch = ch.encode('utf-8')
      word += ch
      if self.model.searchWordPrefix(word):
        if self.model.searchWord(word):
          foundWord = word
      elif self.model.searchWord(word):
        return word
      else:
        return foundWord;

      index += 1

    return ""

  def check_words(self):
    while(self.startIndex < len(self.text)):
      ch = self.text[self.startIndex]
      ch = ch.encode('utf-8')
      word = ''

      if self.isNumber(ch):
        word = self.parseNumber(self.startIndex).encode('utf-8')
      elif self.isEnglish(ch):
        word = self.parseEnglish(self.startIndex).encode('utf-8')
      else:
        word = self.parseTrie(self.startIndex)

      length = len(word.decode('utf-8'))
      if length == 0:
        self.result_all.append(ch.decode('utf-8'))
        self.startIndex += 1
        continue

      result = {}
      if self.model.searchWord(word) or self.isNumber(ch) or self.isEnglish(ch):
        self.result_all.append()
        result["text"] = word.decode('utf-8')
      else:
        result["text"] = word.decode('utf-8')

      self.result_all.append(result)
      self.startIndex += length

    # # write to file
    # with open('result/segment_word.txt', "w", encoding="utf-8") as f:
    #   for word in self.result:
    #     f.write(word + "\n")
    # with open('result/segment_not_word.txt', "w", encoding="utf-8") as f:
    #   for word in self.leftover:
    #     f.write(word + "\n")

  def show(self):
    print('Text: ' + self.text)
    print('After check : [' + ', '.join(self.result_all) + ']')


# kh_text = "អ្នកចេះនិយាយភាសាខ្មែរទេ?"
# kh_text = "ចំណេះ​ដឹង​វិទ្យាសាស្ត្រ​ជា​ចំណុច​គាំទ្រ​ដ៏​សំខាន់​មួយ​ក្នុង​ការ​អភិវឌ្ឍ​សេដ្ឋកិច្ច​សង្គម។ "
# kh_text = "ដឹង​វិទ្យាសាស្ត្រ​ជា​ចំណុច​គាំទ្រ​ដ៏​សំខាន់​មួយ​ក្នុង​ការ​អភិវឌ្ឍ​សេដ្ឋកិច្ច​សង្គម។"
# kh_text = "កំពុងលុបការឃោសនារបស់ពួកជ្រុលនិយមលឿនជាងបច្ចុប្បន្ន បើមិនដូច្នេះទេ"
# kh_text = "សហភាពអឺរ៉ុបបានផ្ដល់ពេល៣ខែឲ្"
kh_text = "ខាងក្រុមហ៊ុនរបស់យើងខ្ញុំត្រូវការជ្រើសរើសនិសិ្សតកម្ពុជាយើងដែលកំពុងរៀនផ្នែកពត័មានវិទ្យានិងផ្នែកទូរគមនាគមន៍"

word_segment = WordSegmentation(kh_text)
word_segment.check_words()
word_segment.show()
