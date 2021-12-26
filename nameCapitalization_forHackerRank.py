
def solve (name):
    nameList = []
    for i in name:
        nameList.append (i)                                                         # append to a list charactors with spaces

    if "a" <= nameList [0] <="z":                                                   # if first letter is a letter
        nameList [0] = chr (ord (nameList [0]) - 32)                                # replace it with its capital 

    for i in range (len (name)-1):  
        if name [i] == " " and "a" <= name [i+1] <= "z":                            # if it is a 1st letter of any other word
            # print (chr (ord (name [i+1]) - 32))
            # name = name.replace (name [i+1], chr (ord (name [i+1]) - 32))
            nameList [i+1] =  chr (ord (nameList [i+1]) - 32)

    return "".join (nameList)

if __name__ =='__main__':
    # name = "132 456 Wq  m e"
    name = input ()
    print (solve (name))