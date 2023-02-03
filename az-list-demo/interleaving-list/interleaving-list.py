import itertools

# interleaving list
# insert 1 element from list1 then 2 elements from list2 to the combined list

def merge_lists(list1, list2):
    result = []
    for i in range(0, max(len(list1), len(list2) // 2 + 1)):
        if i < len(list1):
            result.append(list1[i])
        if 2 * i < len(list2):
            result.append(list2[2 * i])
            result.append(list2[2 * i + 1])
    return result

l1 = [1,2,3,4,5]
l2 = [11, 22, 33, 44, 55, 66, 77, 88]

l = merge_lists(l1, l2)
print(l)
