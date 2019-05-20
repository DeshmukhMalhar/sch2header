import re
sch_file = "kicad-project/USBtiny_custom/USBtiny_custom.sch"
netlist = "kicad-project/USBtiny_custom/USBtiny_custom.net"

lines = list(open(netlist))
for line in lines:
    if(re.match("[\s]*\(comp \(ref [a-zA-Z]+[1-9]+\)", line)):
        print(line)
        # if(re.match("", line.__next__))
