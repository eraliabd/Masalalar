def findMedianSortedArrays(nums1: List(int), nums2: List(int)) -> float:
    lists1 = 0
    lists = nums1 + nums2
    # sorted_lists = sorted(lists)
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

        print(nums)
    bubble_sort(lists)
    if len(lists) % 2 == 0:
        l_num = (len(lists)-1)//2
        lists1 = (lists[l_num] + lists[l_num+1])/2
    else:
        l_num = (len(lists)-1)//2
        lists1 = lists[l_num]
    return lists1

print(findMedianSortedArrays([3], [-2, -1]))
