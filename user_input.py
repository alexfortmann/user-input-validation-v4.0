"""
User Input Validation Module v4.0 - updated 8/17/2024

Version 4.0. - Copyright (c) 2024 Alex Fortmann. All rights reserved.

This module simplifies user input validation.

It provides functions for user input validation, including:

- user_bool: Validate a binary choice by entering '1' or '2'.
- user_file: Validate a filepath to a file.
- user_int: Validate an integer within a specific range.
- user_list: Validate selection from a list of options.
"""

from pathlib import Path

def user_bool(prompt: str):
    """
    Validate a binary choice by entering '1' or '2'.

    Args:
        prompt (string): The message printed to the user to prompt 
                         choosing a binary option.

                         Ex. "Would you like to continue? 
                             (1) Yes
                             (2) No"
    Returns:
        bool: Either True or False depending on if the user 
              enters '1' or '2'.
    """
    valid = False
    error_message = ("\n" 
                    + "Invalid response, "
                    + "please enter '1' or '2' for the prompt.")
    
    while not valid:
        user_response = input("\n" + prompt + "\n")
        if user_response == str(1):
            valid = True
            return True
        elif user_response == str(2):
            valid = True
            return False
        else: print(error_message)


def user_file(prompt: str):
    """
    Validate a valid filepath to a file. 
    
    It is intended to be followed by another function that actually 
    opens/accesses the file, knowing that the filepath is valid.

    Args:
        prompt: The message printed to the user to prompt 
                entering a filepath.
    
    Returns:
        string: The validated filepath to a file.
    """
    valid = False
    error_message = ("\n" + "File could not be loaded. "
                    + "Please double check the directory and filename." 
                    + "\n"
                    + "Input Format: file.txt or folder/file.txt")
    
    while not valid:
        input_path = Path(input("\n" + prompt + "\n"))
        if input_path.is_file():
            try:
                with open(input_path, 'r') as f:
                    print(str(input_path) + " opened successfully")
                    valid = True
            except IOError:
                print(str(input_path) + " exists, but could not be opened.")
        else:
            print(error_message)
    return str(input_path)


def user_int(prompt: str, start: int, end: int):
    """
    Validate an integer within a specific range.

    Args:
        prompt (str): The message printed to the user to prompt
                      choosing an integer.
        start (int): The lower bound of the range.
        end (int): The upper bound of the range.
    
    Returns:
        int: The integer value from the user.
    """
    valid = False
    error_message = ("\n" 
                    + "Invalid response, please enter an integer between " 
                    + str(start) + " and " + str(end) + ".")
    
    while not valid:
        user_response = input("\n" + prompt + "\n")
        try:
            int_value = int(user_response)
        except ValueError:
            print(error_message)
            continue
        if int_value >= start and int_value <= end:
            valid = True
            return int_value
        else: print(error_message)


def user_list(prompt: str, choice_list: list):
    """
    Validate selection from a list of options.

    Args:
        prompt (string): The message printed to the user to 
                         prompt choosing an integer.
        choiceList (list): The list of options for the user 
                           to select from.
    
    Returns:
        any: The element selected by the user, 
             based on the element's string representation.
    """
    valid = False
    error_message = ("\n" 
                    + "Invalid response, "
                    + "please enter one of the below options:")
    
    while not valid:
        user_response = input("\n" + prompt + "\n" 
                              + str(choice_list) + "\n")
        for option in choice_list:
            if user_response == str(option):
                valid = True
                return option
        print(error_message)