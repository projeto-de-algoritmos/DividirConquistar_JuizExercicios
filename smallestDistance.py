def kthSmallestDistance(nums, k):
    def count_pairs(nums, mid):
        count = 0
        j = 0
        n = len(nums)

        for i in range(n):
            while j < n and nums[j] - nums[i] <= mid:
                j += 1
            count += j - i - 1

        return count

    nums.sort()
    low, high = 0, nums[-1] - nums[0]

    while low < high:
        mid = (low + high) // 2
        count = count_pairs(nums, mid)

        if count < k:
            low = mid + 1
        else:
            high = mid

    return low

nums1 = [1, 3, 1]
k1 = 1
print(kthSmallestDistance(nums1, k1))  # Saída: 0

nums2 = [1, 1, 1]
k2 = 2
print(kthSmallestDistance(nums2, k2))  # Saída: 0

nums3 = [1, 6, 1]
k3 = 3
print(kthSmallestDistance(nums3, k3))  # Saída: 5
