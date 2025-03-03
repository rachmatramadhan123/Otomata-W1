import re

def binarystring(s):
  
    return all(char in '01' for char in s)

def arithmeticex(s):
  
    pattern = re.compile(r'^[\d+\-*/\s\(\)]+$')
    return bool(pattern.match(s))

def main():
    binary_input = input("Masukkan string binary untuk validasi")
    if binarystring(binary_input):
        print(f"'{binary_input}' adalah bilangan biner")
    else:
        print(f"'{binary_input}' bukan bilangan biner")

    arithmetic_input = input("Masukkan string aritmatika untuk validasi ")
    if arithmeticex(arithmetic_input):
        print(f"'{arithmetic_input}' adalah ekspresi aritmatika")
    else:
        print(f"'{arithmetic_input}' bukan ekspresi aritmatika")

if __name__ == "__main__":
    main()
