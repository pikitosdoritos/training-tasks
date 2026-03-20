# 1 
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

# 2
# Searching first unique symbol

s = "leetcode"

frequency = {}

def find_unique_symbol():
    for ch in s:
        if ch not in frequency:
            frequency[ch] = 1
        else:
            frequency[ch] += 1
            
    for key, value in frequency.items():
        if value == 1:
            return s.index(key)
            
print(find_unique_symbol())

# We have to strings. Return if it`s anagram.

s = "anagram"
t = "nagaram"

