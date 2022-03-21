def mostCommonFirstletter(s):
    common = { }
    for letter in s:
        l = letter.split(",")[0]
        if l[0] not in common:
            common[l[0]] = 0
        common[l[0]] += 1
    return common

strng = "do you have a voting plan for the election happening next month?"
lst = strng.split()
print(mostCommonFirstletter(lst))