# Example python script to generate a netlist from a KiCad intermediate netlist
# https://forum.kicad.info/t/automatically-generate-a-pindefs-h-header-file-for-include-in-firmware-project/17223/6?u=deshmukhmalhar
#
"""
    @package
    Generate a net list file.

    Command line:
    python "pathToFile/netlist_gen.py" "%I" "%O"
"""

from __future__ import print_function

# Import the KiCad python helper module
import kicad_netlist_reader
import sys


def find_net (ref, pin):
    for net in netlist.nets:
        for node in net.getChildren('node'):
          if node.get("node", "ref") == ref and node.get("node", "pin") == pin:
              return net
    return None


if len(sys.argv) < 2:
    print("Usage ", __file__, "<netlist.xml> <output file>", file=sys.stderr)
    sys.exit(1)


# Generate an instance of a generic netlist, and load the netlist tree from
# the command line option. If the file doesn't exist, execution will stop
netlist = kicad_netlist_reader.netlist(sys.argv[1])


# Open a file to write to, if the file cannot be opened output to stdout
# instead
if len(sys.argv) > 2:
    try:
        f = open(sys.argv[2], 'w')
    except IOError:
        e = "Can't open output file for writing: " + sys.argv[2]
        print( __file__, ":", e, sys.stderr )
        f = sys.stdout
else:
    f = sys.stdout

# Generate a YAML style netlist

components = netlist.getInterestingComponents()

f.write ('---\n' )
f.write ('components:\n' )

for comp in components:
    f.write ('  - ref: %s\n' %  comp.getRef()  )
    f.write ('    value: %s\n' % comp.getValue() )

    part = comp.getLibPart()
    f.write ('    lib: %s\n' % (comp.getLibName() ) )
    f.write ('    device: %s\n' % (comp.getPartName() ) )
    f.write ('    footprint: %s\n' % (comp.getFootprint() ) )

    pins = part.element.getChild('pins')
    if pins:
        f.write ('    pins:\n' )
        for pin in pins.getChildren():
            f.write ('     - num: %s\n' % pin.get("pin", "num") )

            anet = find_net (comp.getRef(), pin.get("pin", "num") )
            if anet:
                f.write ('       net: %s\n' % anet.get("net", "name" )  )
            else:
                f.write ('       net: _none\n' )


f.close()