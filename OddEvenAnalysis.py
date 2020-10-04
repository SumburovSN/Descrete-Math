name = 'positiveOddEven.txt'
sequences = []
file = open(name, "r")
for line in file:
    suit = line.replace("[", "").replace("];\n", "").split(", ")
    sequence = []
    for number in suit:
        sequence.append(int(number))
    sequences.append(sequence)

file.close()
print(sequences)
print(len(sequences))

count_with_5 = 0
for sequence in sequences:
    if 10 in sequence:
        count_with_5 += 1
print(count_with_5)
