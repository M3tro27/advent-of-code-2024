#!/bin/bash
directory=$1

mkdir "$directory"
touch "$directory/main.py" "$directory/input.txt" "$directory/test_input.txt"
