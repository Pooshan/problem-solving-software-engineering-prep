
# Q: Merge Two Sorted Lists

l1 = [1, 2, 4]
l2 = [1, 3, 4]


def merge(l1, l2):
    m = len(l1)
    n = len(l2)
    i = m - 1
    j = n - 1
    k = (m + n - 1)
    output = []
    while i >= 0 and j >= 0:
        if l1[i] > l2[j]:
            output.insert(0, l2[j])
            j -= 1
        elif l1[i] == l2[j]:
            output.insert(0, l2[j])
            output.insert(0, l1[i])
            j -= 1
            i -= 1
        else:
            output.insert(0, l1[i])
            i -= 1
    while i >= 0:
        for ele in output:
            if ele == l1[i] or ele > l1[i]:
                ele_index = output.index(ele)
                output.insert(ele_index, l1[i])
                i -= 1
                break
    while j >= 0:
        for ele in output:
            if ele == l2[j] or ele > l2[j]:
                ele_index = output.index(ele)
                output.insert(ele_index, l2[j])
                j -= 1
                break
    # print(i)
    # print(j)
    return output


print(merge(l1, l2))
