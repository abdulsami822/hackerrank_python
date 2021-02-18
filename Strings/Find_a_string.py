def count_substring(string, sub_string):
    count=0
    for i in range(0,len(string)-len(sub_string)+1):
        if(string.find(sub_string,i,len(sub_string)+i)>=0):
            count=count+1
    return count


