# LeedCode example
def searchInsert(nums: List(int), target: int) -> int:
  
    nums.append(target)
    def bubble(nums):
        n = len(nums)

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    def bubble_sort(nums):
        n = len(nums)

        for _ in range(n-1):
            if bubble(nums) == 0:
                break
                
    bubble_sort(nums)
    
    l = 0
    r = len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
print(searchInsert([1,3,7,6], 5))
