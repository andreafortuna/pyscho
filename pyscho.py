#!/bin/env python

from midiutil.MidiFile import MIDIFile
from random import seed
from random import randint, randrange
import argparse


scales = { 
    "major" : [0, 2, 4, 5, 7, 9, 11],
    "minor" : [0, 2 , 3, 5, 7, 10, 11],
    "dorian" : [0,  2,  3,  5,  7,  9, 10, 12],
    "phrygian" : [0, 1, 3, 5, 7, 8, 10, 12],
    "minor_pentatonic" : [0, 3, 5, 7, 10],
    "major_pentatonic" : [0, 2, 4, 7, 9],
    "harmonic_minor" : [0, 2, 3, 5, 7, 8, 10, 12],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "minor_blues" : [0, 3, 5, 6, 7, 10],
    "locrian" : [0, 1, 3, 5, 6, 8, 10, 12],
    "lydian" :[0, 2, 4, 6, 7, 9, 11, 12],
}

def get_notes(start, intervals):
	return_array = []
	for x in range(0, 2):
		for y in range(0,len(intervals)):
			#print (start + (intervals[y]*x))
			return_array.append(start + (intervals[y] + (12 * x)))
	return return_array    

print ('''
             ____       _
 _ __  _   _/ ___|  ___| |__   ___
| '_ \| | | \___ \ / __| '_ \ / _ \\
| |_) | |_| |___) | (__| | | | (_) |
| .__/ \__, |____/ \___|_| |_|\___/
|_|    |___/

pySchö (python Schönberg) - algorithmic music composition
''')

parser = argparse.ArgumentParser(description="")

parser.add_argument('seed',  help='Algorithm seed')
parser.add_argument('outputfile',  help='output file name')
parser.add_argument('--scale', dest='scale', action='store',default='major', help='musical scale: major, minor, dorian, phrygian, minor_pentatonic, major_pentatonic, harmonic_minor, mixolydian, minor_blues, locrian, lydian (default: major)')
parser.add_argument('--start', dest='start', action='store', type=int, default=60, help='first note (default: 60 - C4)')
parser.add_argument('--bars', dest='bars', action='store',type=int, default=10, help='number of bars (default: 10)')
args = parser.parse_args()

start = args.start #60
mf = MIDIFile(1)
track = 0
time = 0
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)
channel = 0
volume = 100

c_beat = 0
	

seed(args.seed)

notes = get_notes(start,scales[args.scale])
print (notes)
while (c_beat < (args.bars * 4)):
	value = randint(0, len(notes)-1) 
	duration = randrange(25, 425, 25) / 100	
	print(notes[value], duration)
	pitch = notes[value]
	time = c_beat
	mf.addNote(track, channel, pitch, time, duration, volume)
	c_beat += duration


with open(args.outputfile, 'wb') as outf:
    mf.writeFile(outf)
