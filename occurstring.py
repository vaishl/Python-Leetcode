class occurstring(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lengthneedle = len(needle)
        lengthhay = len(haystack)

        #checking if needle is haystack
        if needle not in haystack:
            return -1

        for i in range(0, lengthhay):
            move=i+lengthneedle
            if haystack[i:move] == needle:
                return i

#This solution doesn't use the two pointer method. Instead, it keeps track of the length of the substring as it can only occur at certain positions, then it tracks if it is possible


