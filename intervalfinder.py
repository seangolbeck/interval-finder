move = ["m2", "M2", "m3", "M3", "P4", "#4", "b5", "P5", "#5" "m6", "M6", "m7", "M7"]

pitch_lists = {"C": ["Db", "D", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "Bb", "B"],
"C#": ["D", "D#", "E", "E#","F#", "Fx", "G", "G#", "Gx", "A", "A#", "B", "B#"],
"Db": ["Ebb", "Eb", "Fb", "F", "Gb", "G", "Abb", "Ab", "A", "Bbb", "Bb", "Cb", "C"],
"D": ["Eb", "E", "F", "F#", "G", "G#", "Ab", "A", "A#", "Bb", "B", "C", "C#"],
"D#": ["E", "E#", "F#", "Fx", "G#", "Gx", "A", "A#", "Ax", "B", "Bx", "C#", "Cx"],
"Eb": ["Fb", "F", "Gb", "G", "Ab", "A", "Bbb", "Bb", "B", "Cb", "C", "Db", "D"],
"E": ["F", "F#", "G", "G#", "A", "A#", "Bb", "B", "B#", "C", "C#", "D", "D#"],
"F": ["Gb", "G", "Ab", "A", "Bb", "B", "Cb", "C", "C#", "Db", "D", "Eb", "E"],
"F#": ["G", "G#", "A", "A#", "B", "B#", "C", "C#", "Cx", "D", "D#", "E", "E#"],
"Gb": ["Abb", "Ab", "Bbb", "Bb", "Cb", "C", "Dbb", "Db", "D", "Ebb", "Eb", "Fb", "F"],
"G": ["Ab", "A", "Bb", "B", "C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#"],
"G#": ["A", "A#", "B", "B#", "C#", "Cx", "D", "D#", "Dx", "E", "E#", "F#", "Fx"],
"Ab": ["Bbb", "Bb", "Cb", "C", "Db", "D", "Ebb", "Eb", "E", "Fb", "F", "Gb", "G"],
"A": ["Bb", "B", "C", "C#", "D", "D#", "Eb", "E", "E#", "F", "F#", "G", "G#"],
"A#": ["B", "B#", "C#", "Cx", "D#", "Dx", "E", "E#", "Ex", "F#", "Fx", "G#", "Gx"],
"Bb": ["Cb", "C", "Db", "D", "Eb", "E", "Fb", "F", "F#", "Gb", "G", "Ab", "A"],
"B": ["C", "C#", "D", "D#", "E", "E#", "F", "F#", "Fx", "G", "G#", "A", "A#"]}
pitch = input("use uppercase letter for pitch name '#' for sharp 'b' for flat    practical pitches only                                                           enter pitch:")
interval = input("use lowercase 'm' for minor, uppercase 'M' for major, 'b' for flat symbol, '#' for sharp, 'P' for perfect                                              .....enter interval:")
shift = move.index(interval)
print(pitch_lists[pitch][shift])


