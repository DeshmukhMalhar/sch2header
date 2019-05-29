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
Text Label 6600 3800 0    50   ~ 0
~PPM_IN
Text Label 6600 3700 0    50   ~ 0
SW_USR_2
Text Label 6600 3600 0    50   ~ 0
SW_USR_1
Text Label 6600 3500 0    50   ~ 0
ENCODER_A
Text Label 6600 3400 0    50   ~ 0
WKUP0
Text Label 6600 3300 0    50   ~ 0
TXD
Text Label 6600 3200 0    50   ~ 0
RXD
Text Label 6600 3000 0    50   ~ 0
SCK
Text Label 6600 2900 0    50   ~ 0
MISO
Text Label 6600 2800 0    50   ~ 0
MOSI
Text Label 6600 2700 0    50   ~ 0
BUZZER
Text Label 6600 2600 0    50   ~ 0
MOTOR_B
Text Label 6600 2500 0    50   ~ 0
MOTOR_A
Text Label 6600 2400 0    50   ~ 0
CMP_REF
Text Label 6600 2300 0    50   ~ 0
CMP_IN
$Comp
L power:GND #PWR0101
U 1 1 5CEBBE3A
P 6000 4200
F 0 "#PWR0101" H 6000 3950 50  0001 C CNN
F 1 "GND" H 6005 4027 50  0000 C CNN
F 2 "" H 6000 4200 50  0001 C CNN
F 3 "" H 6000 4200 50  0001 C CNN
	1    6000 4200
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR0102
U 1 1 5CEBDE39
P 6000 2000
F 0 "#PWR0102" H 6000 1850 50  0001 C CNN
F 1 "+3.3V" H 6015 2173 50  0000 C CNN
F 2 "" H 6000 2000 50  0001 C CNN
F 3 "" H 6000 2000 50  0001 C CNN
	1    6000 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 2700 5300 2700
Wire Wire Line
	5300 2500 5400 2500
$Comp
L Device:Crystal_Small Y1
U 1 1 5CEBF29F
P 5300 2600
F 0 "Y1" V 5300 2700 50  0000 L CNN
F 1 "12M" H 5250 2450 50  0000 L CNN
F 2 "Crystal:Crystal_SMD_0603-4Pin_6.0x3.5mm" H 5300 2600 50  0001 C CNN
F 3 "~" H 5300 2600 50  0001 C CNN
	1    5300 2600
	0    1    1    0   
$EndComp
Text Label 5400 2300 2    50   ~ 0
~RST
$Comp
L MCU_Microchip_ATtiny:ATtiny2313-20SU U1
U 1 1 5CEE678D
P 6000 3100
F 0 "U1" H 6150 4150 50  0000 C CNN
F 1 "ATtiny2313-20SU" H 5950 3100 50  0000 C CNN
F 2 "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm" H 6000 3100 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2543-AVR-ATtiny2313_Datasheet.pdf" H 6000 3100 50  0001 C CNN
	1    6000 3100
	1    0    0    -1  
$EndComp
$EndSCHEMATC
