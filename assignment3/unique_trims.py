import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    id = record[0]
    seq = record[1] 
    mr.emit_intermediate("",seq[:len(seq)-10])  


def reducer(key, list_of_values):
    coursera_data_science = {}
    for seq in list_of_values:
        if seq not in coursera_data_science.keys():       
            mr.emit(seq)
            coursera_data_science[seq]=""
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
