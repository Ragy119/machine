
def Get_indexes(st,letter):
    lst=[]
    for i in range(len(st)):
        if (st[i] == letter):
            lst.append(i)
    return lst


def split_option():
    st = input("please enter the string")
    let = input("please enter the letter")
    op = int(input("if you want to split the first letter only press 1 or if you want to split as much as the letter repeated press 2"))
    
    indexes = Get_indexes(st,let)
    
    splited = []
    ln_ind = len(indexes)
    ln_st= len(st)

    if (op == 1):
        splited = [st[0:indexes[0]],st[indexes[0]+1:]]

    elif (op == 2):    
        Lst0 =[-1]
        Lst0.extend(indexes)
        Lst0.extend(ln_st)
        indexes = Lst0

        for i in range(ln_ind+1):
            splited.append(st[indexes[i]+1:indexes[i+1]])

    return splited



