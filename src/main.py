# This is the main python script to create a whole data set of MIDI files.

"""
Things to do
    DONE create .json file with annotation data
    TODO add variation on the instruments
    TODO add variation in the soundfont
    TODO add more chords
    TODO add inversions
    TODO add trailing silence
    TODO make sure the midi_files and wav_files folders exist, if not create them.

Issues detected:
    # Does not work because midi_to_audio does not pass -T to fluidsynth
    fs.midi_to_audio(midi_file_path, wav_file_path)
    # Does not work because -T is not specified??
    subprocess.call(['fluidsynth', '-F', wav_file_path, '-ni', soundfont, midi_file_path])
"""

# from midi2audio import FluidSynth
# from fluidsynth import *
from src.MidiFiles import *
from random import *
from math import *
import subprocess
import src.constants as ct
import json

# Initialize FluidSynth
soundfont = './util/sound_fonts/FluidR3_GM.sf2'
# fs = FluidSynth(sound_font=soundfont, sample_rate=22050)

# here we will create the midi files for all chords with variations on volume and timing.
data = {}
for value in range(ct.NoteRange):
    """ Choose base pitch """
    pitch = ct.BaseLine + value
    for chord_name in ct.Chords.keys():
        """ choose chord type """
        chord = ct.Chords.get(chord_name)
        for variation in range(ct.VariationRange):
            """ Define variability """
            duration = random() * ct.MaxDuration
            volume = int(ct.MinVolume + random() * ct.VolumeRange)
            start_beat = floor(random() * ct.MaxStartBeat) + random() * ct.BeatTolerance
            """ Define file name and paths """
            file_name = "c{}_p{}_v{}_s{:1.0f}_d{:1.0f}" \
                .format(chord_name, pitch, volume, start_beat * 100, duration * 10)
            midi_file_path = ct.midi_folder_path + file_name + '.midi'
            wav_file_path = ct.wav_folder_path + file_name + '.wav'
            """ Create midi object, write midi and convert/write wav """
            my_file = ChordFile(0, 120, pitch, chord, duration, volume, start_beat, 0, 'none', 0)
            my_file.write_file(midi_file_path)
            subprocess.call(['fluidsynth', '-T', 'wav', '-F', wav_file_path, '-ni', soundfont, midi_file_path])
            """ Create data dict for that file """
            chord_data = {"chord_name": chord_name, "pitch": pitch, "chord_form": chord,
                          "third": ct.Chords_Thirds[chord_name], "fifth": ct.Chords_Fifths[chord_name],
                          "seventh": ct.Chords_Sevenths[chord_name]}
            data[file_name] = chord_data

with open('./data/ChoRe_data.json', 'w') as outfile:
    json.dump(data, outfile)
