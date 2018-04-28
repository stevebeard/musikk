#!/usr/bin/env python3
import argparse
import os
import pathlib
import sys

import player

running = True
playing = True
_player = player.Player()

def main():
    parser = argparse.ArgumentParser(
        prog='Musikk',
        description='A simple command line music player.'
    )
    parser.add_argument('uri')
    args = parser.parse_args()
    # print(args)
    uri = pathlib.Path(os.path.abspath(args.uri)).as_uri()
    _player.play_uri(uri)
    while running:
        command = input('> ')
        if command in ['q','quit']:
            print('Quitting...')
            close()
        elif command is 'p':
            if playing:
                pause()
            else:
                play()
        elif command == 'pause':
            pause()
        elif command == 'play':
           play()
        elif command in ['s', 'stop']:
            stop()
        else:
            print('Unrecognised Command: ' + command) 

def play():
    _player.play()
    global playing
    playing = True

def pause():
    _player.pause()
    global playing
    playing = False

def stop():
    _player.stop()
    global playing
    playing = False

def close():
    _player.close()
    global playing
    global running
    playing = False
    running = False

if __name__ == '__main__':
    main()