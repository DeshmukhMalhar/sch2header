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
# print(root.tag, root.attrib)
# print(type(root.attrib))


for group in list(root):
    # Get values of CPU parts used in the sch in a list

    # check if the child of root is tagged components
    if group.tag == "components":
        for component in list(group):
            # for every component tag pair in components list
            # if it's reference matches with the any of the
            # references given in the list of cpu references
            if component.attrib["ref"] in cpu_refs_list:
                child_comp_cpu = component
            # then iterate over it's parameters until
            #  the value tag is found
                for parameters in list(child_comp_cpu):
                    # check if tag is value under childs of componenet
                    if parameters.tag == "value":
                        # append the value of used component to the list
                        cpu_values.append(parameters.text)

# Find the library parts group in the root
# assign the group to a variable
for group in list(root):
    if group.tag == "libparts":
        libparts = group

# For each libpart in the libparts group
for libpart in list(libparts):
    cpu_libparts = []

    if libpart.tag == "libpart":
        # Extract the part name. Do we need this ?
        part_name = libpart.attrib["part"]

        # For each parameter of the part, do
        for parameter in list(libpart):
            # Find the fields tag
            if parameter.tag == "fields":
                child_fields = parameter
                # For every field , find the field of 'Value'
                #   if the value is in the value list of CPUs to be found
                #   this is the libpart we are looking for
                #   append this to a hold list for processing
                for field in list(child_fields):

                    if field.attrib["name"] == 'Value':
                        if field.text in cpu_values:
                            cpu_libparts.append(libpart)

# For each part,which is CPu, as found in the previous loop

for cpu_libpart in cpu_libparts:
    # Hold the pin names and numbers for each cpu
    # Declared here, as for each new cpu_libpart, the lists will be cleared
    cpu_pin_names = []
    cpu_pin_num = []
    # starting with clear lists of pin name and number for each CPU
    for parameter in list(cpu_libpart):
        # Find the 'pins' section of libparts
        if parameter.tag == "pins":
            pins = parameter
            # For each pin in pins,
            #   add it's name and nuimber to respective lists
            for pin in list(pins):
                cpu_pin_names.append(pin.attrib["name"])
                cpu_pin_num.append(pin.attrib["num"])

    # Do add the lists to pin table
    # These pairs(?) are added to a table , where each vector holds "Pin Name" VS "Pin Number" of each CPU
    cpu_pin_table.append([cpu_pin_num, cpu_pin_names])

#             for value in cpu_values:
#                 cpu_pin_names = []
#                 cpu_pin_num = []
#                 if value in alias_list or value == part_name:
#                     child_cpu_libpart = libpart
#                     for parameter in list(child_cpu_libpart):
#                         if parameter.tag == "pins":
#                             pins = parameter
#                             for pin in list(pins):
#                                 cpu_pin_names.append(
#                                     pin.attrib["name"])
#                                 cpu_pin_num.append(pin.attrib["num"])
#                     cpu_pin_table.append([cpu_pin_num, cpu_pin_names])

# # print(cpu_pin_table)
# print("\n\n\n")
# net_table = []


# # ERROR : There is no any corelation between cpu pin table and net table
# # Find something to bind those correctly together
# for group in list(root):
#     if group.tag == "nets":
#         nets = group
#         for ref in cpu_refs_list:
#             # for value in cpu_values:
#             net_names = []
#             net_cpu_pin = []
#             for net in list(nets):
#                 if(net.tag == "net"):
#                     if re.match("/.+", net.attrib["name"]):
#                         for node in list(net):
#                             if node.attrib["ref"] == ref:
#                                 net_cpu_pin.append(node.attrib["pin"])
#                                 net_name = net.attrib["name"]
#                                 net_name = net_name.replace('/', '')
#                                 net_names.append(net_name)
#             net_table.append([net_cpu_pin, net_names])
# # print(net_table)

# print(cpu_pin_table[0])
# print("\n\n\n")
# print(net_table[0])
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
