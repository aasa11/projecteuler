#!/usr/bin/
#coding=gbk
'''
Created on 2013年9月18日

@summary: 

@author: huxiufeng
'''

def q16():
    strs = str(2**1000)
    sums = 0
    for i in strs:
        sums +=int(i)
    print sums

def get_letters(x, letters):
    sums = 0
    a = int(x / 100)
    if a > 0 and a < 10:
        sums += len(letters[a])+len(letters[100])
    elif a == 10:
        sums += len(letters[1])+len(letters[1000])
    
    left = x-a*100
    if left == 0:
        return sums
    if a > 0 and a<10: 
        sums += len('and')
    b = int(left/10)
    if b == 0:
        sums += len(letters[left])
    elif b > 1:
        sums += len(letters[b*10])+len(letters[left-b*10])
    else:
        sums += len(letters[left])
    return sums
    
def q17():
    letters = {0:'',1:'one', 2:'two', 3: 'three',4: 'four',5: 'five',6: 'six',7: 'seven',8: 'eight',9: 'nine',10: 'ten', 
               11: 'eleven',12: 'twelve',13: 'thirteen',14: 'fourteen',15: 'fifteen',16: 'sixteen',17: 'seventeen',18: 'eighteen',19: 'nineteen',20: 'twenty',
               30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'
               }
    
#     print get_letters(1000,letters)
    
    sums = 0
    for i in xrange(1,1001):
        sums += get_letters(i, letters)
    print sums

def q18():
    strs = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
    lst = strs.split('\n')
    lst2 = []
    for l in lst:
        lst2.append([int(i) for i in l.split(' ')])
    print lst2
    
    totallen = len(lst2)
    lst3 = []
    for idx in xrange(totallen-1, -1, -1):
        if idx == totallen-1:
            lst = []
            for i in lst2[idx]:
                lst.append(i)
            lst3.append(lst)
            continue
        idx2 = totallen-1-idx
        lst = []
        for i, v in enumerate(lst2[idx]):
            if v+lst3[idx2-1][i] > v+lst3[idx2-1][i+1]:
                lst.append(v+lst3[idx2-1][i])
            else:
                lst.append(v+lst3[idx2-1][i+1])
        lst3.append(lst)
        
    print lst3
    
def get_Faburaryday(year):
    if year % 400 == 0:
        return 29
    elif year % 100 == 0:
        return 28
    elif year % 4 == 0:
        return 29
    else :
        return 28

def get_yearday(year):
    days = 31+  get_Faburaryday(year)+31+30+31+30+31+31+30+31+30+31
    return days

def get_mothday(year, month):
    if month == 2:
        return get_Faburaryday(year)
    elif month == 4 or month ==6 or month == 9 or month == 11:
        return 30
    else :
        return 31

def q19(): 
    sundays = 0
    weekday = 0
    for year in xrange(1900,2001):
        if year == 1900:
            for _ in xrange(get_yearday(year)):
                weekday += 1
                if weekday >= 7:
                    weekday = 0
            print weekday
            continue
        
        for month in xrange(1,13):
            if weekday == 6:
                sundays += 1
            for _ in xrange(get_mothday(year, month)):
                weekday += 1
                if weekday >= 7:
                    weekday = 0
    
    print sundays
        
def q20():
    proc = 1
    for i in xrange(1, 101):
        proc =proc*i
        
    sums = sum([int(i) for i in str(proc)])
    print sums
    
    
def get_divsum(x):
    if x <= 2:
        return 1
    sums = 1
    for i in xrange(2, int(x**0.5)+1):
        if x %i == 0:
            if i * i == x:
                sums += i
            else:
                sums = sums + i + x/i
    return sums

def q21():
    dicts = {}
    sums = 0
    for x in xrange(1, 10000):
        div = get_divsum(x)
        if (div, x) in dicts.keys():
            print "x", x, "div", div
            sums += x+div
        else :
            dicts[(x, div)] = '1'
    print sums

def get_chridx(C):
    return (ord(C)-ord('A'))+1

def q22():
    filename = r'res/names.txt'
    f = open(filename,'r')
    strs = f.read()
    f.close()
    lst = strs.split(',')
    lst = sorted([str(i[1:-1]) for i in lst])
    
    total = 0
    for i, v in enumerate(lst):
        sums = sum([get_chridx(c) for c in v])
        print v, sums, i+1
        total += sums*(i+1)
    print total
    
