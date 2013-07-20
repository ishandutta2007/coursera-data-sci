import MapReduce
import sys

"""
multiply AxB
N and L are hard-coded cons. but should be vars.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
    if matrix == "a":
        for k in range(0,5):
            mr.emit_intermediate((row,k),("a", row,col,val))
    if matrix == "b":
        for k in range(0,5):
            mr.emit_intermediate((k,col),("b", row,col,val))

def reducer(key, list_of_values):
    sum = 0
    print (key, list_of_values)
    r = key[0]
    c = key[1]
    row = [0,0,0,0,0] 
    col = [0,0,0,0,0]
    
    for j in range(0,5):
        for t in list_of_values:
            if t[0] != "a":
                break;
            if t[2] is j:
                row[j]=t[3]
                break;

    for k in range(0,5):
        for t in reversed(list_of_values):
            if t[0] != "b":
                break;
            if t[1] is k:
                col[k]=t[3]
                break

    print str(row)
    print str(col)

    for m in range(0,5):
        sum+=row[m]*col[m]

    mr.emit((key[0], key[1], sum))
            
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
