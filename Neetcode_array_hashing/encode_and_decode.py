# https://www.lintcode.com/problem/659/
# premium in leetcode

inp = ["lint","code","love","you"]

def encode(strs):

    res = ""
    for s in strs:
        res += str(len(s)) + '#' + s
    
    return res

print(encode(inp))

inp_decode = '4#lint4#code4#love3#you'

def decode(str):
    
    res = []
    i = 0

    while i < len(str):
        j = i
        while str[j] != '#':
            j += 1
        len_num = int(str[i:j])
        # print(len_num)
        res.append(str[j+1:j+1+len_num])
        i = j + 1 + len_num

    return res
            

print(decode(inp_decode))

