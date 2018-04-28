# musikk

A simple python music player.

**musikk_cli** is a command line interface for musikk.

## Installation

`python3 setup.py install --user`

## Usage

`./bin/musikk_cli path/to/audiofile.mp3`

Supported commands:
* quit
* play
* pause
* stop

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Running tests

`python3 -m unittest discover -s musikk/test/ -p 'test_*.py' -v`

There is also a bash script for those on \*nix systems: `./test_all.sh`

## License

MIT License
