''' String  class <str> '''

# String Formatting

# Format Specifiers

'''  %s - string     ;  %d  - integer     ;  %f - float
    %r - boolean          '''

a , b , c = 'Chirag' , 2003 , 17.3
print("Hello %s to %d with %f times"% (a,b,c))      # Hello Chirag to 2003 with 17.300000 times

# Format Function

print("Hello {x} to {y}".format(y = b , x = a))     # Hello Chirag to 2003
print("Hello {} to {} with {}".format(a,b,c))       # Hello Chirag to 2003 with 17.3

print(format(12,'b'))           # binary of 12 (1100)

# F - Strings

binary = 0b101              # stores binary (5)

print(f'Hello {a} to {binary} with {binary:0b}')      # Hello Chirag to 5 with 101


# Slicing in Python
''' extracting strings and list 
    (starting : end : gap)      '''

print(a[4:9:2])       # (4 index : 8 index (9-1) : jump of 2)
print(a[1:3])         # (1 to 2) default jump 1
print(a[2:])          # from 2 to last
print(a[:7])          # from 0 to 6
print(a[::2])          # every 2 element
print(a[::-1])        # reversed
print(a[::-3])          # from last with jump 3
