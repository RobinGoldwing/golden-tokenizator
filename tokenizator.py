#!/bin/env python3

import os, sys



if __name__ == "__main__":


    source = sys.stdin
    
    s = 0
    t=''
    for line in source:
        
        for c in line:
            
            if s == 0:
                
                if c.upper() in ['A','B','C','D','E','F','G','H','J','K','L','M','N','Ñ','O','P','Q','R','S','T','V','W','Y','X','Z','Á','É','Í','Ó','Ú']: 
                    t = c
                    s = 1
                else:
                    print(c)
                    s = 0
            
            elif s == 1:
                
                if c.upper() in ['A','B','C','D','E','F','G','H','J','K','L','M','N','Ñ','O','P','Q','R','S','T','V','W','Y','X','Z','Á','É','Í','Ó','Ú']:
                    s = 1
                    t = t + c
                
                else:
                    print(t)
                    print(c)
                    s = 0
                    