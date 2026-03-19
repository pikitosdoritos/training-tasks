#1 
# We have a list of numbers. We need to find two numbers that in sum will be equal our target. Return indexes of these numbers. 

nums = [10, 100, 22, 2, 9, 11, 10, 7, 22, 15]
target = 9

seen = {}

def find_indx():
    for i, number in enumerate(nums):
        need = target - number
        if need not in seen:
            seen[number] = i
        else:
            return [seen[need], i]
        
print(find_indx())