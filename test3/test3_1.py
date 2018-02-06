import math

def run():
    with open('input/test1.fasta', 'r') as datafile:
        sequences = [line.strip() for line in datafile.readlines()][1::2]
    with open('output/test1_output.txt', 'w') as output:
        for sequence in sequences:
            output.write(find_tandem_repeats(sequence))
            output.write('\n')

def find_tandem_repeats(sequence):
    sequence_len = len(sequence)
    max_repeat_len = math.floor(sequence_len/2)
    repeat_found = False
    for repeat_len in range(max_repeat_len, 1, -1):
        start1 = 0
        max_start1 = len(sequence) - repeat_len - repeat_len  # two repeats have the same length
        while start1 <= max_start1 and not repeat_found:
            repeat1 = sequence[start1:start1+repeat_len]
            start2 = start1 + repeat_len
            while start2 + repeat_len <= sequence_len:
                repeat2 = sequence[start2:start2+repeat_len]
                if repeat1 == repeat2:  # two repeats are identical
                    repeat_found = True
                    break
                start2 += 1
            if repeat_found: break
            start1 += 1
        if repeat_found: break

    if not repeat_found:
        raise Exception('Repeat not found!')
    return ' '.join([str(start1+1), str(repeat_len), str(repeat_len)])

#print(find_tandem_repeats('ATACACTAGCG'))
#print(find_tandem_repeats('GTGGGACATACATAG'))
run()