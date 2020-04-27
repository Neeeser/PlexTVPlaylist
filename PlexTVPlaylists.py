from plexapi.server import PlexServer
import random

baseurl = input("Type ip and port of your Plex server:")
token = input("Type your authentication token (https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/):")
plex = PlexServer("http://" + baseurl, token)


TVShows = []
Episodes = []
PlayList = []
fileoftvshows = open("Shows.txt", "r")

for show in fileoftvshows:
    found = plex.search(show, mediatype="show")
    TVShows.append(found[0])


for i in range(len(TVShows)):
    reversedepisodes = TVShows[i].episodes()
    reversedepisodes.reverse()
    Episodes.append(reversedepisodes)


while len(Episodes) != 0:
    show = random.randint(0, len(Episodes)-1)
    PlayList.append(Episodes[show].pop())
    if len(Episodes[show]) == 0:
        del Episodes[show]

nameofplaylist = input("Type name of playlist:")

plex.createPlaylist("Cartoons", items=PlayList)
