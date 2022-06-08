#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
if __name__ == '__main__':
    
    l = [random.randint(0, 99) for i in range(20)]
n_l=l[:]
 
print(l.index(sorted(set(l))[-2]))

y = l.index(max(l))
l[0], l[y] = l[y], l[0]
 
z = l.index(min(l))
l[-1], l[z] = l[z], l[-1]
 
print(n_l)
print(l)