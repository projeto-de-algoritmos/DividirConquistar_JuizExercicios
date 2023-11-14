import random

def find_kth_largest(nums, k):
    def partition(left, right, pivot_index):
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if nums[i] > pivot_value:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1

        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index

    def quick_select(left, right, k_largest):
        if left == right:
            return nums[left]

        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if k_largest == pivot_index:
            return nums[k_largest]
        elif k_largest < pivot_index:
            return quick_select(left, pivot_index - 1, k_largest)
        else:
            return quick_select(pivot_index + 1, right, k_largest)

    k_largest = k - 1

    return quick_select(0, len(nums) - 1, k_largest)

# Exemplo de uso:
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
output1 = find_kth_largest(nums1, k1)

nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
output2 = find_kth_largest(nums2, k2)

print(output1)  # Output: 5
print(output2)  # Output: 4