def q23():   
    maxs = 28124
    lst = []
    for _ in range(maxs):
        lst.append(0)
    for x in xrange(1,maxs):
        div = get_divsum(x)
        if div > x:
            lst[x] = 1
            
    sums = 1
    for x in xrange(2, maxs):
        isAbound = False
        for y in xrange(1, x):
            if lst[y] == 1 and lst[x-y] == 1:
                isAbound = True
                break
        if not isAbound:
            sums += x
    print sums

def is_order(x):
    strs = str(x)
    lst = [int(i) for i in strs]
    lst = sorted(lst)
    bft = -1
    for i in lst:
        if bft == -1:
            bft = i
            continue
        elif i-bft <> 1:
            return False
        else:
            bft = i
            continue
    return True

def cal_P(a,b):
    proc = 1
    for i in xrange(b):
        proc = proc * (a-i)
    return proc

def q24():
    countMax = 1000000
    
    count = 0
    lst = []
    for i in xrange(9,0,-1):
        k = 0
        while True:
            if count + cal_P(i,i) >countMax:
                lst.append(k)
                print k
                break
            elif count+cal_P(i,i) == countMax:
                print k
                print "i", i
                count = count +cal_P(i,i)
                print "out..."
                return
            else :
                count += cal_P(i,i)
                k += 1
    print countMax -count
    
def q25():
    a = 1
    b = 1
    idx = 2
    while True:
        tmp = b
        b = a+b 
        a = tmp
        idx += 1
        if len(str(b)) == 1000 :
            print idx
            return
        
def cal_recusive(x):
    rec = 0
    lst = []
    st = 1
    lst.append(st)
    ans = []
    p = 0
    while True:
        addzero = 0
        while st < x:
            st *= 10
            addzero +=1
        if addzero >= 2:
            for i in xrange(1, addzero):
                ans.append(0)
                lst.append(0)
        p = st % x
        ans.append(int(st/x))
        if p == 0:
            return 0, ans, 0
        elif p in lst:
            break
        else :
            rec += 1
            st = p
            lst.append(st)
    
    starts = False
    count = 0
    for v in lst:
        if v == p:
            starts = True
        if starts:
            count += 1
    return count, ans ,p
    
            
        
def q26():
    maxrec = 0
    for x in xrange(1, 1000):
        rec ,_,_ = cal_recusive(x)
        if rec > maxrec:
            maxrec = rec
            maxx = x
    print maxrec, maxx
    print cal_recusive(maxx)
    print 1.0/maxx
    
    
def fx(x,a,b):
    return x*x +a*x + b  

def is_prime(x):
    if x == 0:
        return False
    if x < 0:
        x = (-1)*x
    
    for i in xrange(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True         


def q27():
    maxp = 0
    maxn = 0
    maxa = 0
    maxb = 0
    
    for b in xrange(-999, 1000):
        if b<>1 and not is_prime(b):
            continue
        if abs(b) < maxn:
            continue
        for a in xrange(-999,1000):
            if a %2 == 0:
                continue
            n = 0
            cnt = 0
            while True:
                v = fx(n,a,b)
                if is_prime(v):
                    cnt += 1
                    n += 1
                else:
                    break
            if maxp < cnt:
                maxp = cnt
                maxn = n
                maxa = a
                maxb = b
    print maxp , maxn, maxa, maxb
    for x in xrange(0, maxn+1):
        print fx(x, maxa, maxb), is_prime(fx(x, maxa, maxb))
    print maxa*maxb
    
def cal_rnd(n):
    if n == 1:
        return 1
    v = 4*(n**2) -(n-1)*6
    return v
    
    
def q28():
    rnd = 1001
    sums = 0
    for x in xrange(1,rnd+1,2):
        sums += cal_rnd(x)
    print sums

def q29():
    lst = []
    for a in xrange(2,101):
        for b in xrange(2,101):
            lst.append(a**b)
    
    st = set(lst)
    print len(st)
    
def cal_nump(x, p):
    sums = 0
    for v in str(x):
        sums += int(v)**p
    return sums
        
    
def q30():
    p = 5
    sums = 0
    for x in xrange(2, 10**6):
        if x == cal_nump(x, p):
            sums += x
            print x
    print "sums is ", sums
    
def qq():
    pass

#----------------------It is a split line--------------------------------------

def main():
    q30()
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"