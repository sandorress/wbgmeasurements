# extract POWER and DT from the measurement files
import math

def extractDt(filename):
    with open(filename, "rt") as f:
        return abs(float( f.readlines()[-1].split()[-1]))

def extractKey(filename, key):
    with open(filename, "rt") as f:
        for line in f:
            if line.startswith(key):
                line=line.replace('=','\t')
                vals=line.split()[1:]
                break
    return vals

BASE="igot_10mA_2A_"   # ezt kell átírni

print("Extracted data")
print("ID\tIS\tCH0\tCH1\tCH2\tCH3\tP0\tP1\tP2\tP3\tU0\tU1\tU2\tU3")
for dc in [4,6,8]:
    print(f"{dc}\t2", end='\t')
    for i in range(4):
        print( extractDt(f"{BASE}{dc}A.mr{i}"), end='\t')
    print(*extractKey(f"{BASE}{dc}A.par","POWERSTEP="), sep='\t', end='\t')
    print(*extractKey(f"{BASE}{dc}A.pwr","U_CHANNELS="), sep='\t')



