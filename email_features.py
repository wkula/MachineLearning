#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List

import numpy as np


def email_features(word_indices: List[int]) -> np.ndarray:
    """Convert a list of word IDs into a feature vector.

    :param word_indices: a list of word IDs
    :return: a feature vector from the word indices (a row vector)
    """

    # Total number of words in the dictionary
    n_words = 1899

    # FIXME: ====================== YOUR CODE HERE ============================
    # Instructions: Fill in this function to return a feature vector for the
    #               given email (word_indices). To help make it easier to 
    #               process the emails, we have have already pre-processed each
    #               email and converted each word in the email into an index in
    #               a fixed dictionary (of 1899 words). The variable
    #               word_indices contains the list of indices of the words
    #               which occur in one email.
    # 
    #               Concretely, if an email has the text:
    #
    #                  The quick brown fox jumped over the lazy dog.
    #
    #               Then, the word_indices vector for this text might look 
    #               like:
    #               
    #                   60  100   33   44   10     53  60  58   5
    #
    #               where, we have mapped each word onto a number, for example:
    #
    #                   the   -- 60
    #                   quick -- 100
    #                   ...
    #
    #              (note: the above numbers are just an example and are not the
    #               actual mappings).
    #
    #              Your task is take one such word_indices vector and construct
    #              a binary feature vector that indicates whether a particular
    #              word occurs in the email. That is, x(i) = 1 when word i
    #              is present in the email. Concretely, if the word 'the' (say,
    #              index 60) appears in the email, then x(60) = 1. The feature
    #              vector should look like:
    #
    #              x = [ 0 0 0 0 1 0 0 0 ... 0 0 0 0 1 ... 0 0 0 1 0 ..];
    #
    # =========================================================================

    features = np.zeros((n_words,), dtype=int)
    word_indices = set(word_indices)
    for word in word_indices:
        features[word] = 1

    return features

    # =========================== END OF YOUR CODE ============================


if __name__ == '__main__':
    test_indices = [86, 916, 794, 1077, 883, 370, 1699, 790, 1822, 1831, 883, 431,
                    1171, 794, 1002, 1895, 592, 1676, 238, 162, 89, 688, 945, 1663,
                    1120, 1062, 1699, 375, 1162, 479, 1893, 1510, 799, 1182, 1237,
                    810, 1895, 1440, 1547, 181, 1699, 1758, 1896, 688, 1676, 992,
                    961, 1477, 71, 530, 1699, 531]
    out = email_features(test_indices)
    print(out)
    print(len(out))
    print(sum(out))

