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
            

def q51():
    lst = [2]
    dic = {}
    dic[2] = 0
    lst, dic = get_primelst(1000000, lst, dic)      
    
    for v in lst:
        strv = str(v)
        sz = len(strv)
        for i in range(0,sz-1):
            st = int(strv[i])
            if  st>2:
                continue
            cntv = []
            
            for j in xrange(st, 10):
                v1 = v + (j-st)*(10**(sz-i-1))
                if v1 in dic:
                    cntv.append(v1)
            if len(cntv) >= 8:
                print cntv,st, i
                
            for ii in range(i+1, sz-1):
                if strv[i]<>strv[ii]:
                    continue
                cntv = []
                for j in xrange(st, 10):
                    v1 = v + (j-st)*(10**(sz-i-1)) + (j-st)*(10**(sz-ii-1))
                    if v1 in dic:
                        cntv.append(v1)
                if len(cntv) >= 8:
                    print cntv,st, i,ii
                    
                for iii in range(ii+1, sz-1):
                    if strv[i]<>strv[iii]:
                        continue
                    cntv = []
                    for j in xrange(st, 10):
                        v1 = v + (j-st)*(10**(sz-i-1)) + (j-st)*(10**(sz-ii-1))+ (j-st)*(10**(sz-iii-1))
                        if v1 in dic:
                            cntv.append(v1)
                    if len(cntv) >= 8:
                        print cntv,st, i,ii, iii
                 

            
def q52():
    for v in xrange(1, 1000000):
        lstv = sorted([s for s in str(v)])
        isok = True
        for i in xrange(2, 7):
            if sorted([s for s in str(v*i)]) <> lstv :
                isok = False
                break
        if isok:
            print [v*i for i in xrange(1,7)]
            return  
            

def cal_combine(n, a):
    fz = 1
    fm = 1
    for i in xrange(1,a+1):
        fz *= (n-i+1)
        fm *= i
    return fz/fm
    
def q53():
    sums = 0
    for n in xrange(1, 101):
        for a in xrange(1, n-1):
            if cal_combine(n ,a) > 1000000:
                sums += n-a-a + 1
                break
    print sums

def get_pokerv(strv):
    v1 = strv[0]
    a = 0
    b = 0
    if v1=='J':
        a = 11
    elif v1 =='Q':
        a = 12
    elif v1 == 'K':
        a = 13
    elif v1 == 'A':
        a = 14
    elif v1 == 'T':
        a = 10
    else :
        a = int(strv[0])
        
    v2 = strv[1]
    if v2 =='D':
        b = 1
    elif v2 == 'S':
        b = 2
    elif v2 == 'H':
        b = 3
    elif v2 == 'C':
        b = 4
    return (a,b)



def cla_cnt(lst):
    dic = {}
    maxd = 1
    for v in lst:
        if v in dic:
            dic[v] += 1
            if maxd < dic[v]:
                maxd = dic[v]
        else :
            dic[v] = 1
    #print dic
    return maxd , dic
    



def cal_poker(l):
    l1 = sorted([v[0] for v in l])
    l2 = [v[1] for v in l]
    if len(set(l2)) == 1:
        #print l
        if l1 == [10,11,12,13,14]:
            return (10,100000)
        isok = True
        for i in xrange(4):
            if l1[i+1]-l1[i] <> 1:
                isok = False
                break
        if isok:
            return (9, l1[4])
        return (6, sorted(l1, reverse = True))
    maxd, dic = cla_cnt(l1)
    if maxd == 4:
        for k in dic:
            if dic[k] == 4:
                a = k
            if dic[k] == 1:
                b = k
        #print l
        return (8,a,b)

    if maxd == 3:
        
        b = []
        isfull = True
        for k in dic:
            if dic[k] == 3:
                a = k
            if dic[k] == 1:
                b.append(k)
                isfull = False
            if dic[k] == 2:
                c = k
        if isfull:
            #print 7, l
            return (7,a,c)
        else :
            #print 4,l
            return (4,a, sorted(b, reverse=True))
    if maxd == 2:
        a = []
        b = []
        cnt = 0
        for k in dic:
            if dic[k] == 2:
                a.append(k)
                cnt +=1
            if dic[k] == 1:
                b.append(k)
        if cnt == 2:
            print 3, l
            return (3,sorted(a, reverse=True), sorted(b, reverse=True))
        return (2,sorted(a, reverse=True), sorted(b, reverse=True))
    if maxd == 1:
        isok = True
        for i in xrange(4):
            if l1[i+1]-l1[i] <> 1:
                isok = False
                break
        if isok:
            return (5,l1[4])
        return (1, sorted(l1,reverse = True))
        
            

