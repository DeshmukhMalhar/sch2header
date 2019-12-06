EESchema Schematic File Version 4
LIBS:test_project_with_uC-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Label 3100 4250 0    50   ~ 0
~PPM_IN
Text Label 3100 4150 0    50   ~ 0
SW_USR_2
Text Label 3100 4050 0    50   ~ 0
SW_USR_1
Text Label 3100 3950 0    50   ~ 0
ENCODER_A
Text Label 3100 3850 0    50   ~ 0
WKUP0
Text Label 3100 3750 0    50   ~ 0
TXD
Text Label 3100 3650 0    50   ~ 0
RXD
Text Label 3100 3450 0    50   ~ 0
SCK
Text Label 3100 3350 0    50   ~ 0
MISO
Text Label 3100 3250 0    50   ~ 0
MOSI
Text Label 3100 3150 0    50   ~ 0
BUZZER
Text Label 3100 3050 0    50   ~ 0
MOTOR_B
Text Label 3100 2950 0    50   ~ 0
MOTOR_A
Text Label 3100 2850 0    50   ~ 0
CMP_REF
Text Label 3100 2750 0    50   ~ 0
CMP_IN
$Comp
L power:GND #PWR0101
U 1 1 5CEBBE3A
P 2500 4650
F 0 "#PWR0101" H 2500 4400 50  0001 C CNN
F 1 "GND" H 2505 4477 50  0000 C CNN
F 2 "" H 2500 4650 50  0001 C CNN
F 3 "" H 2500 4650 50  0001 C CNN
	1    2500 4650
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0102
U 1 1 5CEBDE39
P 2500 2450
F 0 "#PWR0102" H 2500 2300 50  0001 C CNN
F 1 "+3.3V" H 2515 2623 50  0000 C CNN
F 2 "" H 2500 2450 50  0001 C CNN
F 3 "" H 2500 2450 50  0001 C CNN
	1    2500 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	1900 3150 1800 3150
Wire Wire Line
	1800 2950 1900 2950
Text Label 1900 2750 2    50   ~ 0
~RST
$Comp
L MCU_Microchip_ATtiny:ATtiny2313-20SU U2
U 1 1 5CEE678D
P 2500 3550
F 0 "U2" H 2650 4600 50  0000 C CNN
F 1 "ATtiny2313-20SU" H 2450 3550 50  0000 C CNN
F 2 "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm" H 2500 3550 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2543-AVR-ATtiny2313_Datasheet.pdf" H 2500 3550 50  0001 C CNN
F 4 "header/t2313_hw.h" H 2500 3550 50  0001 C CNN "header"
	1    2500 3550
	1    0    0    -1  
$EndComp
$Comp
L MCU_Microchip_ATmega:ATmega328-MU U6
U 1 1 5CEEC004
P 7000 3550
F 0 "U6" H 7200 5000 50  0000 C CNN
F 1 "ATmega328-MU" V 6650 2950 50  0000 C CNN
F 2 "Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm" H 7000 3550 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/ATmega328_P%20AVR%20MCU%20with%20picoPower%20Technology%20Data%20Sheet%2040001984A.pdf" H 7000 3550 50  0001 C CNN
F 4 "header/m328_hw.h" H 7000 3550 50  0001 C CNN "header"
	1    7000 3550
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0103
U 1 1 5CEED34D
P 7000 2050
F 0 "#PWR0103" H 7000 1900 50  0001 C CNN
F 1 "+3.3V" H 7015 2223 50  0000 C CNN
F 2 "" H 7000 2050 50  0001 C CNN
F 3 "" H 7000 2050 50  0001 C CNN
	1    7000 2050
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0104
U 1 1 5CEEE6EA
P 7100 2050
F 0 "#PWR0104" H 7100 1900 50  0001 C CNN
F 1 "+3.3V" H 7115 2223 50  0000 C CNN
F 2 "" H 7100 2050 50  0001 C CNN
F 3 "" H 7100 2050 50  0001 C CNN
	1    7100 2050
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 5CEEEC0E
P 7000 5050
F 0 "#PWR0105" H 7000 4800 50  0001 C CNN
F 1 "GND" H 7005 4877 50  0000 C CNN
F 2 "" H 7000 5050 50  0001 C CNN
F 3 "" H 7000 5050 50  0001 C CNN
	1    7000 5050
	1    0    0    -1  
$EndComp
Text Label 7600 2850 0    50   ~ 0
SCK
Text Label 7600 2750 0    50   ~ 0
MISO
Text Label 7600 2650 0    50   ~ 0
MOSI
Text Label 7600 4150 0    50   ~ 0
TXD
Text Label 7600 4050 0    50   ~ 0
RXD
$Comp
L Device:Crystal_Small Y2
U 1 1 5CEF26EA
P 8350 3000
F 0 "Y2" V 8350 3100 50  0000 L CNN
F 1 "16M" H 8300 2850 50  0000 L CNN
F 2 "Crystal:Crystal_SMD_0603-4Pin_6.0x3.5mm" H 8350 3000 50  0001 C CNN
F 3 "~" H 8350 3000 50  0001 C CNN
	1    8350 3000
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8150 2900 8150 2950
Wire Wire Line
	8150 2950 7600 2950
Wire Wire Line
	8150 2900 8350 2900
Wire Wire Line
	7600 3050 8150 3050
