# Chess Tournament Management System

## Overview

The Chess Tournament Management System is a Python-based application 
designed to manage chess tournaments. This system allows users to 
create tournaments, manage players, and track matches and rounds. 
It provides functionalities like listing all players alphabetically, 
displaying tournament details, showing players in a tournament, and 
listing all rounds and matches.

## Features

- Create and manage multiple chess tournaments
- Add and manage players
- Generate and display matches and rounds for each tournament
- Sort and display players alphabetically
- View detailed information about tournaments, including players, rounds and matches

## Installation

To set up the Chess Tournament Management System, follow these steps:

1. Clone the repository:

    ```bash
   git clone https://github.com/your-username/chess-tournament-management.git

2. Navigate to the project directory:

    ```bash
   cd chess-tournament-management

3.(Optional) Set up a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Unix or MacOS
    venv\Scripts\activate  # On Windows 

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

## Usage

To run the Chess Tournament Management System, execute the following command 
in the project directory:

    python main.py

## Documentation

- TournamentManager: Handles the creation and management of tournaments.
- PlayerManager: Manages player registration and information.
- MatchManager: Responsible for creating and managing matches.
- MenuManager: Provides a user interface for interacting with the system.
- TournamentView: Displays tournament-related information and prompts.

## Code Quality and Testing
# Generating a Flake8 Report in HTML Format

To maintain high code quality, we use flake8 for linting and checking for coding standards. You can generate a flake8 report by following these steps:
1. Install Flake8 and flake8-html (if not already installed):
   ```bash
pip install flake8 flake8-html
3. Generate the HTML Report:
    ```bash
flake8 --format=html --htmldir=flake-report
3.Access the Report:
After running the command, you'll find the HTML report in the flake8-report directory. Open the index.html file in a web browser to view the report.

## Contributing

Contributions to the Chess Tournament Management System are welcome. 
Please ensure that your code adheres to the project's coding standards 
and include tests for new features.

## Contact

For any queries or suggestions, please contact on my email adress mouhagaye94@gmail.com
