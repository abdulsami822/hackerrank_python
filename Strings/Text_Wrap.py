import textwrap

def wrap(string, max_width):
    b=textwrap.wrap(string,max_width)
    c=''
    for i in range(0,len(b)):
        if(c==''):
            newline=''
        else:
            newline='\n'
        c=c+newline+b[i]
    return c

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
