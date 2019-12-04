# from __future__ import print_function

# Import the KiCad python helper module
import kicad_netlist_reader
import sys
import re
import time

test_o_file = open('d:/Documents/GitHub/sch2header/test_o_file.txt', 'w')
test_o_file.write('testWrite at: ' + str(time.localtime()))
# test_o_file.close()


if len(sys.argv) < 2:
    test_o_file.write('Too few arguments for the script')


test_o_file.write(sys.argv[1])

netl = kicad_netlist_reader.netlist(sys.argv[1])
components = netl.getInterestingComponents()

for component in components:

    # print(type(component))

    desc = component.getDescription()
    test_o_file.write(desc)
    test_o_file.write('\n')


test_o_file.close()
