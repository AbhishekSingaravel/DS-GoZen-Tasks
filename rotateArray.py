def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[n - k:] + nums[:n - k]

input_array = list(map(int, input("Enter the array of integers: ").split()))
k = int(input("Enter the number of steps to rotate the array: "))

rotate_array(input_array, k)
print("Rotated Array:", input_array)