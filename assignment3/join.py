import MapReduce
import sys
mr = MapReduce.MapReduce()

def mapper(record):
    # record: database row as list of strings
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    if len(list_of_values) is 1:
        return;
    tables = {}
    for r in list_of_values:
        if r[0] not in tables.keys():
            tables[r[0]]=[r]
        else:
            tables[r[0]].append(r)

    t1 = tables[tables.keys()[0]]
    #print str(t1)
    t2 = tables[tables.keys()[1]]
    #print str(t2)
    output = []

    for row in t1:
        for _row in t2:
            mr.emit(_row+row)

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
