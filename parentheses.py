class parentheses(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        mydict = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for i in s:
            if i not in mydict:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != mydict[i]:
                        return False
        return not stack

#Stack and dictionary is best for this solution because stack is last in first out and allows you to keep track of the top of the stack. 
