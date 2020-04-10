import numpy as np
import matplotlib.pyplot as plt

'''
Data from displacement helix (residues 293-304) over 100 frames from the last microsecond of the simulation.
The data represents the angle between helices of states fullyP-unP and partP-unP.
'''

fullp_unp = np.array([2.05, 0.75, 2.52, 12.50, 11.96, 11.38, 11.11, 3.82, 9.84, 8.23, 15.72, 9.10, 13.37, 8.94, 8.51,
                      3.85, 6.86, 3.42, 2.19, 11.57, 12.50, 9.20, 4.13, 9.21, 12.10, 0.40, 11.55, 5.52, 12.18, 12.80,
                      1.98, 7.09, 6.78, 8.24, 17.21, 4.26, 7.81, 7.43, 7.69, 6.87, 2.56, 1.64, 6.86, 4.29, 6.76, 3.56,
                      10.58, 15.12, 2.74, 5.04, 8.03, 4.66, 7.60, 14.65, 9.12, 7.83, 8.37, 15.47, 11.52, 4.48, 8.01,
                      6.47, 12.60, 3.02, 2.36, 6.12, 9.29, 5.14, 11.72, 9.90, 8.89, 7.45, 16.32, 5.64, 18.51, 10.55,
                      1.77, 19.69, 7.82, 8.89, 5.02, 5.15, 8.49, 13.78, 16.64, 14.47, 12.77, 5.20, 8.86, 11.88, 1.82,
                      13.37, 19.67, 8.04, 4.67, 4.85, 7.27, 19.13, 8.28, 8.30, 3.83])

print("Mean FullyP-UnP:", np.mean(fullp_unp))
print("Variance FullyP-UnP:", np.var(fullp_unp))
print("Standard deviation FullyP-UnP:", np.std(fullp_unp))

partp_unp = np.array([2.66, 4.90, 1.25, 12.04, 5.60, 6.14, 6.73, 6.02, 13.55, 8.11, 1.48, 8.17, 7.65, 10.05, 2.36,
                      11.20, 12.35, 10.25, 12.13, 4.88, 6.77, 3.47, 5.62, 3.10, 9.13, 8.31, 5.39, 2.38, 6.47, 10.05,
                      4.26, 10.26, 4.36, 6.55, 11.56, 7.15, 11.47, 15.34, 3.62, 8.28, 11.65, 1.24, 6.72, 2.78, 3.64,
                      3.15, 13.40, 5.03, 5.38, 5.84, 10.44, 4.09, 7.70, 5.77, 3.89, 6.31, 10.81, 7.16, 11.36, 7.36,
                      6.02, 11.96, 7.21, 6.46, 8.43, 9.62, 2.96, 2.92, 4.24, 10.12, 16.27, 9.71, 2.94, 4.28, 5.29,
                      7.73, 9.89, 11.09, 15.49, 8.04, 4.37, 7.35, 10.72, 6.56, 8.67, 8.60, 4.84, 7.62, 10.30, 14.80,
                      8.18, 8.58, 15.83, 9.70, 6.27, 12.87, 2.15, 14.76, 5.65, 1.30, 5.58])

print("Mean PartP-UnP:", np.mean(partp_unp))
print("Variance PartP-UnP:", np.var(partp_unp))
print("Standard deviation PartP-UnP:", np.std(partp_unp))

time = list(range(1800, 2810, 10))

'''
Plotting the data over time (ns)
'''

plt.plot(time, fullp_unp, "m-")
plt.axhline(y=np.mean(fullp_unp), color='r')
plt.xlabel("Time (ns)")
plt.ylabel("Displacement Angle (degrees)")
plt.title("Displacement Angle Between FullyP-UnP")
plt.show()


plt.plot(time, partp_unp)
plt.axhline(y=np.mean(partp_unp), color='r')
plt.xlabel("Time (ns)")
plt.ylabel("Displacement Angle (degrees)")
plt.title("Displacement Angle Between PartP-UnP")
plt.show()
