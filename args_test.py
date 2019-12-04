from __future__ import print_function
import getopt
import sys
import kicad_netlist_reader

# GET the args passed by kicad

f = open('d:/Documents/GitHub/sch2header/kicad-project/test_project_with_uC/op.txt', 'w+')

for arg in sys.argv:
    f.write(arg)
    f.write('\n')
    print(arg)

f.close()
