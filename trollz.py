#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 21:11:47 2018

@author: tcake
"""

import pandas as pd
import os
import nltk
import re
import twokenize as tw
import unittest

nltk.data.path.append("/media/t-cake/My Passport/nltk_data/")
stopword_list = nltk.corpus.stopwords.words('english')
stopword_list+["\\xa0","\\n"]

path = os.getcwd()+"/data"
files = os.listdir(path)
test = pd.read_csv(path+"/test.csv")
train = pd.read_csv(path+"/train.csv")
labels = pd.read_csv(path+"/impermium_verification_labels.csv")
sets = pd.read_csv(path+"/impermium_verification_set.csv")


def tokenize(comments):
        """ Tokenizes the incoming comment in the format of a list of strings. Removes the http, @ and other unnecessary things
        """
        PATTERN = r'["!?$&*%@()~#://\|]'
        cleansed = []
        for comment in comments:
            tokenized = tw.tokenize(comment)
            filtered = [word for word in tokenized if re.search(PATTERN,word) == None and word not in stopword_list ]
            cleansed.append(filtered)
                
        return cleansed


class TestClass(unittest.TestCase):
    
    def test_tokenization(self):
        test_string_list = ["The cat has a big hat"]
        tokenized = tokenize(test_string_list)
        
        self.assertEquals(len(tokenized[0]), 4)
        
        
if __name__ == '__main__':
    unittest.main()
    
    comments = labels.Comment.tolist()
  #  print(comments)
    print(tokenize(comments))
