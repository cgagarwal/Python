# Number

x = 0 , 0.0 , 0j         # False
x = 2 , -3 , 1j , 5.4      # True

# String

x = ''                  # False
x = ' ' , 'xd'          # True

# and/or

print(x and y)        # if 'x' is False then 'x' otherwise 'y'
print(x or y)         # if 'x' is True then 'x' otherwise 'y'



# Multiline input in a single line

x , y , z = input().split()           # 1 2 3
x , y , z = input().split(',')        # 1,2,3
x , y , z = input().split('@')        # 1@2@3

a = input().split()                         #  list
li = [int(x) for x in input().split()]      # integer inputbin single line
