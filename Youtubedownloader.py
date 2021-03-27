import socket as soc
import os as systemid
import pytube as pyd1
from pytube import Playlist as pyd2
import getpass
import time


#systemid.popen("pip install pytube -y")
username = getpass.getuser()

#class Dowloader(self):

def path():# file location maintainer
    default = f"/home/{username}/Downloads/YDL/"
    part_input = str(input(f"kinldy input path for download[default[{default}]]:\n> "))
    if len(part_input) == 0:
        path = default
        return path
            
    elif len(part_input) != 0:
        path = part_input + "YDL/"
        return path

def video_downloader(url): #Video downloader
    print(f"Starting downloading {url}")
    
    yt = pyd1.YouTube(url)
    stream = yt.streams.filter(res=res).first()
    outputer = stream.download(output_path=path)
    print(f"Done {url}")

            

hostname = soc.gethostname()
ipaddress_internal = soc.gethostbyname(hostname)
externalip = systemid.popen('wget -qO- http://ipecho.net/plain ; echo').readlines(-1)[0].strip()

print(f"hello {hostname},\nyour private ip is {ipaddress_internal}.\nand your public ip is {externalip}\nI hope you are a Great!!!")
try:
    URL_INPUT = str(input("Kindly provide URL of you YOUTUBE Playlist/Video:\n>>"))
    res = input("RES == resolution\n>>") + "p"
    if len(URL_INPUT) == 0:
        print("Sorry!! no Input received...")
    else:
        path = path()
        print(path)
        confirmation = str(URL_INPUT.capitalize())#https://www.youtube.com/playlist?list=PLoicwUXm27GO54OtCCVJtUXJyD-4oXgxC
        if confirmation.find("playlist") >= 0:
            PLAYLIST_Order = pyd2(URL_INPUT)
            count_of_video_urls = len(PLAYLIST_Order.video_urls)
            if count_of_video_urls !=0:
                for video_url in PLAYLIST_Order:
                    link = video_url
                    print(video_url)
                time.sleep(3)
                print(f"Number of Video URL in Playlist: {count_of_video_urls}")
                for url in PLAYLIST_Order:
                    video_downloader(url)
        elif confirmation.find("playlist") <= 0:#https://www.youtube.com/watch?v=T8g2pcgRiLI
            time.sleep(3)
            url = URL_INPUT
            video_downloader(url)
except KeyboardInterrupt as e:
    print("\nProcess cancelled by user\n")
