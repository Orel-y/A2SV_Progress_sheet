class Solution:    
    def findUnion(self, a, b):
        union = set()
        
        for ina in a:
            union.add(ina)
            
        for inb in b:
            union.add(inb)
            
        return union
