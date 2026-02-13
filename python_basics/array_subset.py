#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    
    def isSubset(self, a, b):
        a_dict = Counter(a)
        for num in b:
            if a_dict[num] == 0:
                return False
            a_dict[num] -= 1
        return True
