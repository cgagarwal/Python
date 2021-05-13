# class <dict>
a = {}        # dictionary

''' store element in {'key':'value'} form
  keys are immutable and not repaeted
  if key repet then it overwrites original '''

d = {'name':'Chirag' , 'age' : 22 , 14:'cool'}

a = d['name']       # Chirag   (accessing)
d[12] = 'jhuju'       # inserting
del d[14]             # deleting

c = d.get('age')      # 22
c = d.get('gur')        # None

b = d.values()        # dict_values([  ])
b = d.keys()           # dict_keys([  ])
d.clear()             # clears the dict
