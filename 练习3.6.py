namelist=['Tom','Jneey','Black']
namelist.insert(0,'Tony')
namelist.insert(int(len(namelist)/2),'Demo')
namelist.append("Jucy")
for i in namelist:
    print(f"{i},Do you have time to my party this Friday?")