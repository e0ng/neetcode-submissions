
class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_strs = ""

        for s in strs:
            encode_strs += f"{len(s)}#{s}"

        return encode_strs

    def decode(self, s: str) -> List[str]:
        result_list = []
        i = 0

        while i < len(s):
            j = s.find("#", i) # i부터 시작해서 # 찾기
            word_len = int(s[i: j])
            result_list.append(s[j+1 : j+1+word_len])
            i = j+1+word_len



                
        return result_list


            
                
                

# 숫자-기준문자-원문