#!/usr/bin/
#coding=gbk
'''
Created on 2013年9月22日

@summary: 

@author: huxiufeng
'''

def cal_cmb(value, lst):
    if value < 0:
        return 0
    if value == 0:
        return 1
    if len(lst) == 1:
        return 1
    v = lst[0]
    cmb = 0
    for idx in range(0, int(value/v)+1):
        cmb +=cal_cmb(value - idx*v, lst[1:])
    return cmb

def q31():
    lst = [200,100,50,20,10,5,2,1]
    print cal_cmb(200, lst)
        

def is_pandigital(a,b,c):
    v = str(a)+str(b)+str(c)
    if len(v) <> 9:
        return False
    lst = sorted([int(x) for x in v])
    if lst <> [1,2,3,4,5,6,7,8,9]:
        return False
    return True

def q32():
    count = 0
    proc = []
    for a in xrange(1, 10):
        for b in xrange(1000,10000):
            if is_pandigital(a, b, a*b):
                print a, b, a*b
                count += 1
                proc.append(a*b)
    for a in xrange(10,100):
        for b in xrange(100,1000):
            if is_pandigital(a, b, a*b):
                print a, b, a*b
                count += 1
                proc.append(a*b)
    print count, sum(x for x in set(proc))
    
def get_rmv(a,b):
    a1 = a%10
    a2 = a/10
    b1 = b%10
    b2 = b/10
    
    if a1 == b1 and a1 <> 0 and a2 <>b2:
        return True, a2, b2
    if a1 == b2 and a1<> 0 and a2 <> b1:
        return True,  a2, b1
    if a2 == b1 and a2<>0 and a1 <> b2:
        return True , a1, b2
    if a2 == b2 and a2<>0 and a1 <> b1:
        return True, a1, b1
    return False , 0,0
    
def get_commondivider(a, b):
    if a > b:
        a, b = b,a
    while True:
        c = b % a
        if c == 0:
            return a
        a , b = c, a

def q33():
    count = 0
    proc = []
    for a in xrange(10,99):
        for b in xrange(a+1, 100):
            isok, a1, b1 = get_rmv(a,b)
            if not isok:
                continue
            if a1*b == b1*a:
                print a, b
                count += 1
                proc.append((a,b))
        
    a = 1
    b = 1
            
    for v in proc:
        a *= v[0]
        b *= v[1]
    print a,b
    
    c = get_commondivider(a, b)
    print c, b/c

def cal_fraction(x):
    if x == 0:
        return 1
    proc = 1
    for i in xrange(2, x+1):
        proc *= i
    return proc                 

def cal_nufraction(x, lst):
    return sum(lst[int(v)] for v in str(x))

def get_frc9():
    n = 1
    f9 = cal_fraction(9)
    while True:
        a = f9 * n
        b = 10**n
        print a, b
        if b > a:
            print "n is ", n
            break
        n +=1
        
        
def q34():
#     get_frc9()
#     return
    lst = []
    for i in xrange(0,10):
        lst.append(cal_fraction(i))
        
    print lst
    cnt = 0
    proc = []
    for i in xrange(3, 10**7):
        if i == cal_nufraction(i, lst):
            print i
            cnt += 1
            proc.append(i)
            
    print cnt
    print sum(v for v in proc)

