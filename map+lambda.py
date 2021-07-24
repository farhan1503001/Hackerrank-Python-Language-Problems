#Use of function with map
def reverse_string(string):
    
    value=''.join(string[i] for i in range(len(string)-1,-1,-1))
    return value
def ceaser_cipher(string):
    value=''.join(chr((ord(string[i])+3-97)%26+97) for i in range(len(string)))
    return value
if __name__=='__main__':
    store=list(map(str,input().split()))
    print(store)
    size_array=list(map(len,store))
    print(size_array)
    reverse_string=list(map(reverse_string,store))
    print(reverse_string)
    cipher_text=list(map(ceaser_cipher,store))
    print(cipher_text)