#documentation https://xesscorp.github.io/kinparse/docs/_build/singlehtml/index.html

from kinparse import parse_netlist

netlist = parse_netlist('kicad-project/test_project_with_uC/test_project_with_uC.net')

print(netlist.version)
print("netlist date: "+netlist.date)

cpu_refs = ['U1']
cpu_values = []

for part in netlist.parts:
    if part.ref in cpu_refs:
        cpu_values.append(part.value)

print(cpu_values)

print(netlist.nets)