print('\033[4mMOKEBEAST\033[0m')
print()

dict = {}
info = ['Beast name', 'Type', 'Special Move', 'HP', 'MP']

print('Enter the following details for your Mokebeast')
print()
for i in info:
  if i == 'Type':
    print(f'{i} (Air,Earth, Water, Spirit or Fire), ', end='')
  else:
    print(f'{i}, ', end='')
print()
a = input('''\033[31mEnter the details in the other above seperating each with a comma
\033[0m>> ''').split(',')

for k in a:
  dict[info[a.index(k)]] = a[a.index(k)]
  
def printer(a):
  print()
  if a['Type'].lower() == 'fire':
    print(f'''\033[31mYour beast is called{a['Beast name']}. It is a {a['Type']} beast with a special move of {a['Special Move']} with a starting HP of {a['HP']} and a starting MP of {a['MP']}''')

  elif a['Type'].lower() == 'water':
    print(f'''\033[34mYour beast is called{a['Beast name']}. It is a {a['Type']} beast with a special move of {a['Special Move']} with a starting HP of {a['HP']} and a starting MP of {a['MP']}''')

  elif a['Type'].lower() == 'air':
    print(f'''\033[0mYour beast is called{a['Beast name']}. It is a {a['Type']} beast with a special move of {a['Special Move']} with a starting HP of {a['HP']} and a starting MP of {a['MP']}''')

  else:
    print(f'''\033[36mYour beast is called {a['Beast name']}. It is a {a['Type']} beast with a special move of {a['Special Move']} with a starting HP of {a['HP']} and a starting MP of {a['MP']}''')

printer(dict)