# HW 3
In this homework, we're going to go back and practice some basisc.

We'll look at variables, functions, lists, dicts, if statements, and loops.

## Variables
- Write function create_vars that creates an integer and a string. Call _register with them.
- Write function create_list that creates a list with three integers in them. Call _register with them.
- Write function modify_list that
    1. creates a list with three integers. Call _register with it.
    2. Then add one to each item in the list. Call _register with it.
- Create function add_item_to_list that will:
    1. Start a list with 2 strings. Call _register with the list.
    2. Add another string to the list. Call _register with the list.
- Create function create_str_dict that will:
    1. Start a dict with two key/value pairs in it. The key should be a string, the value a string as well. Call _register with the dict.
    2. Add a new key/value pair to it, again both key and pair should be a string. Call _register with the dict.
- Create function create_int_dict that will:
    1. Start a dict with two key/value pairs in it. The key should be a int, the value a int as well. Call _register with the dict.
    2. Add a new key/value pair to it, again both key and pair should be a int. Call _register with the dict.
- Create function create_mixed_dict that will:
    1. Start a dict with two pairs. One with a string key and int value. The other with a int key and string value. Call _register with the dict.
    2. Add a new key/value pair to it, a float key and a list of ints as the value. Call _register with the dict.
- Create function update_dict that will:
    1. Start a dict with however many pairs of any type. Call _register with the dict.
    2. Update one value for one key in the dict. Call _register with the dict.
- Create function remove_item_dict that will:
    1. Start a dict with two pairs of any type. Call _register with the dict.
    2. Remove one key/value pair from the dict. Call _register with the dict.
- Create function build_dict that will:
    1. Create two lists. One with 3 unique strings in it, and another with three ints in it. Call _register with the both lists.
    2. Create a dict from these two lists, with the strings as keys, and ints as values. The first string should be the key for the first int, the second string for the second int, and so on. Call _register with the dict.

## Boolean Logic
- Write function called is_1 that takes an integer as a paramater, and returns True if that integer equals 1, otherwise return false.
- Write function called adds_to_10 that takes two integers as parameters, and returns True if the two add up to 10, otherwise False.
- Write function called is_even that takes an intetger, and returns True if that integer is even, otherwise False.
- Write function called is_number that takes a parameter of any type, and returns True if it is a number, otherwise False.
- Write function called is_string that takes a parameter of any type, and returns True if it is a string, otherwise False.
- Write function do_multiple_if that takes three parameters, one float, a second float, and a boolean. If that boolean is True, multiply the two numbers and return the result. If the boolean is False, just return the first number.
- Write function string_even_length that takes a string as parameter, and returns True if length is even, False otherwise.
- Write function check_type that takes a variable of any type, and returns "boolean" if it is a boolean, "string" if it is a string, "number" if it is a float or int, or "other" if it is anything else.

- Write function correct_math that takes three floats, num1, num2, and answer, and a string representing a mathematical operation, "*", "/", "+", "-". The function returns true if performing the operation with the numbers matches the answer given. Example correct_math(num1=3.1, num2=4.2, answer=7.3, operation="+") should return true, beucase 3.1+4.2 does equal 7.3. If the opreation is not recognized, you should raise a NotImplementedError error (this is a built in error).
- Write function contains_word that takes a string "sentence" and another string "needle", and returns True if the needle is in the sentence, False otherwise.
- Write function has_duplicates that takes a list of any type, and returns True if it contains any duplicates.
- Write function any_family that takes a list of type Person and returns true if any of them have the same last name.