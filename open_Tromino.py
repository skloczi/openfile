import matplotlib.pyplot as plt
import numpy as np

file = open("/Users/annamaria/PhD/Data/Tromino/Archive/test_001part1/EqualizedFile.dat")
row = 0
headers = []
dataNS = []
dataEW = []
dataZ = []
dataSync = []
for line in file:
    # accessing headers information
    if row <= 34:
        if not line.strip():
            row = row +1
            continue
        else:
            rows = line.rstrip().split("\n")
            headers.append(rows)
            print(line)
            if "Sampling rate" in line:
                temp = line.rstrip().split()
                Fs = float(temp[2])
            row = row +1
    # extracting data vector
    elif row > 34:
        rows = line.rstrip().split()
        dataNS.append(float(rows[0]))
        dataEW.append(float(rows[1]))
        dataZ.append(float(rows[2]))
        dataSync.append(float(rows[3]))
        row = row +1

# defining the time step
dt = 1/Fs
nt = len(dataNS)
t = np.linspace(0,12,nt)

# Plotting the signal
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex='col')#,use_line_collection=True) #, sharey=True
axes = plt.gca()
fig.set_size_inches(18.5, 10.5, forward=True)

ax1.plot(t,dataNS)
ax1.set_ylabel('Velocity [mm/s]')#, fontsize=14)
ax1.set_title('NS component')#, fontsize=16)

ax2.plot(t,dataEW)
ax2.set_ylabel('Velocity [mm/s]')#, fontsize=14)
ax2.set_title('EW component')#, fontsize=16)

ax3.plot(t,dataZ)
ax3.set_ylabel('Velocity [mm/s]')#, fontsize=14)
ax3.set_title('Z compoment')#, fontsize=16)

ax4.plot(t,dataSync)
ax4.set_ylabel('[count]')#, fontsize=14)
ax4.set_title('Sync')#, fontsize=16)
ax4.set_xlabel('Time [minutes]')#, fontsize=14)

plt.show()
