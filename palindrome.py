class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        harfler=list(cleaned)
        ters = []
        for i in range(len(harfler)):
                ters.append(harfler[-i-1])
        if harfler == ters:
            return True
        else:
            return False
        
