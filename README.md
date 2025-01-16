# Tic-Tac-Toe

## Overview
This is an implementation of the classic game Tic-Tac-Toe on the command line for two players, including an AI option.

## Requirements
- Implemented in Python.
- Use object-oriented programming.
- Design according to the Model View Presenter (MVP) architectural pattern.
- Ability to save the current game state to a file and load the game state when opening the game.
- A second game mode to play against a game AI, using either your own heuristics or the minimax algorithm.
- Unit tests for the business logic including the game AI with at least 90% test coverage.
- Adherence to the Python PEP8 coding style guide and use of a linter.
- Use https://mygit.th-deg.de to manage the codebase.

## Features
- **Two-Player Mode**: Play against a friend on the command line.
- **Save and Load**: Save the current game state and load it later.
- **Game AI**: Play against an AI, controlled either by your own heuristics or the minimax algorithm.
- **Unit Tests**: Comprehensive tests to ensure the correct functionality of the business logic.
- **PEP8-Compliant**: The code follows PEP8 guidelines for clean and readable code.

## Installation
1. Clone the repository:
    ```sh
    git clone https://mygit.th-deg.de/EddyXII/tic-tac-toe.git
    ```
2. Navigate to the project directory:
    ```sh
    cd tic-tac-toe
    ```

## Usage
1. Start the game:
    ```sh
    python app.py
    ```
2. Follow the command line instructions to play the game or load a saved game state.

## Architecture
The game is designed according to the Model View Controller (MVC) architectural pattern, which enables a clear separation of business logic (Model), user interface (View), and control (Controller).

## Game AI
The game AI can be controlled either by your own heuristics or by the minimax algorithm. The minimax algorithm ensures optimized moves by the AI.

## Tests
The business logic and game AI are comprehensively tested to achieve at least 90% test coverage. A test coverage tool is used to check and ensure the test coverage.

Enjoy playing!

