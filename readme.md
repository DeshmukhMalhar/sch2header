# Generate pin definition header file form KiCAD schematic #
The firmware of microcontroller used has to have the correct pins connected to the peripherals in it. This project tries to automatically generate a pindefinitions.h file. This file can be included to your firmware project directly. The net names assigned to the pins in the schematic are #define*d* with actual pin names in the symbol library. So you can assign sensible names to pins and automagically use those in you code.
Generally, this is done manually, which might introduce errors.
Thus, this effort of automating it.

## SCOPE: ##
- Try to generate pindefs.h completely automatically
- try to integrate it in CI, i.e. when pushed, trigger build to generate pindefs.h
- maybe, in KiCAD 6, this can be run on exit of the sch editor, or on run of netlist generator.
- Currently in KiCAD 5.1.x , if possible I will try to make it a BOM script.(it might be possible more than I think)
