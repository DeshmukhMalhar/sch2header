#documentation https://xesscorp.github.io/kinparse/docs/_build/singlehtml/index.html

from kinparse import parse_netlist
netlist = parse_netlist('kicad-project/USBtiny_custom/USBtiny_custom.net')
print(netlist.version)
print("netlist date: "+netlist.date)
# for part in netlist.parts:
#     print(part)
# print(netlist.parts)
for net in netlist.nets:
    # print(net)
    print(netlist.pins)
    # for pin in netlist.pins:
        # print(pin)
# print(netlist.nets)
# print(type(netlist.net))