# Python program to remove all duplicates words from a given sentence

s = "I  learn  Python  from  LetsUpgrad  and  Java  aslo  from  LetsUpgrad"
l = s.split()
k = [ ]
for i in l:

    # if condition is used to store unique string in another list 'k'
    if(s.count(i) > 1 and (i not in k) or s.count(i) == 1):
        k.append(i)
print(' '.join(k))
