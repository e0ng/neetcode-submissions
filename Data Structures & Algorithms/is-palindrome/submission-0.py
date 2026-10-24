class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1

        while i < j :
            char_l = s[i].lower()
            char_r = s[j].lower()

            if not (('a' <= char_l <= 'z') or ('0' <= char_l <= '9')):
                i+=1
                continue
            if not (('a' <= char_r <= 'z') or ('0' <= char_r <= '9')):
                j-=1
                continue
            
            if char_l != char_r:
                return False
                break
            
            i += 1
            j -= 1
            
        return True
