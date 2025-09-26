# asteroids

![asteroid game demo](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/YmSwzVB-691x478.gif)

Another [boot dev](https://www.boot.dev/lessons/5be3e3bd-efb5-4664-a9e9-7111be783271) project which involves building a game using pygame. [Asteroids](https://en.wikipedia.org/wiki/Asteroids_(video_game)) is a 1979 multidirectional shooter video game developed and published by Atari, Inc. for arcades; in Japan. The player controls a spaceship in an asteroid field which is periodically traversed by flying saucers. The object of the game is to shoot and destroy the asteroids and saucers while avoiding colliding with either or being hit by the saucers' counterfire.

## Learning outcome
1. Python package manager: `uv`
2. Think in OOP way: what properties and actions a class should have and perform
3. Multi-file: internal modules (constants, classes, functions) and external package (pygame)

## Prerequisites
* Python 3.10+ installed (see the bookbot project for help if you don't already have it)
* uv project and package manager
* Access to a unix-like shell (e.g. zsh or bash)

## How to clone and run it
```
# clone the project
git clone https://github.com/kaiyin5/boot-dev-asteroids.git
cd boot-dev-asteroids
# run the project
uv run main.py
```

## How to play
* Use `W` and `S` keys to move forward and backward respectively
* Use `A` and `D` keys to rotate anti-clockwise and clockwise respectively
* Use `Spacebar` to shoot