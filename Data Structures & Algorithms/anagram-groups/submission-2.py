class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0]*26

            for c in word:
                idx = ord(c) - ord("a")
                count[idx] += 1

            key =  tuple(count)
            groups[key].append(word)
        return list(groups.values())




        