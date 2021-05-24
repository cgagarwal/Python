a = 'wELcome'

a.upper()    # WELCOME
a.lower()    # welcome
a.replace("e" , 'r')    # wElcomr (not E only e)

a = '  heelo nf  '
print(a.strip())    # heelo nf      (remove unwanted space before/after text)


# Dictionary Order

print('a' > 'b')     # False
print('asd' < 'az')  # True

print('a' > 'A')      # True (ASCII)

''' ASCII       A (65)  ; a (97)   '''

a = ord('c')        # 99  ; ASCII value of c
b = chr(98)         # b   ; ASCII at 98

print(str.isalnum())        #   a-z , A-Z , 0-9
print(str.isalpha())        #   a-z , A-Z
print(str.isdigit())        #   0-9
print(str.islower())        #   a-z
print(str.isupper())        #   A-Z
