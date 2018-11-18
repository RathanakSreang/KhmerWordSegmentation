# KhmerWordSegmentation(NLP)

### Problem
Unlike other languages, Khmer Word Segmentation is way more complected. Because the Khmer language does not have any standard rule on how we are using space to separate between each word(space are used for easier reading). Moreover, Khmer word can have different meaning with the order of words when it will form. Khmer word could also be a join of two or more Khmer words together.


Because of uncertain rule of spacing and the complicated structure above, which it is hard to segment Khmer Word.

### Why we build it?


Ref:

- http://www.apsipa.org/proceedings_2014/Data/paper/1406.pdf

- http://niptict.edu.kh/wp-content/uploads/2016/05/Khmer-Word-Segmentation-Using-Conditional-Random-Fields-edit.pdf

- https://github.com/silnrsi/khmerlbdict

### Plan
#### 1.Build web site for:
- word segmentations: user to input string of sentences and submit then it response with list of words in those sentences.
- words checking: user submit sentences then it response with sentences and some suggestion word
- words contribution: allow user input Khmer words with it function(noun, verb,...) then we use it to train our model

<!--
- Fit word into model
- English, other beside khmer words
- Number

- Read word from file
- Remove space from text
- Splite word into charater
- Fit into Trie node.

- It should know Khmer words or not khmer words(English or other ..)
 -->
