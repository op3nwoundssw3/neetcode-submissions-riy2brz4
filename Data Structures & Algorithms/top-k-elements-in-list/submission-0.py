class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict() # value:count
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        sorted_dict = sorted(count.items(),key=lambda item: item[1] ,reverse=True)
        
        rez = []
        for i in range(k):
            rez.append(sorted_dict[i][0])
        return rez

        