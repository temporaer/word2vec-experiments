#!/usr/bin/python

from corpus import Corpus
import logging

def clean_data(s):
    s = s.replace('`', '\'')
    s = s.replace('\'\'', '\'')
    s = de_period(s)
    s = de_quote(s)
    return s

def de_period(inp):
    res = inp
    res = res.replace('p . m .', 'pm')
    res = res.replace('a . m .', 'am')
    res = res.replace('i . e .', 'that is')
    res = res.replace('e . g .', 'for example')
    res = res.replace('mon .', 'monday')
    res = res.replace('tue .', 'tuesday')
    res = res.replace('wed .', 'wednesday')
    res = res.replace('thu .', 'thursday')
    res = res.replace('fri .', 'friday')
    res = res.replace('sat .', 'saturday')
    # res = res.replace('sun.', 'sunday') # not included, ambiguity
    res = res.replace('Jan .', 'January')
    res = res.replace('Feb .', 'February')
    res = res.replace('Mar .', 'March')
    res = res.replace('Apr .', 'April')
    res = res.replace('Jun .', 'June')
    res = res.replace('Jul .', 'July')
    res = res.replace('Aug .', 'August')
    res = res.replace('Sep .', 'September')
    res = res.replace('Oct .', 'October')
    res = res.replace('Nov .', 'November')
    res = res.replace('Dec .', 'December')
    res = res.replace('Mr .', 'Mr')
    res = res.replace('Ms .', 'Ms')
    res = res.replace('Mrs .', 'Mrs')
    res = res.replace('Doc .', 'Doctor')
    return res


def de_quote(inp):
    res = inp
    res = res.replace('ain \'t', 'is not')
    res = res.replace('can \'t', 'can not')
    res = res.replace('won \'t', 'will not')
    res = res.replace('\'ll ', 'will ')
    res = res.replace('n \'t ', 'not ')
    res = res.replace('\'re ', 'are ')
    res = res.replace('\'d ', 'had ')
    res = res.replace('\'ve ', 'have ')
    res = res.replace('\'m ', 'am ')
    res = res.replace('he \'s ', 'he is ')
    res = res.replace('she \'s ', 'she is ')

    res = res.replace('ain\'t', 'is not')
    res = res.replace('can\'t', 'can not')
    res = res.replace('won\'t', 'will not')
    res = res.replace('n\'t ', 'not ')
    res = res.replace('he\'s ', 'he is ')
    res = res.replace('she\'s ', 'she is ')
    return res




def read_data(data_path, max_line = None):

    sentence = set()
    counter = 0
    with open(data_path) as story:
        for line in story.readlines():
            if max_line and counter >= max_line:
                return sentence
            line = line.strip()
            # delete empty sentence and illustration figure sentences
            if line == '':
                continue
            if line.find('-LCB-') != -1:
                continue
            if line.find('-RCB-') != -1:
                continue
            if line.find('-LRB-') != -1:
                continue
            if line.find('-RRB-') != -1:
                continue
            if line.find('-LSB-') != -1:
                continue
            if line.find('-RSB-') != -1:
                continue
            if line.find('.jpg') != -1:
                continue
            if line.find('_BOOK_TITLE_') != -1:
                continue
            if line.find('CHAPTER') != -1:
                continue
            sentence.add(clean_data(line))
            counter += 1
    # got sentences
    return sentence

def make_childrenbooks_corpus(filename):
    logging.info("Processing %s" % filename)
    sentences = read_data(filename, None)
    return Corpus(sentences)

