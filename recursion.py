#https://bbhosted.cuny.edu/bbcswebdav/pid-58541472-dt-content-rid-458899634_1/courses/SPS01_IS_211_002_1219_1/SPS01_IS_211_002_1219_1_ImportedContent_20210712111902/Week14%20-%20Assignment.pdf

#fibonacci
def fibonacci(n):
    if n <= 2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)


#euclid
def gcd(a, b): 

    if a == 0 :
        return b 
      
    return gcd(b % a, a)

    
#compare strings
def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1
    elif len(s2) == 0:
        return 1

    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])


if __name__ == '__main__':
    print(fibonacci(18))
    print(gcd(20, 200))
    print(compareTo('team', 'tm'))
