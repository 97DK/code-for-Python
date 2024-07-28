def make_album(singer,album,songs='None'):
    if songs:
        dict=dict={'singer':singer,'album':album,'songs':songs,}
    else:
        dict={'singer':singer,'album':album,}
    return dict
album_info=make_album('Jay','cc')
print(album_info)