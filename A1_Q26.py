#26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix
def check_prefix_suffix(s, prefix, suffix):
    
    starts_with_prefix = s.startswith(prefix)  # Check if the string starts with the given prefix
   
    ends_with_suffix = s.endswith(suffix)  # Check if the string ends with the given suffix
    
    return starts_with_prefix, ends_with_suffix


input_string = "Hello, world!"
prefix = "Hello"
suffix = "world!"

starts_with_prefix, ends_with_suffix = check_prefix_suffix(input_string, prefix, suffix)

if starts_with_prefix:
    print(f'The string "{input_string}" starts with the prefix "{prefix}".')
else:
    print(f'The string "{input_string}" does not start with the prefix "{prefix}".')

if ends_with_suffix:
    print(f'The string "{input_string}" ends with the suffix "{suffix}".')
else:
    print(f'The string "{input_string}" does not end with the suffix "{suffix}".')
