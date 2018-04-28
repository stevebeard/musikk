#!/usr/bin/env python3
import argparse
import os
import pathlib
import sys

import player

def main():
    parser = argparse.ArgumentParser(
        prog='Musikk',
        description='A simple command line music player.'
    )
    parser.add_argument('uri')
    args = parser.parse_args()
    # print(args)
    uri = pathlib.Path(os.path.abspath(args.uri)).as_uri()
    p = player.Player()
    p.play_uri(uri)
    running = True
    while running:
        command = input()
        if command is 'q':
            print('Quitting...')
            p.close()
            running = False
        else:
            print('Unrecognised Command: ' + command)

if __name__ == '__main__':
    main()