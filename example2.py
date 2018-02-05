
def run():
    with open('example2_input.txt', 'r') as input:
        lines = [line.strip() for line in input.readlines()]
        size = int(lines[0])
    with open('example2_output.txt', 'w') as output:
        for i in range(int(size)):
            dna = lines[i*2+1]
            motif = lines[i*2+2]
            positions = find_positions(dna, motif)
            output.write(' '.join(positions))
            output.write('\n')

def find_positions(dna, motif):
    output = []
    for i in range(len(dna)-len(motif)):
        if dna[i:i+len(motif)] == motif:
            output.append(str(i+1))
    return output

run()