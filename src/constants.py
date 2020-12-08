BaseLine = 60           # 10
NoteRange = 12         # 120
VariationRange = 3      # 25
MaxDuration = 10
MinVolume = 20
MaxVolume = 120
VolumeRange = MaxVolume - MinVolume
MaxStartBeat = 3
BeatTolerance = 0.1
# paths
soundfont = './util/sound_fonts/FluidR3_GM.sf2'
midi_folder_path = "./data/midi_files/"
wav_folder_path = "./data/wav_files/"
# Chords qualities:
Chords = {
    "single": [0],
    "major_t": [0, 4, 7],
    "minor_t": [0, 3, 7],
    "dim_t": [0, 3, 6]
}
Chords_Thirds = {
    "single": "none",
    "major_t": "major",
    "minor_t": "minor",
    "dim_t": "minor"
}
Chords_Fifths = {
    "single": "none",
    "major_t": "natural",
    "minor_t": "natural",
    "dim_t": "diminished"
}
Chords_Sevenths = {
    "single": "none",
    "major_t": "none",
    "minor_t": "none",
    "dim_t": "none"
}

"""
Chords = {
    "major_t": [0, 4, 7],
    "minor_t": [0, 3, 7],
    "dim_t": [0, 3, 6],
    "major_M7": [0, 4, 7, 11],
    "major_7" : [0, 4, 7, 10],
    "major_6" : [0, 4, 7, 9],
    "minor_M7" : [0, 3, 7, 11],
    "minor_7" : [0, 3, 7, 10],
    "dim_7" : [0, 3, 6, 10],
    "dim" : [0, 3, 6, 9]
}
"""