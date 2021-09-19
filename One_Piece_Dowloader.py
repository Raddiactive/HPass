import anix
import modules._getch as getch
import requests
import os
import sys
import time

getch = getch._Getch()
client = anix.Client()
name = "One Piece"

with client.login(username="Raddiactive",password="alver222",remember="Yes") as login:
    cap = client.anime_last_chapter(name)
    urls = client.download_links(name=name,cap=cap)
    os.system("clear")
    for i, url in enumerate (urls.values()):
        response = requests.get(url).status_code
        if response == 200: color = "\033[1;32;40m" ; link_color = "\033[0;30;47m"
        else:color = "\033[1;31;40m" ; link_color = "\033[0;37;40m"
        server = list(urls.keys())[i]
        print(f"\n\033[0;30;46m ❮ {server} ❯ \033[0;0m " + f"{link_color} {url} \033[0;0m" + f" {color} RESPONSE ❯ {response} \033[0;0m")
    print("\n\033[1;36;40m Escoja la opción deseada mediante un número ❯ \033[0;0m");opcion = int(getch())
    opcion = str('"'+(list(urls.values())[opcion-1])+'"')
    client.open_new_incognito(navegator="google-chrome",url=opcion)
    os.system("clear")
    time.sleep(0.5)
    sys.exit(0)
