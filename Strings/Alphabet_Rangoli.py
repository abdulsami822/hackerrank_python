import string

def print_rangoli(size):
    all_chars=''.join(string.ascii_lowercase)
    
    width=(2*size-1)+(2*size-2)
    design='-'
    
    for i in range(size-1,-size,-1):
        

        if(i<0):
            i=i*-1
        line=''    
        line=line+design*(2*i)
        
        



        j=size-1
                                                 
        while(len(line) <= width//2):
            if((len(line)+1) % 2 ==0):
                line=line+design
            else:
                line=line+all_chars[j]
                j=j-1


    #    print(line)
        
        


        last_char=line[len(line)-1]
        j=all_chars.find(last_char)
    
        while(len(line)  <  width):
            if(j == size-1):
                line=line+design
            else:
                if((len(line)+1)  % 2 ==0):
                    line=line+design
                else:
                    j=j+1
                    line=line+all_chars[j]
                    
        print(line)




if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
