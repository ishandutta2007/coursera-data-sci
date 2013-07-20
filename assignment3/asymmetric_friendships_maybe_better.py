import MapReduce
import sys
mr = MapReduce.MapReduce()

def switch(record):
    tmp = record[0]
    record[0]=record[1]
    record[1]=tmp

def mapper(record):
    if record[0]>record[1]:
        switch(record)
    mr.emit_intermediate(record[0]+'-'+record[1],1)

def reducer(key, list_of_values):
    if len(list_of_values) is 1:   
        mr.emit(key.split('-'))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
