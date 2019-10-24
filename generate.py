import math
from pyknon.MidiFile import MIDIFile

ntracks = 8
m = MIDIFile(ntracks)
length = 1024
prev = [-1]*ntracks
def add(trk,chn,note,time,dur,vol,rep=False):
    if time >= length:
        return
    if rep or note != prev[trk]:
        m.addNote(trk,chn,note,time,dur,vol)
    else:
        idx = -1
        while 'duration' not in dir(m.tracks[trk].eventList[idx]):
            idx -= 1
        m.tracks[trk].eventList[idx].duration += dur
    prev[trk] = note
def popcnt(x):
    return bin(x).count('1')
def toscale(scale, note):
    poct = popcnt(scale)
    n = note%(poct+1)
    c = 0
    o = 0
    for i in format(scale,'012b'):
        if i == '1':
            c += 1
        if c-1 == n:
            break
        o += 1
    return o + note//12*12
scale = int('101001010100',2)

# set instruments
m.addProgramChange(0,0,0,5)
m.addProgramChange(1,1,0,63)
m.addProgramChange(2,2,0,5)
m.addProgramChange(3,3,0,5)
m.addProgramChange(4,4,0,5)
m.addProgramChange(5,5,0,116)
m.addProgramChange(6,6,0,117)
m.addProgramChange(7,7,0,118)

t = 0
dt = 0
for _ in range(65536):
    if dt%64==0:
        shift=1
        scale = (scale >> (12-shift)) | ((scale & ((1<<11)-1))<<shift)
    sh = 4
    p = (t&t//5|t//16&t//64)%48+44
    add(0,0,toscale(scale,p),t/16,sh/16,70)
    p = (t//100&t//64)%48+32
    add(1,1,toscale(scale,p),t/16,sh/16,127)
    p = (t&t//3|t//17&t//65)%48+44
    add(2,2,toscale(scale,p),t/16,sh/16,70)
    p = (t&t//2|t//18&t//66)%48+44
    add(3,3,toscale(scale,p),t/16,sh/16,70)
    p = (t&t//1|t//19&t//67)%48+44
    add(4,4,toscale(scale,p),t/16,sh/16,70)
    p = (t//100&t//64)%48+32
    add(5,5,toscale(scale,p),t/16,sh/16,120)
    p = (t&t//16|t//75&t//67)%36+32
    add(6,6,toscale(scale,p),t/16,sh/16,70)
    p = (t&t//34|t//78&t//64)%24+32
    add(7,7,toscale(scale,p),t/16,sh/16,70)
    t += sh
    dt += 1
m.writeFile(open('out.mid','wb'))
