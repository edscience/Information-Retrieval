# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 00:35:49 2017

@author: clair
"""
from math import floor, sqrt
from InvertedIndex import intersect

#chdir("C:\\Users\\DELL\\OneDrive\\Documents\\Work - School\\Personal\\Information Retrieval")

# Note that this implementation isn't quite right
# Since the sqrt(len(a)) depends on the current length
# of a rather than on the original length of a
def intersectWithSkips(a, b):
    if len(a) == 0:
        return []
    elif len(b) == 0:
        return []      
    if a[0] == b[0]:
        return [a[0]] + intersectWithSkips(a[1:], b[1:])
    elif (a[0] < b[0]):
        try:         
            if (a[floor(sqrt(len(a)))] <= b[0]):
                return intersectWithSkips(a[floor(sqrt(len(a))):], b)
            else:
                return intersectWithSkips(a[1:], b)
        except: 
            return intersectWithSkips(a[1:], b)
        
    else:
        try:
            if (b[floor(sqrt(len(b)))] <= a[0]):
                return intersectWithSkips(a, b[floor(sqrt(len(b))):])
            else:
                return intersectWithSkips(a, b[1:])
        except:
            return intersectWithSkips(a, b[1:])
            
# Creates a positional index from the 'docs'
# In this case, the 'docs' are just strings,
# which is why we can just split them by spaces
def positionalIndex(docs):
    posIndex = dict()
    for docIdx, doc in enumerate(docs):
        for wordIdx, word in enumerate(doc.split(" ")):
            try: # If word already has an entry for doc
                posIndex[word][docIdx][0] += 1
                posIndex[word][docIdx][1].append(wordIdx)
            except KeyError:
                try: # If posIndex[word] was already initialized to a dict
                    posIndex[word][docIdx] = [1, [wordIdx]]
                except KeyError: # If posIndex[word] was never accessed, make it a dict
                    posIndex[word] = dict()
                    posIndex[word][docIdx] = [1, [wordIdx]]
    return posIndex
    
def positionalIntersect(pA, pB, k):
    docIds = intersect(sorted(pA.keys()), sorted(pB.keys()))
    intersection = []
    for docId in docIds:
        a = pA[docId][1]
        b = pB[docId][1]
        for i in range(len(a)):
            j = 0
            while (j != len(b) and b[j] - a[i] <= k):
                if (abs(a[i] - b[j]) <= k):
                    intersection.append((docId, a[i], b[j]))
                j += 1
    return intersection
    
sentences = ["At Dogs and Cats Rule we strive to provide your pet with superior quality brands you won't find in a typical box store or supermarket.", "If your dog or cat has been diagnosed with diabetes mellitus, it's easy to feel alone—but you're not.", "Jul 6, 2011 - The war between cats and dogs is a topic of debate from Hollywood to hometowns."]
s = positionalIndex(sentences)
positionalIntersect(s['cats'], s['dogs'], 3)