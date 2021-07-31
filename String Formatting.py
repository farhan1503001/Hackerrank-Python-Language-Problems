
if __name__=='__main__':
    number=int(input().strip())
    width=len(bin(number)[2:])
    for num in range(number+1):
        print(str(num).rjust(width,' '),oct(num).replace('0o','').rjust(width,' '),
        hex(num).replace('0x','').upper().rjust(width,' '),
        bin(num).replace('0b','').rjust(width,' ')
        )