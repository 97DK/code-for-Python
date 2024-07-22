namelist=['Tom','jackey','John','admin','linda']
if namelist:
    q=len(namelist)
    for i in range(0,len(namelist)):
        namelist.pop()
    print("We need to find some users!")
else:
    print("We need to find some users!")