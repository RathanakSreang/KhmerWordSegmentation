# KhmerWordSegmentation

### Problem
Unlike other languages, Khmer Word Segmentation are way more complected.
Because Khmer language does not have any standard rule on how we are using space to separate between each word(space are use for easier reading). Moreover, Khmer word can have difference meaning with order of words when it will form. Khmer word could also be a join of two or more Khmer words together.


Because of uncertain rule of spacing and the complicated structure above, which it is hard to segment Khmer Word.

### Why we build it?


Ref:

- http://www.apsipa.org/proceedings_2014/Data/paper/1406.pdf

- http://niptict.edu.kh/wp-content/uploads/2016/05/Khmer-Word-Segmentation-Using-Conditional-Random-Fields-edit.pdf

- https://github.com/silnrsi/khmerlbdict

### Plan
- Fit word into model
- English, other beside khmer words
- Number

- Read word from file
- Remove space from text
- Splite word into charater
- Fit into Trie node.
-

### About file and function:

- `parse_tsv_word.py`: read `-f` Tab-separated file and get first coloum then save into file `-o`
