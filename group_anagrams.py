from typing import List
from collections import defaultdict

def groupAnagrams(strs):
    result = defaultdict(list)
    
    for s in strs:
        count = [0] * 26