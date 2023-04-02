import tekore as tk

with open("client_nums.txt", "r") as client_nums:
    lines = client_nums.readlines()
    lines = [line.rstrip() for line in lines]

user_id = "https://open.spotify.com/user/2153lsupa5hschcs774poensq?si=765b0985ebdc45c1"
user_id_cut = user_id[30:55]

client_id = lines[0]
client_secret = lines[1]
redirect_uri = "https://github.com/Owl1y/playlist-added-by-counter"
conf = (client_id, client_secret, redirect_uri)

scoped = tk.scope.playlist_read_collaborative + tk.scope.playlist_read_private + tk.scope.playlist_modify_public
token = tk.prompt_for_user_token(*conf, scope=scoped)

client = tk.Spotify(token)
playlist = client.playlists(user_id_cut)


def get_song_ids(the_playlist):
    song_ids = []
    play_offset =0 
    
    playlist_songs = client.playlist_items(the_playlist, as_tracks=False, offset=play_offset)
    full_list = playlist_songs.total

    while full_list != len(song_ids):
        for songs in playlist_songs.items:
            song_id = songs.track.uri
            added_by = songs.added_by.id
            song_ids.append(added_by)
            #print(song_id)
        play_offset+=100
        playlist_songs = client.playlist_items(the_playlist, as_tracks=False, offset=play_offset)
    return song_ids

# former_playlist = ['7IHZvZIusTuJNMcKleSWwd', 
#                    '6fYjLM7ESHGrh5N9SvzVGB', 
#                    '77sj0Sh0vzMlWnV7SlqkLu', 
#                    '40daaNzvSSvYGIZhqX7HsR', 
#                    '26ZzwXAOlKTvsVjQcQd4gm', 
#                    '7jXzoKibDwt7yYaoU3uPdF', 
#                    '0AFQ3bdD6zCyXda4FOwp39']

current_playlist = ['26ZzwXAOlKTvsVjQcQd4gm']

names = {
        "2153lsupa5hschcs774poensq" : "Ali",
        "lozanoronald2004" : "Ronald",
        "fi70qkp91x0qjkiimbdvjiqy8" : "Jordi",
        "clashlord1115" : "Richard"
        }

current_pl_uris = get_song_ids(current_playlist[0])

# print(current_pl_uris)
print()
print()
print()

name_list = [names[id] for id in current_pl_uris]
ali = name_list.count("Ali")
ronald = name_list.count("Ronald")
jordi = name_list.count("Jordi")
richard = name_list.count("Richard")

print(f"Ali total is {ali} \nRonald total is {ronald} \nJordi total is {jordi} \nRichard total is {richard}")
# for user_id in current_pl_uris:
#     if user_id in names:
#         print(names[user_id])
#     else:
#         print(f"No name found for user id {user_id}")


