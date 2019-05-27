import re
sch_file = "kicad-project/USBtiny_custom/USBtiny_custom.sch"
netlist = "kicad-project/USBtiny_custom/USBtiny_custom.net"

lines = list(open(netlist))
given_id = "U1"

# convert this to a def for getting component id
which_line = 0
list_component_id = []
list_component_value = []
next_line = ""
for line in lines:
    which_line += 1
    if (re.match("[\s]*\(comp \(ref [a-zA-Z]+[1-9]+\)", line)):
        # print(line)
        groups = str.split(line)
        component_id = groups[2].replace(")", "")
        # print(component_id)
        list_component_id.append(component_id)
        next_line = lines[which_line]
        if(re.match("", next_line)):
            temp_linechars = str.split(next_line)
            component_value = temp_linechars[1].replace(")", "")
            # print(component_value)
            list_component_value.append(component_value)
list_components = [list_component_id, list_component_value]
# print(list_components)

if(given_id in list_component_id):
    where_is_IC = list_component_id.index(given_id)

given_value = list_component_value[where_is_IC]

print("FOUND: " + given_value)
where_footprint = 0
for line in lines:
    where_footprint += 1
    if(re.match(".*"+given_value+".*", line)):
        print(line)
        print("Line #: "+str(where_footprint))

fp_lib_sec_regex = "\s*\(libpart \(lib[.]*\)[.]*\(part.*\).*\n\s*\(aliases.*\n [.\n]*\)"


'''
(libpart(lib microcontrollers)(part ATtiny2313V-10SU)
 (aliases
    (alias ATtiny2313-20SU)
    (alias ATtiny2313A-SU)
  (alias ATtiny4313-SU))
'''
