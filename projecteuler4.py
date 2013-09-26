#!/usr/bin/
#coding=gbk
'''
Created on 2013年9月25日

@summary: 

@author: huxiufeng
'''

def is_prime(x):
    if x == 0:
        return False
    if x < 0:
        x = (-1)*x
    
    for i in xrange(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True  

def get_primelst(p, lst,dic):
    for i in xrange(lst[-1]+1, p+1):
        if is_prime(i):
            lst.append(i)  
            dic[i] = 0         
    return lst ,dic



def q46():
    lst = [2]
    dic = {}
    dic[2] = 0
    lst2= []
    dic2 = {}
    for i in xrange(1, 500):
        lst2.append(i*i)
        dic2[i*i] = 0
    lst, dic = get_primelst(500, lst, dic)
    print lst
    
    n = 31
    while True:
        n += 2
        if n > lst[-1]:
            lst, dic = get_primelst(2*n, lst, dic)
        if n in dic:
            continue
        
        isok = False
        for v in lst:
            if v > n:
                break
            pp = (n-v)/2
            if pp > lst2[-1]:
                mm = int(lst2[-1]**0.5)
                for m in xrange(mm+1, 2*mm):
                    lst2.append(m*m)
                    dict[m*m] = 0
            
            if pp in dic2:
                isok = True
                break
            
        if not isok:
            print n
            return


def get_factors(x, lst):
    cnt = []
    while x > 1:
        for p in lst:
            if x % p  == 0:
                cnt.append(p)
                x = x/ p
                break
    return len(set(cnt))

def q47():
    lst = [2]
    dic = {}
    dic[2] = 0
    lst, dic = get_primelst(500, lst, dic)
    print lst
    print get_factors(100, lst)
        
    n = 10
    while True:
        n += 1
        if n+3 > lst[-1]:
            lst, dic = get_primelst(2*n, lst, dic)
        if get_factors(n, lst) == 4:
            if get_factors(n+1, lst) == 4:
                if get_factors(n+2, lst) == 4:
                    if get_factors(n+3, lst) == 4:
                        print n
                        return 
                    

def q48():
    maxx = 10000000000
    sums = 0
    for n in xrange(1,1001):
        v = n
        for  _ in xrange(1, n):
            v *=n
            if v > maxx:
                v = v % maxx
        sums = (sums+v)% maxx
    print sums

def q49():
    lst = [2]
    dic = {}
    dic[2] = 0
    lst, dic = get_primelst(10000, lst, dic)
    print lst
    
    dicts = {}
    
    for n in lst:
        if n < 1000:
            continue
        strv = str(n)
        lstv = sorted([v for v in strv])
        strv = ''
        for v in lstv:
            strv += v
        nn = int(strv)
        
        if nn in dicts:
            dicts[nn].append(n)
        else:
            dicts[nn] = [n]
    
    lstvall = []
    
    for k in dicts.keys():
        lstv = dicts[k]
        lstv = sorted(lstv)
        if len(lstv) >= 3:
            lstvall.append(lstv)
            print lstv


    lstmatch = []
    for v in lstvall:
        l = len(v)
        for i in xrange(0,l-2):
            for j in xrange(i+1, l-1):
                if v[j]*2 - v[i] in v:
                    print v[i], v[j], 2*v[j]-v[i]
                    lstmatch.append([v[i], v[j], 2*v[j]-v[i]])
                    
    print lstmatch
    
    
def q50():
    maxnum = 10**6
    lst = [2]
    dic = {}
    dic[2] = 0
    lst, dic = get_primelst(maxnum, lst, dic)
    
    maxnt = 2
    fst = 2
    for i in xrange(len(lst)):
        if i + maxnt >len(lst):
            break
        sums = lst[i]
        cnt = 1
        for j in xrange(i+1, len(lst)):
            if cnt < maxnt:
                sums += lst[j]
                cnt += 1
                if sums > maxnum:
                    break
                continue
            else:
                sums += lst[j]
                cnt += 1
                if sums > maxnum:
                    break
                if sums in dic:
                    print cnt, lst[i]
                    maxnt = cnt
                    fst = lst[i]
                    
    print maxnt, fst
    
    print sum(v for v in lst[3:543+3])
            
            
        

def qq():
    pass

#----------------------It is a split line--------------------------------------

def main():
    q50()
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"