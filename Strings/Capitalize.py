#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    text=s.split()
#    print('s is ====>>'+s)
    final_text=''    
    space=''
#    print(text)
    for i in range(0,len(text)):
        space=''

        result_length=len(final_text)
    
        if(i+1 < len(text)):
            #print("----------------------------"+str(i)+"r_s===>"+str(result_length))    
            a_string=s[result_length:].find(text[i])+len(text[i])+result_length
            #print("a_s====>"+str(a_string))
            a=s[a_string:].find(text[i+1])+a_string
    
            print(a)
            
            b_string = s[result_length:].find(text[i])+len(text[i])+result_length
            b = b_string-1
            #print("b_s===>>"+str(b_string))
            print(b)
                
            
            space_len = a-b-1
            space=' '*space_len
    
        if(text[i][:1].isalpha() and text[i][:1].islower()):
            final_text=final_text+text[i][:1].upper()+text[i][1:]+space
        else:
            final_text=final_text+text[i]+space
    return final_text
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

