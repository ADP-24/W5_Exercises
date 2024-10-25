a = "  101.1 " 
b = '55' 
c = "402 Stevens" 
d = 'Number 5  '

a_stripped = a.strip()
d_stripped = d.strip()

# a_int = int(a) # ValueError: invalid literal for int() with base 10: '  101.1 '
# b_int = int(b) # 55, 55
# c_int = int(c) # ValueError: invalid literal for int() with base 10: '402 Stevens'
# d_int = int(d) # ValueError: invalid literal for int() with base 10: 'Number 5  '

# print(a, a_int)
# print(b, b_int)
# print(c, c_int)
# print(d, d_int)

# a_float = float(a)
# b_float = float(b)
# c_float = float(c)
# d_float = float(d)

# print(a, a_float) 101.1  101.1
# print(b, b_float) 55 55.0
# print(c, c_float) ValueError: could not convert string to float: '402 Stevens'
# print(d, d_float) ValueError: could not convert string to float: 'Number 5  '

# print(int(float(a))) 101

a_numeric = int(float(a_stripped))
c_numeric_part = c[:3]
c_numeric = int(c_numeric_part)
d_numeric_part = d_stripped[-1]
d_numeric = int(d_numeric_part)

print(a_numeric, type(a_numeric))

print(f"a_stripped: '{a_stripped}', type: {type(a_stripped)}")
print(f"b: '{b}', type: {type(b)}")
print(f"c_numeric_part: '{c_numeric_part}', type: {type(c_numeric_part)}")
print(f"d_stripped: '{d_stripped}', type: {type(d_stripped)}")