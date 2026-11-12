def display_playlist():
    songs = ["Song 1", "Song 2", "Song 3"]

    print("\n===== MY PLAYLIST =====")
    for number, song in enumerate(songs, start=1):
        print(f"{number}. {song}")