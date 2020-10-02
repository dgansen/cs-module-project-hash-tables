a = [
        [8, [4]], 
        [[90, 91], -1, 3], 
        [9, 62], 
        [[-7, -1, [-56, [-6]]]], 
        [201], 
        [[76, 0], 18],
      ]

def recurSum(arr):
    s = 0
    compare_set = set()
    for elem in arr:
        if type(elem) == list:
            s += recurSum(elem)
        else:
            compare_set.add(elem)
    if len(compare_set) > 0:
        s += min(compare_set)
    return s
        
print(recurSum(a))