#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = 'Last digit of'
str2 = 'is'
str3 = 'and is greater than 5'
str4 = 'and is 0'
str5 = 'and is less than 6 and not 0'

if number[-1]>5:
    print(f'{str} + {number} + {str2} + {number[-1]} + {str3}')

if number[-1] == 0:
    print(f'{str} + {number} + {str2} + {number[-1]} + {str4}')

if number[-1] != 0 & number[-1]<6:
    print(f'{str} + {number} + {str2} + {number[-1]} + {str5}')
