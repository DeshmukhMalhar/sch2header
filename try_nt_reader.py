from __future__ import print_function

# Import the KiCad python helper module
import kicad_netlist_reader
import sys

xml_file = sys.argv[1]
# xml_file = 'D:\Documents\GitHub\sch2header\kicad-project\test_project_with_uC\gen_xml_netlist_output.xml'
# xml_file = xml_file.replace('\\', '/')

print(xml_file)
netl = kicad_netlist_reader.netlist(xml_file)
components = netl.getInterestingComponents()

for component in components:
    # print(type(component))
    desc = component.getDescription()
    print(desc)
