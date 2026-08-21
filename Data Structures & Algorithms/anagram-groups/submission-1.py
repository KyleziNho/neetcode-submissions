class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = {}
        for s in strs:
            s_sort = "".join(sorted(s))
            if s_sort not in group_anagram:
                group_anagram[s_sort] = []
            group_anagram[s_sort].append(s)
        return list(group_anagram.values())


                

            
            
            
        

            
            
        