favorite_places={"Jack":["shanghai","chongqing","xian"],
                 "Karry":['hunan','chongqing'],
                 "kiki":['zhejiang','suzhou','yunnan','hainan'],
                 'cino':["chendu"]
}
for name,place in favorite_places.items():
    print(f"{name} favorite places are:")
    if len(place)!=1:
        for i in place:
            print(i)
    else:
        print(place[0])