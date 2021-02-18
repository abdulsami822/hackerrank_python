if __name__ == '__main__':
    s = input()
    alnum='False'
    alpha='False'
    digit='False'
    lower='False'
    upper='False'
    for i in range(0,len(s)):
        if(s[i].isalnum() and alnum=='False'):
            alnum='True'
        if(s[i].isalpha() and alpha=='False'):
            alpha='True'
        if(s[i].isdigit() and digit=='False'):
            digit='True'
        if(s[i].islower() and lower=='False'):
            lower='True'
        if(s[i].isupper() and upper=='False'):
            upper='True' 
    print(alnum+'\n'+alpha+'\n'+digit+'\n'+lower+'\n'+upper)   

