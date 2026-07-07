class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count_s = Counter(s)
        count_t = Counter(t)
        
        return count_s == count_t

        # for char in t:
        #     if char not in count_s:
        #         return False
        #     count_s[char] -=1
        #     if count_s[char] == 0:
        #         del count_s[char]
        
        # if count_s
        


        