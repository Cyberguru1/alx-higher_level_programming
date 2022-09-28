# *More Data Structures* :joy:

**In this repository we are going into more data structures and operations on them such as :**
- 
- ## Lambda, filter, reduce and map
- ## Learn to Program 12 Lambda Map 

- ## Filter Reduce

### **[0. Squared simple](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/0-square_matrix_simple.py)**

> Write a function that computes the square value of all integers of a matrix.
1. matrix is a 2 dimensional array
2. Returns a new matrix:
3. Same size as matrix
4. Each value should be the square of the value of the input
5. Initial matrix should not be modified
6. You are not allowed to import any module
7. You are allowed to use regular loops, map, etc.

### **[1. Search and replace](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/1-search_replace.py)**

> Write a function that replaces all occurrences of an element by another in a new list.

1. Prototype: def search_replace(my_list, search, replace):
2. my_list is the initial list
3. search is the element to replace in the list
4. replace is the new element
5. You are not allowed to import any module

### **[2. Unique addition](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/2-uniq_add.py)**

> Write a function that adds all unique integers in a list (only once for each integer).

1. Prototype: def uniq_add(my_list=[]):
2. You are not allowed to import any module
   
### **[3. Present in both](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/3-common_elements.py)**

> Write a function that returns a set of common elements in two sets.

1. Prototype: def common_elements(set_1, set_2):
2. You are not allowed to import any module
   
### **[4. Only differents](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/4-only_diff_elements.py)**

> Write a function that returns a set of all elements present in only one set.

1. Prototype: def only_diff_elements(set_1, set_2):
2. You are not allowed to import any module
   
### **[5. Number of keys](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/5-number_keys.py)**

> Write a function that returns the number of keys in a dictionary.

1. Prototype: def number_keys(a_dictionary):
2. You are not allowed to import any module
   
### **[6. Print sorted dictionary](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/6-print_sorted_dictionary.py)**

> Write a function that prints a dictionary by ordered keys.

1. Prototype: def print_sorted_dictionary(a_dictionary):
2. You can assume that all keys are strings
3. Keys should be sorted by alphabetic order
4. Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
5. Dictionary values can have any type
6. You are not allowed to import any module
   
### **[7. Update dictionary](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/7-update_dictionary.py)**

> Write a function that replaces or adds key/value in a dictionary.

1. Prototype: def update_dictionary(a_dictionary, key, value):
2. key argument will be always a string
3. value argument will be any type
4. If a key exists in the dictionary, the value will be replaced
5. If a key doesn’t exist in the dictionary, it will be created
6. You are not allowed to import any module

### **[8. Simple delete by key](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/8-simple_delete.py)**

> Write a function that deletes a key in a dictionary.

1. Prototype: def simple_delete(a_dictionary, key=""):
2. key argument will be always a string
3. If a key doesn’t exist, the dictionary won’t change
4. You are not allowed to import any module
   
### **[9. Multiply by 2](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/9-multiply_by_2.py)**

> Write a function that returns a new dictionary with all values multiplied by 2

1. Prototype: def multiply_by_2(a_dictionary):
2. You can assume that all values are only integers
3. Returns a new dictionary
4. You are not allowed to import any module
   
### **[10. Best score](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/10-best_score.py)**

> Write a function that returns a key with the biggest integer value.

1. Prototype: def best_score(a_dictionary):
2. You can assume that all values are only integers
3. If no score found, return None
4. You can assume all students have a different score
5. You are not allowed to import any module

### **[11. Multiply by using map](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/11-multiply_list_map.py)**

> Write a function that returns a list with all values multiplied by a number without using any loops.

1. Prototype: def multiply_list_map(my_list=[], number=0):
2. Returns a new list:
3. Same length as my_list
4. Each value should be multiplied by number
5. Initial list should not be modified
6. You are not allowed to import any module
7. You have to use map
8. Your file should be max 3 lines
   
### **[12. Roman to Integer](https://github.com/Cyberguru1/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/12-roman_to_int.py)**


> **Technical interview preparation:**

1. You are not allowed to google anything
2. Whiteboard first
3. Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.
4. 
5. You can assume the number will be between 1 to 3999.
6. def roman_to_int(roman_string) must return an integer
7. If the roman_string is not a string or None, return 0

### **14. Squared by using map**

> Write a function that computes the square value of all integers of a matrix using map

1. Prototype: def square_matrix_map(matrix=[]):
2. matrix is a 2 dimensional array
3. Returns a new matrix:
4. Same size as matrix
5. Each value should be the square of the value of the input
6. Initial matrix should not be modified
7. You are not allowed to import any module
8. You have to use map
9. You are not allowed to use for or while
10. Your file should be max 3 lines