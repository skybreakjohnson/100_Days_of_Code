#!/usr/bin/env python
# coding: utf-8

# # Day 4

# In[3]:


import random

random_interger = random.randint(1, 10)
print(random_interger)


# In[4]:


import my_module
print(my_module.pi)


# In[7]:


random_float = random.random()
print(random_float)


# In[8]:


random_float * 5


# In[10]:


love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')


# In[11]:


import random

coin = random.randint(0, 1)

if coin == 1:
  print('Heads')
else:
  print('Tails')


# In[20]:


import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(names)
all_names = len(names)
random_number = random.randint(1, all_names - 1)
random_name = names[random_number]
print(f'{random_name} is going to buy the meal today!')

# Same as: random name = random.choice(names)


# Lists

# In[2]:


states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])
print(states_of_america[-1])


# In[3]:


states_of_america[1] = 'Pencilvania'
print(states_of_america)


# In[4]:


states_of_america.append('Angelaland')
print(states_of_america)


# In[5]:


states_of_america.extend(['Apple', 'Bill'])
print(states_of_america)


# In[21]:


# list index out of range
# print(states_of_america[90]) 

# Anzahl der Elemente in der Liste
num_of_states = len(states_of_america)

# Anzahl der Elemente in der Liste minus 1 = letzte Element der Liste
print(states_of_america[num_of_states -1])

print(states_of_america[num_of_states -5])


# nested lists 

# In[19]:


# dirty_dozens = ['Strawberries', 'Spinach', 'Kale', 'Nectarines','Apples','Grapes','Peaches','Cherries','Pears','Tomatoes','Celery','Potatoes']
# print(dirty_dozens)

fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery','Potatoes']

dirty_dozens = [fruits, vegetables]
print(dirty_dozens)

# print erste Liste
print(dirty_dozens[0])

# print zweite Liste
print(dirty_dozens[1])

# print zweite Element in zweite Liste
print(dirty_dozens[1][1])


# In[ ]:


# 🚨 Don't change the code below 👇
row1 = ["⬜","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
'''
column = int(position[0])
row = int(position[1])

# map[column, row]

if column == 1 and row == 1:
  mark = map[0][0] = 'x'
elif column == 1 and row == 2:
  mark = map[1][0] = 'x'
elif column == 2 and row == 2:
  mark = map[1][1] = 'x'
elif column == 1 and row == 3:
  mark = map[2][0] = 'x'
elif column == 3 and row == 1:
  mark = map[0][2] = 'x'
elif column == 2 and row == 3:
  print('spalte: ', column)
  print('zeile: ', row)
  mark = map[2][1] = 'x'
elif column == 3 and row == 2:
  mark = map[1][2] = 'x'
elif column == 3 and row == 3:
  mark = map[2][2] = 'x'
else:
  print('suck my dick')
'''

horizontal = int(position[0])
vertical = int(position[1])

if horizontal == 1 and vertical == 1:
  mark = map[0][0] = 'x'
elif horizontal == 1 and vertical == 2:
  mark = map[1][0] = 'x'
elif horizontal == 2 and vertical == 2:
  mark = map[1][1] = 'x'
elif horizontal == 1 and vertical == 3:
  mark = map[2][0] = 'x'
elif horizontal == 3 and vertical == 1:
  mark = map[0][2] = 'x'
elif horizontal == 2 and vertical == 3:
  mark = map[2][1] = 'x'
elif horizontal == 3 and vertical == 2:
  mark = map[1][2] = 'x'
elif horizontal == 3 and vertical == 3:
  mark = map[2][2] = 'x'
else:
  print('suck my dick')



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


# In[ ]:


row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

