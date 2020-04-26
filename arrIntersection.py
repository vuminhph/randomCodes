def intersection(nums1, nums2):
  if len(nums1) > len(nums2):
  	smaller_arr, larger_arr = nums2, nums1  
  else:
    smaller_arr, larger_arr = nums1, nums2
  inter_arr = []
  dict = {elem : 1 for elem in smaller_arr}
  for elem in larger_arr:
    if dict.get(elem) == 1:
    	inter_arr.append(elem)
    dict[elem] = 0
  return inter_arr

print(intersection([1, 2, 3, 4, 5], [2, 4]))