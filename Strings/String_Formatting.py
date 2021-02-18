def print_formatted(number):
    s=bin(number)
    length=len(s[2:])+1
    
    for i in range(1,number+1):
        integer=str(i)
        octal=str(oct(i))
        hexa=hex(i).upper()
        binary=str(bin(i))
        print( integer.rjust(length-1)  +  octal[2:].rjust(length)   +      hexa[2:].rjust(length) +     binary[2:].rjust(length))       

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
