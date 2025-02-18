class Palindrome(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        
        alist = []
        if abs(x) != x:
            return False
        else:
            alist = [int(digit) for digit in str(x)]
            blist = alist[::-1]
            return alist == blist
        """
        if x < 0:
            return False
        return str(x) == str(x)[::-1] #This solution has a better time complexity
