

def mergesort(inp):
    n = len(inp)
    if n < 2:
        return inp
    left = mergesort(inp[:n // 2])
    right = mergesort(inp[n // 2:])

    output = []
    i = j = 0
    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    
    while(i < len(left)):
        output.append(left[i])
        i += 1

    while (j < len(right)):
        output.append(right[j])
        j += 1
    return output

x = [1, 5,2,3,7,4]
print('x is ' + str(x))
print('after sorting, x is ' + str(mergesort(x)))
