# -*- coding: utf-8 -*-
"""
@author: clair
"""

from collections import defaultdict

sentences = ["new home sales top forecasts", "home sales rise in july", "increase in home sales in july", "july new home sales rise"]

def indexSentences(sentences):
    s = []
    for sentence in sentences:
        s += [sentence.split(" ")]
    
    dic = defaultdict()
    for idx, doc in enumerate(s):
        for term in doc:
            try:
                dic[term] += [idx]
            except KeyError as e:
                dic[term] = []
                dic[term] += [idx]
    return dic
    
sentences = ["breakthrough drug for schizophrenia", "new schizophrenia drug", "new approach for treatment of schizophrenia", "new hopes for schizophrenia patients"]

# Get documents with schizophrenia and drug
#set(dic['schizophrenia']).intersection(dic['drug'])

# Get documents with for but NOT drug OR approach
#set(dic['for']).difference(dic['drug'], dic['approach'])

def intersect(a, b):
    sect = []
    try:
        aIdx = 0
        bIdx = 0
        while(True):
            if a[aIdx] == b[bIdx]:
                sect += [a[aIdx]]
                aIdx += 1
                bIdx += 1
            elif a[aIdx] < b[bIdx]:
                aIdx += 1
            else:
                bIdx += 1
    except:
        pass
    return sect
    
# Put length of posting with posting
#for key in dic.keys():
#   dic[key] = (len(dic[key]), dic[key])
    
    
def union(a, b):
    uni = []
    try:
        aIdx = 0
        bIdx = 0
        while(True):
            if a[aIdx] == b[bIdx]:
                uni += [a[aIdx]]
                aIdx += 1
                bIdx += 1
            elif a[aIdx] < b[bIdx]:
                uni += [a[aIdx]]
                aIdx += 1
            else:
                uni += [b[bIdx]]
                bIdx +=1
    except:
        if aIdx != len(a):
            uni += a[aIdx:]
        elif bIdx != len(b):
            uni += b[bIdx:]
    return uni
    
def difference(a, b):
    if len(a) == 0:
        return []
    if len(b) == 0:
        return a
    if a[0] == b[0]:
        return difference(a[1:], b[1:])
    elif a[0] < b[0]:
        return [a[0]] + difference(a[1:],b)
    else:
        return difference(a, b[1:])