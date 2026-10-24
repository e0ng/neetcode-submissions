from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_dict = defaultdict(list)

        for s in strs:
            word_dict[tuple(sorted(s))].append(s)

        return list(word_dict.values())
        
        

# 아스키코드 활용
# (26개) 튜플로 변환해서 키로 사용 : array 는 키 사용 불가능