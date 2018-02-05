import math

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
    if b <= 3*a:  # aerobic is more economic
        return x/(a+6*b)*38
    else:  # fermentation is more economic
        return x/a*2

# simple()

def hard():
    with open('test1_input_hard.txt', 'r') as input:
        lines = [line.strip() for line in input.readlines()]
        size = int(lines[0])
    with open('test1_output_hard.txt', 'w') as output:
        for i in range(int(size)):
            params = lines[i+1].split(' ')
            a = int(params[0])
            b = int(params[1])
            x = int(params[2])
            atp_amount = find_atp_amount_hard(a, b, x)
            output.write(str(atp_amount))
            output.write('\n')

def find_atp_amount_hard(a, b, x):
    max_apt = 0
    unit_price_in_aerobic = a/6+b
    max_r = math.floor(x/unit_price_in_aerobic) # r = mole of oxygen

    if b <= 3*a: # aerobic is more economic, maximize oxygen
        start = max_r
        end = 0
        step = -1
    else: # fermentation is more economic, minimize oxygen
        start = 0
        end = max_r
        step = 1
    for r in range(start, end, step):
        glucose = math.floor((x - b * r) / a)
        glucose_in_aeribic = r/6
        apt_amount = 38 * glucose_in_aeribic + 2 * (glucose - glucose_in_aeribic)
        if apt_amount >= max_apt:
            max_apt = apt_amount
        else:
            break
    return max_apt

# print(str(find_atp_amount_hard(7, 5, 23)))
hard()