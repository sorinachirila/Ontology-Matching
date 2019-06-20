# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:13:17 2019

@author: Sorina
"""

# =============================================================================
# The Edit Distance (Levenshtein Distance) is a measure of similarity between two strings. The
# distance between the source and the target is the minimum number of edit operations (deletions,
# insertions, or substitutions) required to transform the source into the target. The lower the distance,
# the more similar the two strings.
# 
# the Damerau-Levenshtein edit distance: besides
# insertion, deletion, substitution you could have transposition of two adjacent letters.
# More information at: https://www.researchgate.net/publication/268334497_Damerau-Levenshtein_Algorithm_and_Bayes_Theorem_for_Spell_Checker_Optimization

# Results:  Print the distance matrix (D), the backtrace matrix, the minimum edit distance table
# and the alignment table.
# For testing purpose is used location property
# =============================================================================

import numpy as np
import tabulate as tb



#Implement a naive backtrace
def backtrace(B):
    i, j = B.shape[0]-1, B.shape[1]-1
    backtrace_idxs = [(i, j)]
    while (i, j) != (0, 0):
        if B[i,j][1]:
            i, j = i-1, j-1
        elif B[i,j][0]:
                i, j = i-1, j
        elif B[i,j][2]:
            i, j = i, j-1
        backtrace_idxs.append((i,j))
    return backtrace_idxs

#The next function takes a backtrace and computes the alignment between two words
def alignment(w1, w2, bt):
    aligned1 = []
    aligned2 = []
    operations = []
    backtrace = bt[::-1] # make it a forward trace
    for k in range(len(backtrace) - 1):
        i0, j0 = backtrace[k]
        i1, j1 = backtrace[k+1]
        w1_letter = None
        w2_letter = None
        op = None
        if i1 > i0 and j1 > j0: # either substitution or no-op
            if w1[i0] == w2[j0]: # no-op (the same symbol)
                w1_letter = w1[i0]
                w2_letter = w2[j0]
                op = " "
            else: # cost increased: substitution
                w1_letter = w1[i0]
                w2_letter = w2[j0]
                op = "s"
        elif i0 == i1: # insertion
                w1_letter = " "
                w2_letter = w2[j0]
                op = "i"
        else: # j_0 == j_1, deletion
                w1_letter = w1[i0]
                w2_letter = " "
                op = "d"
        aligned1.append(w1_letter)
        aligned2.append(w2_letter)
        operations.append(op)
    return tb.tabulate([aligned1, aligned2, operations])   

#The next function formats the results from the minimum distance algorithm and backtracking to a
#table that is human-readable.
def make_table(word_1, word_2, D, B, bt):
    w1 = word_1.upper()
    w2 = word_2.upper()
    w1 = "#" + w1
    w2 = "#" + w2
    table = []
    table.append([""] + list(w2))
    for i, l_1 in enumerate(w1):
        row = [l_1]
        for j, l_2 in enumerate(w2):
            v, d, h = B[i,j]
            direction = ("⇑" if v else "") +\
                ("⇖" if d else "") +\
                ("⇐" if h else "")
            dist = str(D[i,j])
            cell_str = "{direction} {star}{dist}{star}".format(
                                           direction=direction,
                                           star=" *"[((i,j) in bt)],
                                           dist=dist)
            row.append(cell_str)
        table.append(row)
    return print(tb.tabulate(table, stralign="right", tablefmt="orgtbl"))

#Minimum edit distance function
def min_edit_dist(X, Y):
    n = len(X) + 1 # counting empty string
    m = len(Y) + 1
    # initialize D matrix
    D = np.zeros(shape=(n, m), dtype=np.int)
    D[:,0] = range(n)
    D[0,:] = range(m)
    # B the backtrack matrix: at each index, a triple of booleans, used as flags
    # ex: B(i,j) = (1, 1, 0), the distance D(i,j) came from a deletion or a substitution
    B = np.zeros(shape=(n, m), dtype=[("del", 'b'),
    ("sub", 'b'),
    ("ins", 'b')])
    B[1:,0] = (1, 0, 0)
    B[0,1:] = (0, 0, 1)
    for i, c1 in enumerate(X, start=1):
        for j, c2 in enumerate(Y, start=1):
            deletion = D[i-1,j] + 1
            insertion = D[i, j-1] + 1
            substitution = D[i-1,j-1] + (0 if c1==c2 else 2)
            mo = np.min([deletion, insertion, substitution])
            B[i,j] = (deletion==mo, substitution==mo, insertion==mo)
            D[i,j] = mo
    return print("\nDistance matrix:\n", D), print("\nBacktrace matrix:\n", B), print("\nMinimum edit distance table:\n "), make_table(X, Y, D, B, backtrace(B)), print("\nAlignment table:\n", alignment(X, Y, backtrace(B)))

#Call of the function min_edit_dist
min_edit_dist("location", "location")

#Damerau-Levenshtein
def min_edit_dist_D(X, Y):
    n = len(X) + 1 # counting empty string
    m = len(Y) + 1
    # initialize D matrix
    D = np.zeros(shape=(n, m), dtype=np.int)
    D[:,0] = range(n)
    D[0,:] = range(m)
    # B the backtrack matrix: at each index, a triple of booleans, used as flags
    # ex: B(i,j) = (1, 1, 0), the distance D(i,j) came from a deletion or a substitution
    B = np.zeros(shape=(n, m), dtype=[("del", 'b'),
    ("sub", 'b'),
    ("ins", 'b'),
    ("trans", 'b')]) #modificare
    B[1:,0] = (1, 0, 0, 0)
    B[0,1:] = (0, 0, 0, 1)
    for i, c1 in enumerate(X, start=1):
        for j, c2 in enumerate(Y, start=1):
            deletion = D[i-1,j] + 1
            insertion = D[i, j-1] + 1
            substitution = D[i-1,j-1] + (0 if c1==c2 else 2)
            transposition = D[i-2, j-2] + (0 if c1==c2 else 1)
            mo = np.min([deletion, insertion, substitution, transposition])
            B[i,j] = (deletion==mo, substitution==mo, insertion==mo, transposition==mo)
            D[i,j] = mo
    return print("\nDistance matrix D:\n", D),  print("\nBacktrace matrix D:\n", B), print("\nMinimum edit distance table:\n "), make_table(X, Y, D, B, backtrace(B)), print("\nAlignment table D:\n", alignment(X, Y, backtrace(B)))
#
min_edit_dist_D("location", "location")
