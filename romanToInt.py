    
def romanToInt(s):
    vals = {'I':1, 'V':5, 'X':10,'L':50, 'C':100,'D':500,'M':1000}
    sum = 0
    i = 0
    while i < len(s):
        try:
            if vals[s[i]] < vals[s[i+1]]:
                sum += (vals[s[i+1]] - vals[s[i]])
                i+=2
                continue
        except IndexError:
            pass
        sum += vals[s[i]]
        i+=1
    return sum

if __name__ == "__main__":
    s = "MCMXCIV"
    print(romanToInt(s))