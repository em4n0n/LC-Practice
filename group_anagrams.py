from typing import List
from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] +=1