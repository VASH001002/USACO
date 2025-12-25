"""
ID: v_asvin1
LANG: PYTHON3
PROG: ride
"""
pplfile = open("ride.in", "r")
UFO = pplfile.readline()
PPL = pplfile.readline()
outfile = open("ride.out", "w")
ufo_value = 1

for i in UFO:
    ufo_value *= (ord(i)-64)

ppl_value = 1
for j in PPL:
    ppl_value *= (ord(j)-64)

if ufo_value % 47 == ppl_value % 47:
    #print("GO")
    outfile.write("GO\n")
else:
    outfile.write("STAY\n")