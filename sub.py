from bisect import bisect_left

def lengthOfLIS(nums):
    if not nums:
        return 0

    lis = [nums[0]]

    for num in nums[1:]:
        if num > lis[-1]:
            lis.append(num)
        else:
            # Utilizamos la búsqueda binaria para encontrar la posición
            # donde el número puede ser insertado para mantener la subsecuencia creciente más larga.
            index = bisect_left(lis, num)
            print(index)
            lis[index] = num
        print(lis)
    print(lis)
    return len(lis)

nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums1))  # Output: 4

nums2 = [0, 1, 0, 3, 2, 3]
print(lengthOfLIS(nums2))  # Output: 4

nums3 = [7, 7, 7, 7, 7, 7, 7]
print(lengthOfLIS(nums3))  # Output: 1