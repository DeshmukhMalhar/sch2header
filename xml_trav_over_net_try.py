import xml.etree.ElementTree as ET
import re

cpu_refs_list = ["U1"]
cpu_list = ["ATtiny2313V-10SU"]

netlist_xml = "kicad-project/test_project_with_uC/test_project_with_uC.xml" 
tree = ET.parse(netlist_xml)
root = tree.getroot()
# root = ET.fromstring()
print(root.tag,root.attrib)
# print(type(root.attrib))


for child_generation1 in root.getchildren():
    # print(child_generation1.tag,child_generation1.attrib)
    # print(child_generation1.tag)
    # print(type(child_generation1))
    if child_generation1.tag == "libparts":
        child_libparts = child_generation1
        # print("found libparts")
        for child_libpart in child_libparts:
            # print(child_libpart.attrib['part'])
            if child_libpart.attrib['part'] in cpu_list:
                # print("CPU LIB DEFn Found")
                child_cpu = child_libpart
                print(child_cpu.attrib)
    if child_generation1.tag == "nets":
        child_nets = child_generation1
        print("found nets")



# Generate CPU Pin Number VS Pin Name List
cpu_pin_names=[]
cpu_pin_num=[]
cpu_pin_table=[cpu_pin_num,cpu_pin_names]

for child in child_cpu.getchildren():
    if child.tag == "pins":
        for pins_tag in child:
            # print(pins_tag.attrib["num"])
            cpu_pin_num.append(pins_tag.attrib["num"])
            cpu_pin_names.append(pins_tag.attrib["name"])

print(cpu_pin_table)

#generate net name vs cpu pin numer table
net_names = []
net_cpu_pin = []
cpu_pin_net_bindings=[net_cpu_pin,net_names]
for child in child_nets.getchildren():
    if (child.tag == "net"):
        net_name = child.attrib["name"]
        if(re.match("/.+",net_name)):
            net_name = net_name.replace('/','')
            net_names.append(net_name)
            # Currently let's leave the '~' in the names, it will be helpful
            # if we generate a comment stating "this pin is inverted"
            # and the remove the '~' and generate the #define statement
            for node in child.getchildren():
                if node.tag == "node":
                    if node.attrib["ref"] in cpu_refs_list:
                        net_cpu_pin.append(node.attrib["pin"])
        

print(cpu_pin_net_bindings)
# print(len(net_cpu_pin),len(net_names))
# IMPORTANT to have len(net_cpu_pin) == len(net_names)
# for correct 1 to 1 mapping otherwise we will miss some net names or pin numbers

