# test case
songs = [('Roar', 4.4, 4.0), ('Sail', 3.5, 7.7),
         ('Timber', 5.1, 6.9), ('Wannabe', 2.7, 1.2)]
max_size = 11
songs1 = [('Roar', 4.4, 4.0), ('Sail', 3.5, 7.7),
          ('Timber', 5.1, 6.9), ('Wannabe', 2.7, 1.2)]


def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    out = []
    cursize = 0
    lieder = songs[:]
    # check first song if it fits add
    if lieder[0][2] <= max_size:
        add = lieder.pop(0)
        out.append(add[0])
        cursize += add[2]
    # if first doesnt fit return empty list
    else:
        return []
    # for other songs find smallest song in size and try to add it to out
    for lied in range(len(lieder)):
        # get sizes
        sizes = []
        for lied in lieder:
            sizes.append(lied[2])
        # get min from sizes
        minimum = min(sizes)
        for lied in lieder:
            if lied[2] == minimum:
                cursize += lied[2]
                if cursize <= max_size:
                    lieder.pop(lieder.index(lied))
                    out.append(lied[0])

                else:
                    return out
    return out


print(song_playlist(songs1, max_size))