Wire Wire Line
	8150 3050 8150 3100
Wire Wire Line
	8150 3100 8350 3100
$Comp
L Switch:SW_DIP_x04 SW1
U 1 1 5CEF6224
P 8900 3450
F 0 "SW1" H 8900 3917 50  0000 C CNN
F 1 "SW_DIP_x04" H 8900 3826 50  0000 C CNN
F 2 "" H 8900 3450 50  0001 C CNN
F 3 "~" H 8900 3450 50  0001 C CNN
	1    8900 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	8600 3250 7600 3250
Wire Wire Line
	7600 3350 8600 3350
Wire Wire Line
	8600 3450 7600 3450
Wire Wire Line
	7600 3550 8600 3550
Text Label 7600 3650 0    50   ~ 0
SCL
Text Label 7600 3750 0    50   ~ 0
SDA
Text Label 7600 3850 0    50   ~ 0
~RST_2
Text Label 7600 4250 0    50   ~ 0
LED_USR2
Text Label 7600 4350 0    50   ~ 0
LED_USR3
Text Label 7600 4450 0    50   ~ 0
LED_USR4
Text Label 7600 4550 0    50   ~ 0
LED_USR5
Text Label 7600 4750 0    50   ~ 0
SW_USR_3
Text Label 7600 4650 0    50   ~ 0
SW_USR_4
NoConn ~ 6400 2350
Text Label 6400 2550 2    50   ~ 0
TEMP_SEN0
Text Label 6400 2650 2    50   ~ 0
TEMP_SEN1
Text Label 7600 2450 0    50   ~ 0
MOTOR1_A
Text Label 7600 2550 0    50   ~ 0
MOTOR1_B
$Comp
L Transistor_FET:IRF540N Q1
U 1 1 5CEFB8AA
P 9750 2350
F 0 "Q1" H 9956 2396 50  0000 L CNN
F 1 "IRF540N" H 9956 2305 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 10000 2275 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf540n.pdf" H 9750 2350 50  0001 L CNN
	1    9750 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	9550 2350 7600 2350
$Comp
L power:GND #PWR0106
U 1 1 5CEFE619
P 9850 2550
F 0 "#PWR0106" H 9850 2300 50  0001 C CNN
F 1 "GND" H 9855 2377 50  0000 C CNN
F 2 "" H 9850 2550 50  0001 C CNN
F 3 "" H 9850 2550 50  0001 C CNN
	1    9850 2550
	1    0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J1
U 1 1 5CEFFBA9
P 10150 1900
F 0 "J1" H 10230 1892 50  0000 L CNN
F 1 "Screw_Terminal_01x02" H 10230 1801 50  0000 L CNN
F 2 "" H 10150 1900 50  0001 C CNN
F 3 "~" H 10150 1900 50  0001 C CNN
	1    10150 1900
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR0107
U 1 1 5CF007D1
P 9850 1800
F 0 "#PWR0107" H 9850 1650 50  0001 C CNN
F 1 "VCC" H 9867 1973 50  0000 C CNN
F 2 "" H 9850 1800 50  0001 C CNN
F 3 "" H 9850 1800 50  0001 C CNN
	1    9850 1800
	1    0    0    -1  
$EndComp
Wire Wire Line
	9950 1900 9850 1900
Wire Wire Line
	9850 1900 9850 1800
Wire Wire Line
	9950 2000 9850 2000
Wire Wire Line
	9850 2000 9850 2150
Text Label 7600 2350 0    50   ~ 0
MOSFET_GATE
$Comp
L power:GND #PWR0108
U 1 1 5CF02547
P 9300 3650
F 0 "#PWR0108" H 9300 3400 50  0001 C CNN
F 1 "GND" H 9305 3477 50  0000 C CNN
F 2 "" H 9300 3650 50  0001 C CNN
F 3 "" H 9300 3650 50  0001 C CNN
	1    9300 3650
	1    0    0    -1  
$EndComp
Wire Wire Line
	9200 3250 9300 3250
Wire Wire Line
	9300 3250 9300 3350
Wire Wire Line
	9200 3350 9300 3350
Connection ~ 9300 3350
Wire Wire Line
	9300 3350 9300 3450
Wire Wire Line
	9200 3450 9300 3450
Connection ~ 9300 3450
Wire Wire Line
	9300 3450 9300 3550
Wire Wire Line
	9200 3550 9300 3550
Connection ~ 9300 3550
Wire Wire Line
	9300 3550 9300 3650
Text Label 7600 3250 0    50   ~ 0
SW_DIP0
Text Label 7600 3350 0    50   ~ 0
SW_DIP1
Text Label 7600 3450 0    50   ~ 0
SW_DIP2
Text Label 7600 3550 0    50   ~ 0
SW_DIP3
$Comp
L Analog_ADC:MCP3204 U3
U 1 1 5D50E6C3
P 2950 6200
F 0 "U3" H 2950 6781 50  0000 C CNN
F 1 "MCP3204" H 2950 6690 50  0000 C CNN
F 2 "" H 3850 5900 50  0001 C CNN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/21298c.pdf" H 3850 5900 50  0001 C CNN
	1    2950 6200
	1    0    0    -1  
$EndComp
Text Label 1800 2950 0    50   ~ 0
X1
Text Label 1800 3150 0    50   ~ 0
X2
$EndSCHEMATC
