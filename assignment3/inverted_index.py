import MapReduce
import sys
mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document text
    docs = []
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      if docs.count(w) is 0:
        docs.append(w)
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: document id list
    mr.emit((key, list_of_values))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
