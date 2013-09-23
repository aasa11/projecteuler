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

def qq():
    pass
#----------------------It is a split line--------------------------------------

def main():
    q36()
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"