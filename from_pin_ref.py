import kicad_netlist_reader
import re
import xml.etree.ElementTree as ET
import os
import datetime
import sys

try:
    netlist_xml = sys.argv[1]
except IndexError:
    print('Please provide a KiCAD xml netlist as argument')
    sys.exit()

# %% Constants
# netlist_xml = 'D:\Documents\GitHub\InteDrive\mosfet_realighn\MosfetDriverOn210404.xml'
headerfieldname = 'header'
excludelist = []


# %%
header_info = open('headerinfo.txt', 'r').read()

time_now = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

header_info = header_info + '\n\n//File Timestamp: ' + time_now


# %%
tree = ET.parse(netlist_xml)
root = tree.getroot()

# %%


def get_pin_map(root, reference, value):
    libparts = getgroupinelement(root, 'libparts')
    for libpart in list(libparts):

        aliases_list = list()

        aliases = getgroupinelement(libpart, 'aliases')
        if aliases:
            for alias in list(aliases):
                aliases_list.append(alias.text)
            if value in aliases_list:
                pin_map = list()
                pins = getgroupinelement(libpart, 'pins')
                for pin in list(pins):
                    num = pin.attrib['num']
                    pin_name = pin.attrib['name']
                    pin_map.append((num, pin_name))

        elif libpart.attrib['part'] == value:
            pin_map = list()
            pins = getgroupinelement(libpart, 'pins')
            for pin in list(pins):
                num = pin.attrib['num']
                pin_name = pin.attrib['name']
                pin_map.append((num, pin_name))

    return pin_map


def get_net_table(root, reference):

    net_table = list()
    nets = getgroupinelement(root, 'nets')
    for net in nets:
        for node in list(net):
            if node.attrib['ref'] == reference:
                net_table.append((node.attrib['pin'], net.attrib['name']))

    return net_table


def getgroupinelement(element, grouptag):

    for group in list(element):
        if group.tag == grouptag:
            return group

# %%


components = getgroupinelement(root, 'components')

for component in list(components):

    ref = component.attrib['ref']

    valuetag = getgroupinelement(component, 'value')
    value = valuetag.text

    fields = getgroupinelement(component, 'fields')
    if fields:
        for field in list(fields):
            if field.attrib['name'] == headerfieldname:
                # if we get here, that means the header file for the part has to be generated
                # Let us write a method to get the header file generated right here
                headerfilename = field.text

                pin_map = get_pin_map(root, ref, value)
                net_table = get_net_table(root, ref)
                # print(pin_map, net_table)

                complete_list = list()
                for pin, name in pin_map:
                    for pin_net, net in net_table:
                        if pin == pin_net:
                            complete_list.append((pin, name, net))

                # print(complete_list)

                formatted_list = list()
                for reln in complete_list:
                    pin_name = reln[1].replace('/', '')
                    pin_name = re.sub('(~.+~/) |(~.+~)|(~)|RESET', '', reln[1])

                    pin_value = re.sub('(~.+~/) |(~.+~)|(~)', '', str(reln[2]))

                    formatted_list.append((reln[0], pin_name, pin_value))
                # print(formatted_list)
                with open(headerfilename, 'w+') as header_file:
                    header_file.write(str(header_info))
                    header_file.write('\n\n\n')
                    for pin_num, pin_name, pin_net in formatted_list:
                        if re.match('^/.+', str(pin_net)):
                            write_net = re.sub('/', '', str(pin_net))
                            write_name = re.sub(
                                'XTAL./|/XTAL.|\(.*\)', '', str(pin_name))
                            write_name = re.sub('/.*', '', write_name)
                            write_num = '//' + pin_num

                            out_str = '#define ' + write_net + ' ' + write_name + ' ' + write_num + '\n'
                            header_file.write(str(out_str))
                    # for pin_num, pin_name, pin_net in formatted_list:

                header_file.close()
                # print(formatted_list)

            # else:
            #     print(
            #         'There are no components in the design with header file field. \
            #             \nPlease check your schematic')
