# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:29:49 2019

@author: Sorina
"""

# =============================================================================
# Matching Methods in Python
# =============================================================================

# =============================================================================
# 1. Basic Similarity Measures
# 1.1 Name-Based Techniques
# 1.1.1. String-Based Methods
# String Equality: string equality, Hamming distance, substring test, substring similarity, n-Gram similarity. 
# Edit Distances: Levenshtein distance, Needleman-Wunsch distance, Jaro measure, Jaro–Winkler measure, SMOA.
# Token-based Distances work well on long texts: Cosine similarity, TF-IDF, Kullback-Leibler divergence.
# 1.1.2. Language-Based Methods
# Intrinsic Methods, Linguistic Normalisation: tokenization, lemmatization, stopword elimination.
# Extrinsic Methods: synonymy similarity, cosynonymy similarity, Resnik semantic similarity, Jiang-Conrath, Lin information-theoretic similarity, Leacock-Chodorow, Hirst-St.Onge, edge count, Wu-Palmer, gloss overlap.
# 
# =============================================================================

# =============================================================================
# The Edit Distance (Levenshtein Distance) is a measure of similarity between two strings. The
# distance between the source and the target is the minimum number of edit operations (deletions,
# insertions, or substitutions) required to transform the source into the target. The lower the distance,
# the more similar the two strings.
# =============================================================================

# =============================================================================
# N.B. We analyze properties and classes respective entities
#      from DBpedia and Wikidata (English versions)
# For testing purpose :
#      a. location
#     https://www.wikidata.org/wiki/Property:P276
#     http://dbpedia.org/ontology/location
#      b. Berlin
#     http://dbpedia.org/page/Berlin
#     https://www.wikidata.org/wiki/Q64
# =============================================================================

import nltk
dbWord = 'location'
wikidataWord = 'location'
print("edit dist: ", nltk.edit_distance(dbWord, wikidataWord))

dblabel = "location"
wikidataAliases = ['moveable object location', 'located in', 'event location', 'venue', 'is in', 'location of item', 'place held',
'based in', 'neighborhood', 'region', 'in']
for word in wikidataAliases:
 ed = nltk.edit_distance(dblabel, word)
 print(word, ed)
 
# =============================================================================
# moveable object location 16
# located in 4
# event location 6
# venue 8
# is in 6
# location of item 8
# place held 8
# based in 7
# neighborhood 11
# region 5
# in 6
# =============================================================================
 
#print the word with the minimum distance from the given list
 edword = sorted([(nltk.edit_distance(dblabel, word), word) for word in wikidataAliases])
print("minimum distance word(s): ", edword[0][1])



# =============================================================================
# Jaccard Distance is a measure of how dissimilar two sets are. 
# The lower the distance, the more
# similar the two strings are. The Jaccard Distance depends on the Jaccard Similarity Index which is
# (the number in both sets) / (the number in either set) * 100.
# J(X,Y)=|X intersects Y| / |X U Y|
# The Jaccard Distance, D(X,Y) = 1 – J(X,Y).
# =============================================================================

dbWord = 'location'
wikidataWord = 'location'
print("Jaccard dist: ", nltk.jaccard_distance(set(dbWord), set(wikidataWord)))


dblabel = "location"
wikidataAliases = ['moveable object location', 'located in', 'event location', 'venue', 'is in', 'location of item', 'place held',
'based in', 'neighborhood', 'region', 'in']
for word in wikidataAliases:
 ed = nltk.jaccard_distance(set(dblabel), set(wikidataAliases))
 print(word, ed)
 
# =============================================================================
#  Sentence or paragraph comparison    
#  Distances calculated for sentences
#  In our example, for property location, we have
#  
#  DBpedia: rdfs:comment --> The location of the thing.
#  Wikidata: description --> location of the item, physical object or event is within. In case of an administrative entity use P131. In case of a distinct terrain feature use P7
#  
#  
# =============================================================================
 

sent1 = "The location of the thing."
sent2 = "location of the item, physical object or event is within. In case of an administrative entity use P131. In case of a distinct terrain feature use P7"

#Edit distance
ed_sent_1_2 = nltk.edit_distance(sent1, sent2)
print('Edit Distance between sent1 and sent2: ', ed_sent_1_2)

#Jaccard Distance
distancejaccard_sent_1_2 = nltk.jaccard_distance(set(sent1), set(sent2))
print('Jaccard  Distance between sent1 and sent2: ', distancejaccard_sent_1_2)

