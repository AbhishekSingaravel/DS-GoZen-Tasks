def find_missing_number(nums):
    n = len(nums) + 1
    total = (n * (n + 1)) // 2
    array_sum = sum(nums)
    
    return total - array_sum
    
input_array = list(map(int, input("Enter the array of integers: ").split()))
print("Missing Number:", find_missing_number(input_array))