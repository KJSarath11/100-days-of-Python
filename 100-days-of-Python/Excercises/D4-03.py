#treasure map
list1=["[]","[]","[]"]
list2=["[]","[]","[]"]
list3=["[]","[]","[]"]
map=[list1,list2,list3]
print('Hiding you treasure, Makr "x" on a spot')
position=input()#a5
letter=position[0].lower()
abc=["a","b","c"]
letter_index=abc.index(letter)#.index return the index value
#here the index is replaces with a,b,c instead of 0,1,2
number_index=int(position[1])-1
map[letter_index][number_index]="x"
print(f"{list1}\n{list2}\n{list3}")

