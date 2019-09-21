# %%
import xml.etree.ElementTree as ET
import re

cpu_refs_list = ["U1", "U2"]
cpu_values = []


netlist_xml = "kicad-project/test_project_with_uC/test_project_with_uC.xml"
tree = ET.parse(netlist_xml)
root = tree.getroot()
# root = ET.fromstring()
# print(root.tag, root.attrib)
# print(type(root.attrib))

# %%
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

# %%

# Find the library parts group in the root
# assign the group to a variable
for group in list(root):
    if group.tag == "libparts":
        libparts = group

# %%
cpu_pin_table_list = list()
# For each CPU in the list
for cpu_value in cpu_values:
    # Empty dict to hold the pin dict
    # Will be created for each cpu in cpu_values
    cpu_pin_table = dict()

    # For each libpart in the libparts group
    for libpart in list(libparts):
        # empty alias list for each libpart
        # If parts other than CPU have alias, we will be able to find cpus by
        #   seeing if the current cpu is in the list of aliases of current part
        #   Thus, extracting the correct pin table for the cpu

        libpart_alias_list = list()
        if libpart.tag == "libpart":
            # Extract the part name. Do we need this ?
            part_name = libpart.attrib["part"]

            # For each parameter of the part, do
            for parameter in list(libpart):
                # Find the fields tag
                if parameter.tag == "aliases":
                    parameter_aliases = parameter
                    for alias in parameter_aliases:
                        libpart_alias_list.append(alias.text)

        if cpu_value in libpart_alias_list:
            # This is a cpu we are looking at, extract the pin map
            for parameter in list(libpart):
                if parameter.tag == "pins":
                    pins = parameter
                    for pin in pins:
                        cpu_pin_table[pin.attrib['num']] = pin.attrib['name']

    cpu_pin_table_list.append(cpu_pin_table)


# %%
# print(cpu_pin_table_list)

# %%

# for table in cpu_pin_table_list:
#     print(table)
#     print('\n\n')

# %%
for group in list(root):
    if group.tag == 'nets':
        nets = group

# %%

net_table_list = list()

for cpu_ref in cpu_refs_list:
    net_table_dict = dict()

    for net in list(nets):
        net_refs = list()

        net_name = net.attrib['name']
        # If the net is user created
        if re.match("/.+", net_name):
            # Strip the leading '/'
            net_name = net_name.replace('/', '')

            # For each node on the net, get
            #   all the parts
            for node in list(net):
                net_refs.append(node.attrib['ref'])

            if cpu_ref in net_refs:
                for node in list(net):
                    if node.attrib['ref'] == cpu_ref:
                        net_table_dict[node.attrib['pin']] = net_name

    net_table_list.append(net_table_dict)

# %%
# print(net_table_list)

# # %%
# for net_table in net_table_list:
#     print(net_table)
#     print('\n\n')

# %%

pin_map_list = list()

for i in range(len(cpu_refs_list)):
    common_pins = net_table_list[i].keys() & cpu_pin_table_list[i].keys()
    # print(common_pins)
    # print(cpu_refs_list[(i)])
    pin_map = dict()
    for common_pin in common_pins:
        pin_map[cpu_pin_table_list[i][common_pin]
                ] = net_table_list[i][common_pin]

    pin_map_list.append(pin_map)

    filename = str(cpu_refs_list[i])
    file_ext = '.h'
    filename = filename + file_ext
    header_file = open(filename, 'w+')

    for pin in pin_map:
        pin_name = str(pin).replace('/', '')
        pin_name = re.sub('(~.+~/) |(~.+~)|(~)|RESET', '', pin_name)
        pin_value = re.sub('(~.+~/) |(~.+~)|(~)', '', str(pin_map[pin]))

        out_str = '#define ' + pin_value + ' ' + pin_name + '\n'

        header_file.write(out_str)

    header_file.close


# %%
# print('Printing Pin Maps')
# for pin_map in pin_map_list:
#     print(pin_map)
#     print('\n')


# %%
logfile = open('log.txt', 'w+')
for pin_map in pin_map_list:
    logfile.write(str(pin_map))
    logfile.write('\n')

logfile.close


# %%
