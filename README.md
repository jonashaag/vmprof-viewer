# vmprof-viewer
Standalone vmprof profile viewer

## Install instructions

    git submodule update --init
    python setup.py install

## Usage
Create profile with vmprof:

    python -m vmprof -o test.prof <your script arguments>

View profile:

    vmprofview test.prof
