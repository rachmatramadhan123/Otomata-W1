import re

def is_binary_string(s):

    return all(char in '01' for char in s)

def is_arithmetic_expression(s):
 
    pattern = re.compile(r'^[\d+\-*/\s\(\)]+$')
    return bool(pattern.match(s))

def main():

    binary_input = input("Masukkan string untuk memeriksa apakah itu bilangan biner: ")
    if is_binary_string(binary_input):
        print(f"'{binary_input}' adalah bilangan biner")
    else:
        print(f"'{binary_input}' bukan bilangan biner")

    arithmetic_input = input("Masukkan string untuk memeriksa apakah itu ekspresi aritmatika yang valid: ")
    if is_arithmetic_expression(arithmetic_input):
        print(f"'{arithmetic_input}' adalah ekspresi aritmatika")
    else:
        print(f"'{arithmetic_input}' bukan ekspresi aritmatika")

if __name__ == "__main__":
    main()