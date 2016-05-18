#!/usr/bin/env python

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:

    # handle changing of radio buttons
    def onToggleMP4(self, button):
        global state
        if button.get_active():
            state = 0  # mp4
        else:
            state = 1  #mp3


    # handle file chooser
    def onFile(self, button):
        global dir  # directory where file is stored
        dir = fileCH.get_filename()


    # handle download button
    def onClick(self, button):
        urlTXT.grab_focus()

        global audio  # either " " or extract audio option
        global ext    # file extension
        global state  # state of radio button
        global dir    # directory from filechooser

        if state == 0 :
            ext = ".mp4"
            audio = " "
        elif state == 1:
            ext = ".mp3"
            audio = " --extract-audio --audio-format mp3 "

        url = urlTXT.get_text()    # get url of video

        if fileTXT.get_text() == "":
            file = "%\(title\)s"
        else:
            file = fileTXT.get_text()  # get filename

        # execute youtube-dl with options and arguments from GUI
        os.system("youtube-dl -o " + dir + "/" + file + ext + audio + url + " | zenity --progress --pulsate --text='Downloading.....' --percentage=0 --auto-close")


builder = Gtk.Builder()
builder.add_from_file("/home/corey/YTDL.glade")

# reference to gui objects
urlTXT = builder.get_object("urlTXT")
fileTXT = builder.get_object("fileTXT")
fileCH = builder.get_object("fileCH")

builder.connect_signals(Handler())

# state of radio buttons initialized to mp4
global state
state = 0

window = builder.get_object("mainWND")

window.connect("delete-event", Gtk.main_quit)  # exit program
window.show_all()

Gtk.main()
