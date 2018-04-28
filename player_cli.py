#!/usr/bin/env python3
import argparse
import os
import pathlib
import time

import player

def main():
    parser = argparse.ArgumentParser(
        prog='Musikk',
        description='A simple command line music player.'
    )
    parser.add_argument('uri')
    args = parser.parse_args()
    print(args)
    uri = pathlib.Path(os.path.abspath(args.uri)).as_uri()
    musicPlayer = player.Player()
    musicPlayer.play(uri)

    time.sleep(3)

if __name__ == '__main__':
    main()