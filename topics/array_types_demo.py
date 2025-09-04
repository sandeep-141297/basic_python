"""
✅ Python Array Module - Type Codes Cheat Sheet
----------------------------------------------
| Code | Type                  | Size (bytes) | Example Values                     |
|------|-----------------------|--------------|------------------------------------|
| 'b'  | Signed char (int)     | 1            | -128 to 127                        |
| 'B'  | Unsigned char (int)   | 1            | 0 to 255                           |
| 'u'  | Unicode character     | 2 or 4       | 'a', 'A', '😊'                     |
| 'h'  | Signed short (int)    | 2            | -32768 to 32767                    |
| 'H'  | Unsigned short (int)  | 2            | 0 to 65535                         |
| 'i'  | Signed int            | 4            | -2147483648 to 2147483647          |
| 'I'  | Unsigned int          | 4            | 0 to 4294967295                    |
| 'l'  | Signed long           | 4            | Same as 'i' in many systems        |
| 'L'  | Unsigned long         | 4            | Same as 'I'                        |
| 'q'  | Signed long long      | 8            | Very large int                     |
| 'Q'  | Unsigned long long    | 8            | Very large int                     |
| 'f'  | Float                 | 4            | 1.5, 3.14                          |
| 'd'  | Double (float)        | 8            | 2.718, 9.81                        |
----------------------------------------------

👉 Note: Arrays in Python's array module can only store one data type at a time.
"""

from array import *

# Signed integer array ('i')
arr_int = array('i', [1, 2, 3, 4])
print("Integer Array:", arr_int)

# Unsigned int array ('I') → only positive numbers
arr_uint = array('I', [10, 20, 30])
print("Unsigned Int Array:", arr_uint)

# Float array ('f')
arr_float = array('f', [1.5, 2.3, 3.9])
print("Float Array:", arr_float)

# Double precision float ('d')
arr_double = array('d', [2.718, 3.14159])
print("Double Array:", arr_double)

# Unicode character array ('u')
arr_char = array('u', ['a', 'b', '😊'])
print("Unicode Char Array:", arr_char)

# Signed short int ('h')
arr_short = array('h', [-300, 1000, 2000])
print("Signed Short Int Array:", arr_short)

# Unsigned short int ('H')
arr_ushort = array('H', [100, 50000])
print("Unsigned Short Int Array:", arr_ushort)

# Signed long long ('q')
arr_longlong = array('q', [-123456789, 987654321])
print("Signed Long Long Array:", arr_longlong)

# Unsigned long long ('Q')
arr_ulonglong = array('Q', [123456789, 987654321])
print("Unsigned Long Long Array:", arr_ulonglong)
