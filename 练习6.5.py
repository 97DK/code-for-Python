river={'Nile':'egypt','Changjiang':'China','Huanghe':'China'}
for k,v in river.items():
    print(f"The {k} runs through {v}.")
print("所有的河流有:")
for i in river.keys():
    print(i)
print("所有河流的流域分别为：")
for i in river.values():
    print(i)