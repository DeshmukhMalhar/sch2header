import xml.etree.ElementTree as ET
import re

cpu_refs_list = ["U1", "U2"]
cpu_values = []
cpu_alias_list = []


cpu_pin_table = []

netlist_xml = "kicad-project/test_project_with_uC/test_project_with_uC.xml"
tree = ET.parse(netlist_xml)
root = tree.getroot()
# root = ET.fromstring()
# print(root.tag,root.attrib)
# print(type(root.attrib))


for child_generation1 in root.getchildren():
    # Get values of CPU parts used in the sch in a list

    # check if the child of root is tagged components
    if child_generation1.tag == "components":
        for comp in child_generation1.getchildren():
            # for every component tag pair in components list
            # if it's reference matches with the any of the
            # references given in the list of cpu references
            if comp.attrib["ref"] in cpu_refs_list:
                child_comp_cpu = comp
            # then iterate over it's parameters until
            #  the value tag is found
                for param in child_comp_cpu.getchildren():
                    # check if tag is value under childs of componenet
                    if param.tag == "value":
                        # append the value of used component to the list
                        cpu_values.append(param.text)

# completely iterate over the given tree and find all the values/alises for given CPU refs

for child_generation1 in root.getchildren():
    if child_generation1.tag == "libparts":
        child_libparts = child_generation1

        for libpart in child_libparts.getchildren():
            alias_list = []
            if libpart.tag == "libpart":
                part_name = libpart.attrib["part"]
                for parameter in libpart.getchildren():
                    if parameter.tag == "aliases":
                        child_aliases = parameter
                        for alias in child_aliases.getchildren():
                            alias_list.append(alias.text)

            for value in cpu_values:
                cpu_pin_names = []
                cpu_pin_num = []
                if value in alias_list or value == part_name:
                    child_cpu_libpart = libpart
                    for parameter in child_cpu_libpart.getchildren():
                        if parameter.tag == "pins":
                            pins = parameter
                            for pin in pins.getchildren():
                                cpu_pin_names.append(
                                    pin.attrib["name"])
                                cpu_pin_num.append(pin.attrib["num"])
                    cpu_pin_table.append([cpu_pin_num, cpu_pin_names])

print(cpu_pin_table)
print("\n\n\n")
net_table = []


# ERROR : There is no any corelation between cpu pin table and net table
# Find something to bind those correctly together
for child_generation1 in root.getchildren():
    if child_generation1.tag == "nets":
        nets = child_generation1
        for ref in cpu_refs_list:
            # for value in cpu_values:
            net_names = []
            net_cpu_pin = []
            for net in nets.getchildren():
                if(net.tag == "net"):
                    if re.match("/.+", net.attrib["name"]):
                        for node in net.getchildren():
                            if node.attrib["ref"] == ref:
                                net_cpu_pin.append(node.attrib["pin"])
                                net_name = net.attrib["name"]
                                net_name = net_name.replace('/', '')
                                net_names.append(net_name)
            net_table.append([net_cpu_pin, net_names])
print(net_table)

# for child in child_nets.getchildren():
#     if (child.tag == "net"):
#         net_name = child.attrib["name"]
#         if(re.match("/.+", net_name)):
#             net_name = net_name.replace('/', '')
#             net_names.append(net_name)
#             # Currently let's leave the '~' in the names, it will be helpful
#             # if we generate a comment stating "this pin is inverted"
#             # and the remove the '~' and generate the #define statement
#             for node in child.getchildren():
#                 if node.tag == "node":
#                     if node.attrib["ref"] in cpu_refs_list:
#                         net_cpu_pin.append(node.attrib["pin"])


# # print(cpu_pin_net_bindings)
# # print(len(net_cpu_pin),len(net_names))
# # IMPORTANT to have len(net_cpu_pin) == len(net_names)
# # for correct 1 to 1 mapping otherwise we will miss some net names or pin numbers

#                     net_name = net_name.replace('/', '')
#                     net_names.append(net_name)
#                     # Currently let's leave the '~' in the names, it will be helpful
#                     # if we generate a comment stating "this pin is inverted"
#                     # and the remove the '~' and generate the #define statement
