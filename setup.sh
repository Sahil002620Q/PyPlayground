#!/bin/bash

# This finds exactly where your file is on the user's computer
FILE_PATH="$(pwd)/tea.py"

# This adds the custom 'py-' command to their terminal settings
echo "alias tea-='python3 tea.py $FILE_PATH'" >> ~/.bashrc
echo "alias tea-='python3 tea.py $FILE_PATH'" >> ~/.zshrc

echo "alias dice-='python3 dice.py $FILE_PATH'" >> ~/.bashrc
echo "alias dice-='python3 dice.py $FILE_PATH'" >> ~/.zshrc

echo "alias bomb-='python3 bomb2.py $FILE_PATH'" >> ~/.bashrc
echo "alias bomb-='python3 bomb2.py $FILE_PATH'" >> ~/.zshrc

echo "Done! Restart your terminal or type 'source ~/.bashrc' to start using 'py-'"
