class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat_list = []
        new_nums = []
        for sublist in nums:
            for num in sublist:
                flat_list.append(num)

        if len(flat_list) != r*c:
            return nums
        else:
            for i in range(0,len(flat_list),c):
                new_nums.append(flat_list[i:i+c])
            return new_nums
