## Script for cleaning duplicates in lists

## Project Description
This Python script reads a text file with a list of contacts (names and phone numbers) and generates a new file containing the original list, but with all duplicates removed.

## Key Concepts
The main functionality of the script is based on the Python `set` data structure, which stores only unique elements. This allows to process the contact list efficiently and to automatically discard duplicate entries.

## Requirements
* Python 3.x

## How to Use the Script
1. Make sure you have a file named `contacts.txt` in the same folder as this script, with the list of contacts you wish to clean up.
2.  Execute the script from your terminal with the following command:
 ````bash
 python clean_list.py
 ````

## Result
At the end of the execution, the script will create a new file called ``clean_contacts.txt` in the same folder, containing the list of contacts without duplicate entries.
