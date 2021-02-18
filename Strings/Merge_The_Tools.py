def merge_the_tools(string, k):
    sub_list=[string[i:i+k] for i in range(0,len(string),k)]
    for i in range(len(sub_list)):
            temp_list=[]
            temp_list=[sub_list[i][j:j+1] for j in range(len(sub_list[i]))]
            
            temp_list2=[]
            [temp_list2.append(x) for x in temp_list if x not in temp_list2]
            #print(temp_list2)
            print(''.join(temp_list2))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
