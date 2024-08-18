# User Input Validation Module v4

This Python module simplifies user input validation in projects by enhancing the functionality of the standard input() function. 

This module provides functions to validate binary choices, file paths, integer ranges, and list selections.

## Installation

To use this module, clone the repository and use the module directly in your Python scripts:


```bash
git clone https://github.com/alexfortmann/user-input-validation-module.git
```

After cloning, you can directly import and use the module in your Python scripts. Make sure your script is located in the same directory as the module, or adjust the import path accordingly.
## Usage

Here’s how you can use the module in your project:

```python
from user_input_validation import user_bool, user_file, user_int, user_list, 

continue_game = user_bool("Would you like to continue? (1) Yes (2) No")
file_path = user_file("Enter the path to your file:")
age = user_int("Enter your age:", 0, 120)
color = user_list("Choose your favorite color:", ['Red', 'Blue', 'Green'])
```

## Erorr Feedback
In all cases of invalid input, the functions will loop until valid input is provided:

### user_bool:
```
Would you like to continue? (1) Yes (2) No
4

Invalid response, please enter '1' or '2' for the prompt.

Would you like to continue? (1) Yes (2) No
```
### user_file:
```
Enter the path to your file:
asdf

File could not be loaded. Please double check the directory and filename.
Input Format: file.txt or folder/file.txt

Enter the path to your file:
```
This function will output the following message if the file is able to be opened:
```
test.txt opened successfully
```

### user_int:
```
Enter your age:
500

Invalid response, please enter an integer between 0 and 120.

Enter your age:
```
### user_list:
```
Choose your favorite color:
['Red', 'Blue', 'Green']
asdf

Invalid response, please enter one of the below options:

Choose your favorite color:
['Red', 'Blue', 'Green']
red

Invalid response, please enter one of the below options:

Choose your favorite color:
['Red', 'Blue', 'Green']
```
Note: The input must *exactly* match the string representation of the desired list element, including capitalization.

## Features
- Validate a binary choice with '1' or '2'.
- Validate and open a file path.
- Validate an integer within a specific range.
- Validate a selection from a list of options.


## License
There is currently no license for this project. But I am planning to update it with one in the future.

## Author
Written by Alex Fortmann.

Version 4.0. - Copyright (c) 2024 Alex Fortmann. All rights reserved.