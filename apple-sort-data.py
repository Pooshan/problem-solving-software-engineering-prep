# Let's say you have a CSV datafile:

# dataFile="""
# "entry1",2,3.6
# "boots",5,1.7
# "slack",1,2.6
# "triffid",11,-1.5
# """

# The data needs to be sorted numerically  by the second column. 
# How would you go about sorting the entries and dumping the
# newly sorted data?

# entry1, boots, slack, triffid
# 2        5        1    2.6
# 3.6       1.7    2.6    -1.5

# output 

# entry1, boots, slack, triffid
# 3.6       1.7    2.6    -1.5
# 2        5        1    2.6

# datafile = 
    # "slack",1,2.6
    # "entry1",2,3.6
    # "boots",5,1.7
    # "triffid",11,-1.5
    

# Steps: 
# interate csv file, 
# second colum sort data accd
# yild result 

deliminiter = ","
result = []
def sort_csv(datafile):
    for line in datafile:
        # word = line.split(deliminiter)
        sorted1 = sorted(line, key=lambda raw: int(raw[1]))
    for raw in sorted1:
        result.append(raw)
    print("sorted1---", sorted1)
        
# Let's say you have string variable with this input data; forget about csv file and see if you can solve it.

def my_sort(line):
    line_fields = line.strip().split(",") 
    amount = int(line_fields[2])
    return amount 

for line in datafile:
    line.sort(my_sort(line))


        
        
    
