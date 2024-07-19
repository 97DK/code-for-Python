namelist=['Tom','Jneey','Black']
namelist.insert(0,'Tony')
namelist.insert(int(len(namelist)/2),'Demo')
namelist.append("Jucy")
print(namelist)
for i in range(0,6):
    if len(namelist) > 2:
        print(f"{namelist[-1]},i am so sorry that couldnot invite you to my party")
        namelist.pop()
        print(namelist)
    else:
        print(f"{namelist[0]},Do you have time to my party this Friday?")
