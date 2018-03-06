maxVal = ''
    for i in range(len(s) - 1):
        for j in range(i, len(s)):
            subStr = s[i:j]
            if len(subStr) > len(maxVal):
                if subStr == subStr[::-1]:
                    maxVal = subStr
    if len(s) == 1:
        return s
    else:
        return maxVal
