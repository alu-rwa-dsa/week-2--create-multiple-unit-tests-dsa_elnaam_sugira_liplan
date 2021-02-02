

def StringDict(str):
    toList = []
    toList[:0] = str
    
    dict = {}
    for char in toList:  # O(N)
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1  # O(logn)
    
    return dict


if __name__ == "__main__":
    print(StringDict("Hello"))

# Time Complexity - O(nlogn)
# Space Complexity - O(n)