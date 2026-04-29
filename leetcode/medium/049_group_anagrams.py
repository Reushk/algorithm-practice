""""
problem: group anagrams
difficulty:medium
topic: array,hash table
""""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            count = {}
            for c in word:
                count[c] = count.get(c,0) + 1

            key = tuple(sorted(count.items()))

            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]
        
        return list(d.values())
