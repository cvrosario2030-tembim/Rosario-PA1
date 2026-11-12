def display_playlist():
    songs = ["Heather", "P.S ILOVE YOU", "bdkmv"]

    print("\n===== MY PLAYLIST =====")
    for number, song in enumerate(songs, start=1):
        print(f"{number}. {song}")
