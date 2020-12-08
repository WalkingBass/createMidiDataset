from src.MidiFiles import *


def test_construction():

    chord_file = ChordFile(0, 120, 60, (0, 3, 6), 2, 1, 0, 0, 'none', 0)
    assert chord_file
