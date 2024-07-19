namelist=['Tom','Jneey','Black']
print("Black couldnot participate the party")
newnamelist=[]
for i in namelist:
    if i!='Black':
        newnamelist.append(i)
    else:
        newnamelist.append('Jack')
for i in newnamelist:
    print(f"{i},Do you have time to my party this Friday?")