#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_len = ()
    if len(sentence) == 0:
        sentence_len = 0, None
    else:
        sentence_len = len(sentence), sentence[0]
    return sentence_len
