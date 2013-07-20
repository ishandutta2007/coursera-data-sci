import MapReduce
import sys
mr = MapReduce.MapReduce()

def mapper(record):
    # record: database row as list of strings
    mr.emit_intermediate(record[0],1)

def reducer(key, list_of_values):
    total = 0
    mr.emit((key, len(list_of_values)))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
