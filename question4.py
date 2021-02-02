
listA = [20, 5, 2, 9, 3]

listB = [20, 2, 9, 3]


def TwoLists(lsA, lsB):
    for num in lsA:  # O(A) - t
        if num not in lsB: # O(B) - t
            return num


if __name__ == "__main__":
    print(TwoLists(listA, listB))


# Time Complexity - O(A * B)
# Space Complexity - O(1)