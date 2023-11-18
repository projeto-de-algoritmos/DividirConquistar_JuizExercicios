def findMedianSortedArrays(nums1, nums2):
    merged = []
    i, j = 0, 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    merged += nums1[i:]
    merged += nums2[j:]
    
    total_length = len(merged)
    
    if total_length % 2 == 0:
        mid_right = total_length // 2
        mid_left = mid_right - 1
        return (merged[mid_left] + merged[mid_right]) / 2
    else:
        mid = total_length // 2
        return merged[mid]

nums1_example1 = [1, 3]
nums2_example1 = [2]
print(findMedianSortedArrays(nums1_example1, nums2_example1))

nums1_example2 = [1, 2]
nums2_example2 = [3, 4]
print(findMedianSortedArrays(nums1_example2, nums2_example2))
