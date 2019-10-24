from pyknon.MidiFile import MIDIFile, MIDIHeader, MIDITrack, writeVarLength, frequencyTransform,  returnFrequency

tx = 11
m = MIDIFile(tx)
length = 256
# all notes off
for t in range(128):
    m.addNote(0,0,t,0,0,0)
prev = [-1]*tx
def writeNote(a,b,c,d,e,f,g=False):
    if d >= length:
        return
    if g or c != prev[a]:
        m.addNote(a,b,c,d,e,f)
    else:
        m.tracks[a].eventList[-1].duration += e
    prev[a] = c
def popcnt(x):
    return bin(x).count('1')
def toscale(scale, note): # todo: totally broken
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
m.addProgramChange(0,0,0,65)
m.addProgramChange(1,1,0,63)
for t in range(2048):
    if t%64==0:
        scale = (scale >> 9) | ((scale & ((1<<11)-1))<<3)
    writeNote(0,0,toscale(scale,(t//2&t//5|t//8&t//16)%36+60),t/8,1/8,127)
    writeNote(1,1,toscale(scale,(t//5|t//8|t//16)%12+36),t/8,1/8,127)
m.writeFile(open('out.mid','wb'))
