#!/bin/bash

# This finds exactly where your file is on the user's computer
FILE_PATH="$(pwd)/tea.py"

# This adds the custom 'py-' command to their terminal settings
echo "alias py-='python3 $FILE_PATH'" >> ~/.bashrc
echo "alias py-='python3 $FILE_PATH'" >> ~/.zshrc

echo "Done! Restart your terminal or type 'source ~/.bashrc' to start using 'py-'"