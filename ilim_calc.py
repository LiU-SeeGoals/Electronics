import random
resistors = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91]

def ilim_calc(Vin, desired_threshold):
    desired_Vout = (3.3/2) - 0.4*0.9*desired_threshold/8
    print(desired_Vout)
    diff_Vout = 10000
    output = []
    R1 = None
    R2 = None
    Vout = None
    for i1 in range(len(resistors)):
        for i2 in range(len(resistors)):
            R1 = resistors[i1]
            R2 = resistors[i2]
            Vout = Vin*R2/(R1 + R2)
            if (diff_Vout > abs(Vout-desired_Vout)):
                diff_Vout = abs(Vout-desired_Vout)
                output = [Vout, R1, R2]

    return output

print(ilim_calc(3.3, 5.48))