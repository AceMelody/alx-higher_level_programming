#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        ln = 0
        ch1 = "None"
    else:
        ln = len(sentence)
        ch1 = sentence[0]
    return ln, ch1
