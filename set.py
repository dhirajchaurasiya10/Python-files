
#Set        
s1={23,2,3,3,2,3,56,32,34,23,2,2}
print(s1)                           #shows repeated elements only once

#to add one element
s1.add(3333)
print(s1)

#to add more than one
s1.update([12,12,423,3423,34343])
print(s1)

#to remove
s1.remove(23)
print(s1)

#remove command removes the element only if it's present if not present it throws error
#discard-> removes the element if present if not present doesn't matter
s1.discard(12323)

# other functions such as .pop, .clear, del, intersection, union can be used
