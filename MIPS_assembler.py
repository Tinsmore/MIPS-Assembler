def decToBin5(strnum):
    num=int(strnum)
    s=''
    if(num>31):
        return s
    while(num>0):
        s=str(num%2)+s
        num=num//2
    if(len(s)<5):
        s=(5-len(s))*'0'+s
    return s

def decToBin16(strnum):
    num=int(strnum)
    s=''
    while(num>0):
        s=str(num%2)+s
        num=num//2
    if(len(s)<16):
        s=(16-len(s))*'0'+s
    return s

def decToBin26(strnum):
    num=int(strnum)
    s=''
    while(num>0):
        s=str(num%2)+s
        num=num//2
    if(len(s)<26):
        s=(26-len(s))*'0'+s
    return s

def add(li):
    s='000000'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[3][1:])
    s+=decToBin5(li[1][1:])
    s+='00000100000'
    return s

def sub(li):
    s='000000'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[3][1:])
    s+=decToBin5(li[1][1:])
    s+='00000100010'
    return s

def And(li):
    s='000000'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[3][1:])
    s+=decToBin5(li[1][1:])
    s+='00000100100'
    return s

def Or(li):
    s='000000'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[3][1:])
    s+=decToBin5(li[1][1:])
    s+='00000100101'
    return s

def xor(li):
    s='000000'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[3][1:])
    s+=decToBin5(li[1][1:])
    s+='00000100110'
    return s

def sll(li):
    s='00000000000'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[1][1:])
    s+=decToBin5(li[3])
    s+='000000'
    return s

def srl(li):
    s='00000000000'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[1][1:])
    s+=decToBin5(li[3])
    s+='000010'
    return s

def sra(li):
    s='00000000000'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[1][1:])
    s+=decToBin5(li[3])
    s+='000011'
    return s

def addi(li):
    s='001000'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[1][1:])
    s+=decToBin16(li[3])
    return s

def andi(li):
    s='001100'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[1][1:])
    s+=decToBin16(li[3])
    return s

def ori(li):
    s='001101'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[1][1:])
    s+=decToBin16(li[3])
    return s

def xori(li):
    s='001110'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[1][1:])
    s+=decToBin16(li[3])
    return s

def beq(li):
    s='000100'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[1][1:])
    s+=decToBin16(li[3])
    return s

def bne(li):
    s='000101'
    s+=decToBin5(li[2][1:])
    s+=decToBin5(li[1][1:])
    s+=decToBin16(li[3])
    return s

def lui(li):
    s='00111100000'
    s+=decToBin5(li[1][1:])
    s+=decToBin16(li[2])
    return s

def lw(li):
    s='100011'
    i=0
    while(i<len(li[2])):
        if(li[2][i]=='$'):
            break
        i=i+1
    s+=decToBin5(li[2][i+1:-1])
    s+=decToBin5(li[1][1:])
    s+=decToBin16(li[2][:i-1])
    return s

def sw(li):
    s='101011'
    i=0
    while(i<len(li[2])):
        if(li[2][i]=='$'):
            break
        i=i+1
    s+=decToBin5(li[2][i+1:-1])
    s+=decToBin5(li[1][1:])
    s+=decToBin16(li[2][:i-1])
    return s

def jr(li):
    s='000000'
    s+=decToBin5(li[1][1:])
    s+='000000000000000001000'
    return s

def j(li):
    s='000010'
    s+=decToBin26(li[1])
    return s

def jal(li):
    s='000011'
    s+=decToBin26(li[1])
    return s

def assemble(cmd):
    result=''
    li=cmd.split()
    if(li[0]=='add' and li[1][0]=='$' and li[2][0]=='$' and li[3][0]=='$'):
        result=add(li)
    elif(li[0]=='sub' and li[1][0]=='$' and li[2][0]=='$' and li[3][0]=='$'):
        result=sub(li)
    elif(li[0]=='and' and li[1][0]=='$' and li[2][0]=='$' and li[3][0]=='$'):
        result=And(li)
    elif(li[0]=='or' and li[1][0]=='$' and li[2][0]=='$' and li[3][0]=='$'):
        result=Or(li)
    elif(li[0]=='xor' and li[1][0]=='$' and li[2][0]=='$' and li[3][0]=='$'):
        result=xor(li)
    elif(li[0]=='sll' and li[1][0]=='$' and li[2][0]=='$'):
        result=sll(li)
    elif(li[0]=='srl' and li[1][0]=='$' and li[2][0]=='$'):
        result=srl(li)
    elif(li[0]=='sra' and li[1][0]=='$' and li[2][0]=='$'):
        result=sra(li)
        
    elif(li[0]=='addi' and li[1][0]=='$' and li[2][0]=='$'):
        result=addi(li)
    elif(li[0]=='andi' and li[1][0]=='$' and li[2][0]=='$'):
        result=andi(li)
    elif(li[0]=='ori' and li[1][0]=='$' and li[2][0]=='$'):
        result=ori(li)
    elif(li[0]=='xori' and li[1][0]=='$' and li[2][0]=='$'):
        result=xori(li)
    elif(li[0]=='beq' and li[1][0]=='$' and li[2][0]=='$'):
        result=beq(li)
    elif(li[0]=='bne' and li[1][0]=='$' and li[2][0]=='$'):
        result=bne(li)
        
    elif(li[0]=='lw' and li[1][0]=='$'):
        result=lw(li)
    elif(li[0]=='sw' and li[1][0]=='$'):
        result=sw(li)
    elif(li[0]=='jr' and li[1][0]=='$'):
        result=jr(li)
    elif(li[0]=='lui' and li[1][0]=='$'):
        result=lui(li)
    elif(li[0]=='j'):
        result=j(li)
    elif(li[0]=='jal'):
        result=jal(li)
        
    else:
        return "invalid input!"
    
    return result

def binToHex(s):
    if(s=='0000'):
        return '0'
    elif(s=='0001'):
        return '1'
    elif(s=='0010'):
        return '2'
    elif(s=='0011'):
        return '3'
    elif(s=='0100'):
        return '4'
    elif(s=='0101'):
        return '5'
    elif(s=='0110'):
        return '6'
    elif(s=='0111'):
        return '7'
    elif(s=='1000'):
        return '8'
    elif(s=='1001'):
        return '9'
    elif(s=='1010'):
        return 'a'
    elif(s=='1011'):
        return 'b'
    elif(s=='1100'):
        return 'c'
    elif(s=='1101'):
        return 'd'
    elif(s=='1110'):
        return 'e'
    elif(s=='1111'):
        return 'f'
    else:
        return 'Wrong!'


def convert16(s):
    t=''
    for i in range(0,29,4):
        t+=binToHex(s[i:i+4])
    return t
    
def main():
    while(1):
        cmd=input("input command:\n")
        if(cmd[0] == '0'):
            break
        s=assemble(cmd)
        t=convert16(s)
        print(s)
        print(t)

main()
