EESchema Schematic File Version 4
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
$Comp
L microcontrollers:ATtiny2313-20SU U1
U 1 1 5CEBAACE
P 3650 3200
F 0 "U1" H 3850 4250 50  0000 C CNN
F 1 "ATtiny2313-20SU" V 3300 2750 50  0000 C CNN
F 2 "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm" H 4050 4950 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2543-AVR-ATtiny2313_Datasheet.pdf" H 3650 3200 50  0001 C CNN
	1    3650 3200
	1    0    0    -1  
$EndComp
Text Label 4350 2350 0    50   ~ 0
RXD
Text Label 4350 2450 0    50   ~ 0
TXD
Text Label 4350 2550 0    50   ~ 0
WKUP0
Text Label 4350 2650 0    50   ~ 0
ENCODER_A
Text Label 4350 2750 0    50   ~ 0
SW_USR_1
Text Label 4350 2850 0    50   ~ 0
SW_USR_2
Text Label 4350 2950 0    50   ~ 0
~PPM_IN
Text Label 4350 3300 0    50   ~ 0
CMP_IN
Text Label 4350 3400 0    50   ~ 0
CMP_REF
Text Label 4350 3500 0    50   ~ 0
MOTOR_A
Text Label 4350 3600 0    50   ~ 0
MOTOR_B
Text Label 4350 3700 0    50   ~ 0
BUZZER
Text Label 4350 3800 0    50   ~ 0
MOSI
Text Label 4350 3900 0    50   ~ 0
MISO
Text Label 4350 4000 0    50   ~ 0
SCK
$Comp
L power:GND #PWR0101
U 1 1 5CEBBE3A
P 3650 4300
F 0 "#PWR0101" H 3650 4050 50  0001 C CNN
F 1 "GND" H 3655 4127 50  0000 C CNN
F 2 "" H 3650 4300 50  0001 C CNN
F 3 "" H 3650 4300 50  0001 C CNN
	1    3650 4300
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0102
U 1 1 5CEBDE39
P 3650 2100
F 0 "#PWR0102" H 3650 1950 50  0001 C CNN
F 1 "+3.3V" H 3665 2273 50  0000 C CNN
F 2 "" H 3650 2100 50  0001 C CNN
F 3 "" H 3650 2100 50  0001 C CNN
	1    3650 2100
	1    0    0    -1  
$EndComp
Text Label 2950 2350 2    50   ~ 0
~RST
$Comp
L Device:Crystal_Small Y1
U 1 1 5CEBF29F
P 2850 2850
F 0 "Y1" V 2850 2950 50  0000 L CNN
F 1 "12M" H 2800 2700 50  0000 L CNN
F 2 "Crystal:Crystal_SMD_0603-4Pin_6.0x3.5mm" H 2850 2850 50  0001 C CNN
F 3 "~" H 2850 2850 50  0001 C CNN
	1    2850 2850
	0    1    1    0   
$EndComp
Wire Wire Line
	2850 2750 2950 2750
Wire Wire Line
	2950 2950 2850 2950
$EndSCHEMATC
