class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'}':'{',']':'[',')':'('}
        for i in s:
            if i in dic.values():
                stack.append(i)
            elif i in dic.keys() and len(stack)>0 and dic[i] == stack[-1]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
            
            