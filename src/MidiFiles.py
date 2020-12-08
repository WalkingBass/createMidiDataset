# This is to hold the Classes that will create the MIDI files

from midiutil import MIDIFile


class ChordFile:
    def __init__(self, program, tempo, pitch, chord, duration=1, volume=1, start_beat=1, trail_silence=1,
                 noise_type='none', noise_volume=0):
        self.program = program
        self.tempo = tempo
        self.pitch = pitch
        self.chord = chord
        self.duration = duration
        self.volume = volume
        self.start_beat = start_beat
        self.trail_silence = trail_silence
        self.noise_type = noise_type
        self.noise_volume = noise_volume
        self.track = 0
        self.channel = 0

        my_midi = MIDIFile(1)

        my_midi.addTempo(self.track, 0, self.tempo)

        for item in self.chord:
            my_midi.addNote(self.track, self.channel, self.pitch + item, self.start_beat, self.duration, self.volume)

        my_midi.addProgramChange(self.track, self.channel, 0, self.program)

        self.midi_file = my_midi

    def write_file(self, path=''):
        if path != '':
            with open(path, "wb") as output_file:
                self.midi_file.writeFile(output_file)
