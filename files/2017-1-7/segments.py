#!/usr/bin/env python
# 
# IDA Script to add new Segments
# Memory Map of Texas Instruments TM4C123G

from idautils import *
from idc import *
from idaapi import *


SEGMENT_ARCH = 32

# Not all SEGMENTS from the datasheet are here
SEGMENTS = [
# ('Start address', 'end address', 'description')
	(0x00000000, 0x0003FFFF, 'ROM'),
	(0x20000000, 0x20007FFF, 'SRAM'),
	(0x40000000, 0x40000FFF, 'Watchdog timer 0'),
	(0x40001000, 0x40001FFF, 'Watchdog timer 1'),
	(0x40004000, 0x40004FFF, 'GPIO Port A'),
	(0x40005000, 0x40005FFF, 'GPIO Port B'),
	(0x40006000, 0x40006FFF, 'GPIO Port C'),
	(0x40007000, 0x40007FFF, 'GPIO Port D'),
	(0x40008000, 0x40008FFF, 'SSI0'),
	(0x40009000, 0x40009FFF, 'SSI1'),
	(0x4000A000, 0x4000AFFF, 'SSI2'),
	(0x4000B000, 0x4000BFFF, 'SSI3'),
	(0x4000C000, 0x4000CFFF, 'UART0'),
	(0x4000D000, 0x4000DFFF, 'UART1'),
	(0x4000E000, 0x4000EFFF, 'UART2'),
	(0x4000F000, 0x4000FFFF, 'UART3'),
	(0x40010000, 0x40010FFF, 'UART4'),
	(0x40011000, 0x40011FFF, 'UART5'),
	(0x40012000, 0x40012FFF, 'UART6'),
	(0x40013000, 0x40013FFF, 'UART7'),
	(0x40020000, 0x40020FFF, 'I2C0'),
	(0x40021000, 0x40021FFF, 'I2C1'),
	(0x40022000, 0x40022FFF, 'I2C2'),
	(0x40023000, 0x40023FFF, 'I2C3'),
	(0x40024000, 0x40024FFF, 'GPIO Port E'),
	(0x40025000, 0x40025FFF, 'GPIO Port F'),
	(0x40028000, 0x40028FFF, 'PWM0'),
	(0x40029000, 0x40029FFF, 'PWM1'),
	(0x4002C000, 0x4002CFFF, 'QEI0'),
	(0x4002D000, 0x4002DFFF, 'QEI1'),
	(0x40038000, 0x40038FFF, 'ADC0'),
	(0x40039000, 0x40039FFF, 'ADC1'),
	(0x40040000, 0x40040FFF, 'CAN0'),
	(0x40041000, 0x40041FFF, 'CAN1'),
	(0x40050000, 0x40050FFF, 'USB'),
	(0x400FE000, 0x400FEFFF, 'SystemControl'),
	(0x400FF000, 0x400FFFFF, 'uDMA'),
]


def add_segments():
	for seg in SEGMENTS:
		# AddSeg(startea, endea, base, use32, align, comb)

		start 	= seg[0]
		end 	= seg[1]
		desc 	= seg[2].replace(" ", "_")

		print start, end

		if seg[0] and seg[1] and seg[2]:
			AddSeg(start, end, 0x0, 1, 1, 0)
			s = getseg(start)
			set_segm_name(s, desc)
		

add_segments()
#set_names()
