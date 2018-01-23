# HW 1 Problem 4
yours=['Yale','MIT','Berkeley']
mine=['UCLA','Yale','Harvard']
ours1=[]
ours1= mine+yours
ours2=[]
ours2.append(mine)
ours2.append(yours)

print(ours1,ours2)

yours[1]='NYU'
print(ours1,ours2)

# ours1 is a new list we created, but ours2 is depended on yours and mine two lists together.
