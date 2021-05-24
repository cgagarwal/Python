# mode ('r','a','w','r+','a+','w+','rb','wb','w+b')   b for binary

f = open("name_of_file.format" , 'mode')

print(f.read())               # reads the file
print(f.read(i))              # reads i bytes of file
print(f.tell())               # tells the positon of cursor
f.seek(i)                     # cursor goes on i position
print(f.readline())           # reads only one line
f.write("cool")               # use for writing

# reads the file  ('r')
''' file not exist ; then error
  opens file in read mode   '''

# write mode    ('w')
''' file not exist  ; then creates a new one
  remove the previous and write new '''

# append mode   ('a')
''' file not exist ; then creates
  append always at last independent of cursor '''

# append and read ('a+')
'''  cursor at last so read nothing 
  seek at 0 position to read   '''

# write and read ('w+')
''' delete old content then write and read  '''

# read and write ('r+')
''' old content dosen't deletes '''

f.close()         # close the file
