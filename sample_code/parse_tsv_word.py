#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file use to get Khmer word from tsv and save in other file

import pandas as pd
import numpy as np
from codecs import open
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", type=str, default="",
                    help="File input name", required=True)
parser.add_argument("-o", "--out", type=str, default="",
                    help="File output name", required=True)

args = vars(parser.parse_args())
file_path = args["file"]
output_file_path = args["out"]

words_list = pd.read_csv(file_path, delimiter="\t",
                         encoding="utf-8", header=None)
with open(output_file_path, "w", encoding="utf-8") as f:
  for word in words_list[words_list.columns[0]]:
    f.write(word + "\n")
