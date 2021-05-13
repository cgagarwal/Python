# if - elif - else
if 4>6:
  print(12)
elif 6 > 8:   # else + if
  print(89)
else:
  print('hoye')

# while loop
x = 9
while x < 12:     # check condition
  print(x)        # exectued while true
  x += 1      # update the condition value
  
while x == 12:
  pass          # placeholder use for empty looop

while x >= 12:
  if x == 14:
    break       # breaks
  print(x)
  x += 1

while x < 18:
  x += 1
  if x == 16:
    continue
  print(x)
  
  
# Ternary Operatos  (one staement to execute)

if 4 < 6: print(6)                            # if
print(2) if 4 > 6 else print(11)              # if - else
print('gh') if 4 > 6 else print("=") if 3 == 3 else print("rk")       # if - elif - else
