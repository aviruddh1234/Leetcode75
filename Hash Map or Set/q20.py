def finddifference(nums1, nums2):
    output = []
    
    output.append(list(set(nums1)-set(nums2)))
    output.append(list(set(nums2)-set(nums1)))
    
    return output 

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

print(finddifference(nums1, nums2))