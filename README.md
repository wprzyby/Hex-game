# Hex

## Description
An implementation of Hex game for a programming basics course project at Warsaw University of Technology.

## State of the project
Fully functional GUI with setup screen allowing to choose board radius and player names. Contains documentation and pytest unit tests. Files with .ui extension are generated via qt-designer and ui_*.py files generated using pyside2-uic tool.

## Prerequisites
The game requires PySide2 installed to run. You can install it using pip install:
```console
pip install PySide2
```

## Usage
To launch the game, open the terminal in this folder and enter the command:
```console
python3 main.py
```
You can find rules of the game [here](https://en.wikipedia.org/wiki/Hex_(board_game)).


First you will see the setup screen. Here you can enter names of Player 1 and Player 2 or leave them empty if you'd like them to stay as default. The colors beside players' names are the colors of tiles of the respective players. You can also select board radius which determines the size of the board. Once you've entered all information, click 'START GAME' for the game to start.

You will see a hex grid on which the game will be player, information on which player is supposed to move and the color of the tile of said player. You can also use the restart button to run the setup again and start a new game or you can exit the game through the exit button.

To make a move, you simply doubleclick the tile you choose, it will be painted with your color and the current player will change.

The player with the red tiles aims to connect the red borders while the player with the blue tiles - the blue borders.

Once the game is over, a restart button will show up. Pressing it will cause the game to restart with players reversed, so Player Two from previous game will now move first and will have the red tile color. Board radius will remain the same. Of course you can also choose to run setup again by clicking the restart button.