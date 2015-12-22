#!/usr/bin/python
import sys
import os
import logging
from corpus_childrenbooks import make_childrenbooks_corpus

def main():
    logging.getLogger().setLevel("INFO")
    cbt_path = sys.argv[1]
    cbt_files = ['data/cbt_train.txt', 'data/cbt_valid.txt', 'data/cbt_test.txt']
    cbt = [make_childrenbooks_corpus(os.path.join(cbt_path, f)) for f in cbt_files]

if __name__ == "__main__":
    main()

