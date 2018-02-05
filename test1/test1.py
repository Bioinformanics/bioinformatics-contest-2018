
def simple():
    with open('test1_input_simple.txt', 'r') as input:
        lines = [line.strip() for line in input.readlines()]
        size = int(lines[0])
    with open('test1_output_simple.txt', 'w') as output:
        for i in range(int(size)):
            params = lines[i+1].split(' ')
            a = int(params[0])
            b = int(params[1])
            x = int(params[2])
            atp_amount = find_atp_amount(a, b, x)
            output.write(str(atp_amount))
            output.write('\n')

def find_atp_amount(a, b, x):
    if b <= 3*a:
        return x/(a+6*b)*38
    else:
        return x/a*2

simple()