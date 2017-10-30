#!/usr/bin/env python

import os
import sys
import random


l1 = random.sample(xrange(1, 51), 20)
l2 = random.sample(xrange(1, 51), 20)
l3 = random.sample(xrange(1, 51), 20)
l4 = [1,2,3,4]
l5 = [1,2,4,5]
l6 = [1,2,3,6]


def main(l1,l2,l3):
	print(l1)
	print(l2)
	print(l3)
	print("In alle drie sets")
	print(set(l1).intersection(l2,l3))
	print("In een van de twee sets")
	print(set(l1).intersection((set(l2) | set(l3))))
	print("manier 2")
	print(str(float(len(set(l1).intersection(l2,l3)))/float(len(set(l1)))*100) + " procent van list 1 zit ook in list 2 en 3")
if __name__ == '__main__':
    sys.exit(main(l1,l2,l3))
