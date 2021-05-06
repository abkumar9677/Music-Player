# Importing Necessary Modules
import pygame
from tkinter.filedialog import askdirectory
import os
import tkinter as tkr

# creating window (interface) for player

musicplayer = tkr.Tk()

# setting dimensions of tkinter window

musicplayer.geometry('450x350')
# adding title for interface

musicplayer.title("Music Player")

# askdirectory() prompt the user to choose a
# directory(music directory)

directory = askdirectory()

# os.chdir() method in python is used to change the
# current working directory to specified path.
# It takes only a single argument as new directory path

os.chdir(directory)

# os.listdir() returns a list containing the names of the
# entries in the directory given by path.
songlist = os.listdir()

playlist = tkr.Listbox(musicplayer, font="Cambria 14 bold", bg="cyan2", selectmode=tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1
pygame.init()
pygame.mixer.init()
