filepath = 'input'
def calculate_fuel_mass(module_mass):
    return int(module_mass / 3) - 2


def calc_full_mass(module_mass):
    fmass = calculate_fuel_mass(module_mass)
    ffmass = calculate_fuel_mass(fmass)
    while ffmass > 0:
        if ffmass >= 0:
            fmass += ffmass
        ffmass = calculate_fuel_mass(ffmass)
    return fmass

with open(filepath) as fp:
    line = fp.readline()
    acc = 0
    cnt = 0
    while line:
        acc += calc_full_mass(int(line))
        cnt += 1
        line = fp.readline()
    print(cnt)
    print(acc)

