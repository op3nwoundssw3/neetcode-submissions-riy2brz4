class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = dict()
        my_dict2 = dict()
        for i in s:
            if i in my_dict.keys():
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        for j in t:
            if j in my_dict2.keys():
                my_dict2[j] += 1
            else:
                my_dict2[j] = 1
        if my_dict == my_dict2:
            return True
        else:
            return False