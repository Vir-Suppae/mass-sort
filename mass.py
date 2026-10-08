def sort(array: list[int]):
    arr = array.copy()
    i = 1
    zeroes = 0
    while not all(a <= b for a, b in zip(arr, arr[1:])):
        print(i, arr)
        if len(arr) % 2**(i+1) != 0:
            arr.append(0)
            zeroes += 1
            continue
        arrs: list[list] = [arr[j:j+2**i] for j in range(0, len(arr), 2**i)]
        for k in range(0, len(arrs), 2):
            if sum(arrs[k+1]) < sum(arrs[k]):
                arrs[k], arrs[k+1] = arrs[k+1], arrs[k]
        arr = [x for chunk in arrs for x in chunk]
        to_pop = []
        for idx in range(len(arr)):
            if arr[idx] == 0 and zeroes > 0:
                zeroes -= 1
                to_pop.append(idx)
        for index in to_pop:
            arr.pop(index)
                
        i += 1
        if 2**i > len(arr):
            i = 1
    return arr[:len(array)]
            
        
