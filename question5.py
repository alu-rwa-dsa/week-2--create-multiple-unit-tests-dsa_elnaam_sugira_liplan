
def ocurrenceCalc(num):
    ls = []
    val = num
    occ = 1

    while val != 0:  #O(N)
        addls = num - (val - 1)
        ls.append(addls)
        if occ == addls:
            val = val - 1  # go to next num
            occ = 1
        else:
            occ = occ + 1  # O(logn)
        
    return ls


print(ocurrenceCalc(6))

# Time Complexity - O(nlogn)
# Space Complexity - O(1)