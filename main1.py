def pascal(n):
    if n == 1:
        return [[1]]
    
    if n == 2:
        return [[1], [1, 1]]
    
    arr = pascal(n - 1)
    last_row = arr[-1]
    new_row = [1]
    
    for i, item in enumerate(last_row):
        if i >= len(last_row) - 1:
            new_row.append(1)
            break
        
        pair_sum = item + last_row[i + 1]
        new_row.append(pair_sum)
        
    arr.append(new_row)
    
    return arr

print(pascal(5))