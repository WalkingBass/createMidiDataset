createMidiDataset

This project tries to create an artificial annotated dataset of MIDI files for the following musical elements:

- Single notes (all 88 notes) with randomized lengths, strengths, durations, instruments, etc.
- All Major, Minor in no-inversion form, in different octaves.

In the future I want to add other chords like tetrads (diminished triad, dominant, Maj7, Min7, MajMin7, Diminished, HalfDiminished, etc.), inversions, two hands chords, extensions, etc.

This requires FluidSynth to be installed on the computer. You can find all the information on how to install it here TODO add URL.

This project needs a soundfont file named 'FluidR3_GM.SF2' in folder /createMidiDataset/util/sound_fonts/'. Due to the size of the soundfont file I am using I have not been able to include it in the repository. You can find the file I am using in https://member.keymusician.com/Member/FluidR3_GM/index.html.
