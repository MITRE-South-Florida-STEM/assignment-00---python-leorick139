'''
Write 6 print() statements to "draw" the following on the console

ooo/\ooo
oo/  \oo
o/ '' \o
/______\
|| || ||
xxxxxxxx

(hint: use escape sequence)
'''
line1='ooo/\\ooo'
line2='oo/  \\oo'
line3='o/ \'\' \\o'
line4='/______\\'
line5='|| || ||'
line6='xxxxxxxx'
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)

'''
Can you do it with just one print statement?
(hint: use string concatenation
'''
print('\nooo/\\ooo \noo/  \\oo\no/ \'\' \\o \n/______\\ \n|| || || \nxxxxxxxx')

'''
Choose three positive values for a, b, and c such that the final print() statement returns True
'''
a = 9
b = 12
c = 15
print(a**2 + b**2 == c**2)
