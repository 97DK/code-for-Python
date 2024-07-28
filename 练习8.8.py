def make_album(singer,album,songs='None'):
    dict={'singer':singer,'album':album,}
    return dict
a=b=' '
while 1:
    if a !='q' or b !='q':
        a=input("请输入歌手名字,输入q停止:")
        b=input("请输入专辑名称,输入q停止:")
    else:
        break
album_info=make_album(a,b)
print(album_info)