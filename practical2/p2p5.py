animals = "herd of elephants"

seg = animals[2:2]
print("Segment is:", seg)
# a) When x and y are the same the segment is empty

seg = animals[5:1]
print("Segment is:", seg)
# b) When x is bigger than y the segment is empty

seg = animals[:4]
print("Segment is:", seg)
# c) When x is omitted it prints the first y letters

seg = animals[3:]
print("Segment is:", seg)
# d) When y is omitted it skips the first x letters then prints the remainder of the string 

seg = animals[:]
print("Segment is:", seg)
# e) When x and y are omitted the segment is the entire string