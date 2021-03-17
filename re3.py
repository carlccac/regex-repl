from csv import reader
import re

def opn_csv(x):
    with open(x, 'r') as f:
        a = reader(f)
        b = list(a)
        return b
    
def uin_csv(): 
    uin = input('enter csv file name: ')
    return uin
    
def uin(): 
    print('enter \'r\', a space, then regex or any other key to exit ')
    uin = input(': ')
    return uin

def rx(x, y):
    for i in range(len(y)):
        a = re.finditer(x, y[i][0])
        print(i+1,': ', y[i][0], ': ', sep = '', end = '')
        for j in a: print(j.group(),' ' , j.span(), ', ' , sep ='', end = '')
        print()
            
def loop(x):
    flag = True
    while flag == True:
        inp = uin()
        if inp == '':
            flag = False
        elif inp[0] == 'r':
            rx(inp[2:], x)
            print()
        else:
            flag = False

def main():
    
    a = opn_csv(uin_csv())
    loop(a)
    
if __name__ == "__main__":
    main()
    