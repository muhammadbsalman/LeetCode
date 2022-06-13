class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        this_dict={}
        for x in range(len(numbers)):
            this_dict[numbers[x]]=x
        for x in range(len(numbers)):
            if (target-numbers[x]) in this_dict:
                return [x+1, this_dict[target-numbers[x]]+1]