def cal_pokerwin(l1,l2):
    v1 = cal_poker(l1)
    v2 = cal_poker(l2)
    #print v1, v2
    if v1[0] > v2[0]:
        return 0
    elif v1[0]< v2[0]:
        return 1
    else:
        if v1[0] == 10:
            return -1
        if v1[0] == 9 or v1[0] == 8 or v1[0] == 5 or v1[0]  == 6 or v1[0]  == 1 or v1[0]  == 4:
            if v1[1]>v2[1]:
                return 0
            return 1
        if v1[0] == 7:
            if v1[1] > v2[1]:
                return 0
            elif v1[1] == v2[1] and v1[2] > v2[2]:
                return 0
            return 1
        if v1[0] == 2 or v1[0] == 3:
            if v1[1]> v2[1] or (v1[1] == v2[1] and v1[2]> v2[2]):
                return 0
            return 1
        

            
# 1 High Card: Highest value card.
# 2 One Pair: Two cards of the same value.
# 3 Two Pairs: Two different pairs.
# 4 Three of a Kind: Three cards of the same value.
# 5 Straight: All cards are consecutive values.
# 6 Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
            
    

    
def q54(): 
    f = open('res/poker.txt', 'r')
    strv = f.read()   
    rounds = strv.split('\n')
    rnd_pair = []
    for v in rounds:
        l = v.split(' ')
        if len(l) < 10:
            break
        l1 = []
        l2 = []
        for i in xrange(5):
            l1.append(get_pokerv(l[i]))
        for i in xrange(5,10):
            l2.append(get_pokerv(l[i]))
        rnd_pair.append((l1,l2, cal_pokerwin(l1,l2)))
        
    cnt = 0
    for v in rnd_pair:
        #print v
        if v[2] == 0:
            cnt +=1
    print cnt

def get_rev(i):
    strv  = str(i)
    rev = ''
    for i in xrange(len(strv)-1, -1, -1):
        rev += strv[i]
    return int(rev)

def is_para(v):
    strv = str(v)
    ln = len(strv)
    for i in xrange(0, ln/2+1):
        if strv[i] <> strv[ln-1-i]:
            return False
    return True
    
def q55():
    dic = {}
    cnt = []
    for i in xrange(10, 10000):
        if i in dic:
            continue
#         if not is_para(i):
#             continue
        v = i
        step = []
        isok = False
        for _ in xrange(49):
            revi = get_rev(v)
            v = revi + v
            step.append(i)
            step.append(revi)
            if is_para(v):
                isok = True
                break
            
        if isok:
            for v in step:
                dic[v] = 1
        else:
            cnt.append(i)
    
    print len(cnt)
    
    

            
def q56():
    sums = 0
    maxa = 0
    maxb = 0
    for a in xrange(1,100):
        for b in xrange(1, 100):
            x = a**b
            num = sum(int(v) for v in str(x))
            if num > sums:
                sums = num
                maxa = a
                maxb = b
    print sums, maxa, maxb
    
def get_com_deivider(a,b):
    v1 = max(a,b)
    v2 = min(a,b)
    while True:
        if v1%v2 == 0:
            return v2
        v1, v2 = v2, v1%v2
        
def q57():
    a = 3
    b = 2
    sums = 0
    for i in xrange(1000):
        a2, b2 = a+2*b, a+b
        d = get_com_deivider(a2,b2)
        a,b  = a2/d, b2/d
        print i ," : ", a2, b2, d , a , b
        if len(str(a)) > len(str(b)):
            sums += 1
            print a, b, i
        
    print sums
    
def q58():
    #the data on the diagram of n line is : (2n-1)^2, -(2n-2), -2(2n-2), -3(2n-2)
    #the total number of diagram is 4n-3
    prime_lst = []
    
    n = 1
    while True:
        n += 1
        a = (2*n-1)**2
        if is_prime(a):
            prime_lst.append(a)
        for _ in range(3):
            a = a-(2*n-2)
            if is_prime(a):
                prime_lst.append(a) 
                
        if len(prime_lst)*100.0 /(4*n-3) < 10.0:
            print (2*n-1)
            break
        
    
    
    
    
def qq():
    pass

#----------------------It is a split line--------------------------------------

def main():
    q58()
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"