def is_prime(x):
    if x == 0:
        return False
    if x < 0:
        x = (-1)*x
    
    for i in xrange(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True  

def get_lp(x):
    v = str(x)
    lst = []
    for i in xrange(1, len(v)):
        lst.append(int(v[i:]+v[:i]))
        
    return lst
    
def q35():
    prime = [2]
    for x in xrange(3, 1000000,2):
        if is_prime(x):
            prime.append(x)
            
    ans = []
    
    for x in prime:
        lst = get_lp(x)
        if len(lst) == 0:      
            ans.append(x)
        else:
            isok = True
            for v in lst:
                if v not in prime:
                    isok = False
                    break
            if isok:
                ans.append(x)
              
    print ans
    print len(ans)

def get_base2(x):
    v = []
    rem = x
    while rem > 1:
        v.append(rem%2)
        rem = int(rem/2)
    
    v.append(1)
    
    return v[::-1]
        
def is_palindromes(v):
    for i in range(0, len(v)/2+1):
        if v[i] <>v[len(v)-1-i]:
            return False
    return True

def q36():
    cnt = 0
    proc = []
    for i in xrange(1, 1000000):
        if is_palindromes([int(v) for v in str(i)]) \
            and is_palindromes(get_base2(i)):
            cnt += 1
            proc.append(i)
    print cnt
    print proc
    print sum(v for v in proc)

def is_mvinlst(x, primes):
    v = str(x)
    for i in xrange(1,len(v)):
        if int(v[i:]) not in primes:
            return False
        if int(v[0:len(v)-i]) not in primes:
            return False
    return True

def q37():
    primes = [2,3,5,7]
    ans = []
    x = 11
    while True:
        if is_prime(x):
            primes.append(x)
            
            if is_mvinlst(x, primes):
                ans.append(x)
                print x
            if len(ans) >= 11:
                break
        x += 1
    print ans
    print sum(x for x in ans)

def is_pandigital2(strv):
    if len(strv) <> 9:
        return False
    lst = sorted([int(v) for v in strv])
    if lst <>[1,2,3,4,5,6,7,8,9]:
        return False
    return True

def q38():
    maxv = 0 
    maxx = 0
    maxn = 0
    for x in xrange(1,10000000):
        strv = ""
        i = 1
        while True:
            strv += str(i*x)
            if len(strv) >= 9:
                break
            i += 1
        if is_pandigital2(strv):
            if int(strv)> maxv:
                maxv = int(strv)
                maxx = x
                maxn = i
                print maxv, maxx, maxn 
    print maxv, maxx, maxn 
    
def q39():
    maxcnt = 0
    maxp = 0
    for p in xrange(10,1001):
        lstv = []
        for a in xrange(1,int(p/2)):
            for b in xrange(a+1, p-a):
                if (p-a-b)**2 == a**2 + b**2:
                    l = sorted([a,b,p-a-b])
                    dt = 1000*1000*l[0]+1000*l[1]+l[2]
                    lstv.append(dt)
                    break
                elif (p-a-b)**2 < a**2 + b**2:
                    break
        if len(lstv) <= 0:
            continue
        print lstv
        cnt = len(set(lstv))
        if cnt > maxcnt:
            maxcnt = cnt
            maxp = p
            print maxcnt, maxp
    print maxcnt, maxp
                

def q40():
    i = 1
    cnt = 0
    idx = 1
    lst = []
    while True:
        strv = str(i)
        l = len(strv)
        while l+cnt >= idx:
            lst.append(strv[idx-cnt-1])
            idx *= 10
        cnt += l
        if idx > 1000000:
            break
        i += 1
    print lst
    proc = 1
    for v in lst:
        proc *= int(v)
    print proc
    
def is_pandigital3(x):
    strv = str(x)
    lst = sorted([int(v) for v in strv])
    if lst == range(1,len(strv)+1):
        return True
    return False    

def get_pandigitalrev(lst):
    for idx, v in enumerate(lst):
        if len(lst) == 1:
            yield lst
        else:
            lst2 = lst[0:idx]+lst[idx+1:]
            #print lst2
            for l in get_pandigitalrev(lst2):
                lst3 = [v] + l
                yield lst3
    
def q41():
    for n in xrange(9,1,-1):
        lst = range(n,0,-1)
        for l in get_pandigitalrev(lst):
            print l
            strv = ''
            if l is None:
                continue
            for v in l:
                strv += str(v)
            if is_prime(int(strv)):
                print l
                return

def cal_trnum(strv):
    s = 0
    for v in strv:
        s += ord(v)-ord('A')+1
    return s


def q42():
    filename = r'res/words.txt'
    f = open(filename, 'r')
    ws = f.read()
    f.close()
    lst = ws.split(',')
    print lst
    lst2 = []
    for v in lst:
        lst2.append(v[1:-1])
    print lst2

    trlst = []
    for i in xrange(1,100,1):
        trlst.append(i*(i+1)/2)
    print trlst
    cnt = 0
    for v in lst2:
        if cal_trnum(v) in trlst:
            print v
            cnt +=1
    print cnt

def q43():
    lst = range(0,10)
    primelst = [2,3,5,7,11,13,17]
    s = 0
    for l in get_pandigitalrev(lst):
        if l[0] == '0':
            continue
        isok = True
        for i in xrange(7):
            strv = ''
            for x in xrange(1,4):
                strv += str(l[x+i])
            if int(strv) % primelst[i] <> 0:
                isok = False
                break
        if isok:
            strv = ''
            for v in l:
                strv += str(v)
            s += int(strv)
            print strv
            
    print s
    

def q44():
    lst = [2,10,24,44]
    j = 3
    while True:
        lens = len(lst)
        if j > lens-1:
            for p in xrange(lens+1, 2*lens):
                lst.append(p*(3*p-1))
            print lst
        for i in xrange(j-1,(j/2), -1):
            if lst[j]-lst[i] in lst:
                v = lst[j]-lst[i]
                print v, lst[i], lst[j]
                if lst[i]-v in lst:
                    print (lst[i]-v)/2
                    return
        j += 1

def q45():
    maxx = 100000
    lst1 = []
    dict2 = {}
    dict3 = {}
    for n in xrange(1, maxx):
        lst1.append(n*n+n)
        dict2[3*n*n-n] = 0
        dict3[4*n*n-2*n] = 0
    
    sums = 0
    j = 0
    for j in xrange(1, maxx-1):
        if lst1[j] in  dict2 :
            print lst1[j], j
            if lst1[j] in dict3:
                sums += 1
                print "ok", (lst1[j])/2, j
        if sums >= 3:
            print "find"
            break


def qq():
    pass
#----------------------It is a split line--------------------------------------

def main():
    q45()
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"