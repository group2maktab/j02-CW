def sortTuples(lst1, lst2):
    zipped = list(zip(lst1, lst2))
    sortedTuples = sorted(zipped)
    return sortedTuples
lst1 = ["Mike", "Danny", "Jim", "Annie"]
lst2 = [4, 12, 7, 19]
sortedTuples = sortTuples(lst1, lst2)
print(sortedTuples)
