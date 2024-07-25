cities={'beijing':{
    'country':'China',
    'people':'2185.8 million',
    'fact':'is the capital '
},
    'dongjing':{
    'country':'Japen',
    'people':'1400 million',
    'fact':'is the capital '
},
    'paris':{
    'country':'France',
    'people':'210.3 million',
    'fact':'is the capital '
},
}
for city,info in cities.items():
    print(f"{city} have {info['people']} people,it {info['fact']} of {info['country']}")