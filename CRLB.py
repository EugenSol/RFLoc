# Compute Cramer-Rao lower bounds for spherical localization problem for range dependent measurement covariance
import numpy as np
import matplotlib.pyplot as plt


x_list = np.linspace(-500, 2000, 100)
y_list = np.linspace(-250, 1250, 100)
X, Y = np.meshgrid(x_list, y_list)

txpos = np.array([[1500, 1000],
         [1500, 0],
         [0, 1000],
         [0, 0]])

n_tx = txpos.shape[0]
alpha = 0.0134
measCov_const = 1
measCov_slope = 9/2000

def measCov_i(dist):
    return dist * measCov_slope + measCov_const

def dist(txpos_i, rxpos):
    dist = np.sqrt( (rxpos[0]-txpos_i[0])**2 + (rxpos[1]-txpos_i[1])**2 )
    if dist == 0:
        dist = 1
    return dist

def dCov_i(txpos_i, rxpos, d_var):
    dist_eval = dist(txpos_i, rxpos)
    return measCov_slope * (txpos_i[d_var] - rxpos[d_var])/dist_eval

def dRSS_i(txpos_i, rxpos, d_var): # compute derivative of RSS signal
    dist_eval = dist(txpos_i, rxpos)
    return -20 / (np.log(10)*dist_eval**2) * (txpos_i[d_var] - rxpos[d_var]) - 20 * alpha * np.log10(np.exp(1)) * (txpos_i[d_var] - rxpos[d_var])/dist_eval

def fisher_matrix(x,y):  # compute Fisher information matrix for position (x,y)
    F = np.zeros([2, 2]) # initialize Fisher information matrix
    #
    for m in range(2):
        for n in range(2):
            dmu_T = np.array([])
            dmu = np.array([])
            C = np.array([])
            dC_m = np.array([])
            dC_n = np.array([])
            for N in range(n_tx):
                dmu_T = np.append(dmu_T, dRSS_i(txpos[N], [x,y], m) )
                dmu = np.append(dmu, dRSS_i(txpos[N], [x,y], n) )
                C = np.append(C, measCov_i( dist(txpos[N], [x,y]) ) )
                dC_m = np.append(dC_m, dCov_i(txpos[N], [x,y], m))
                dC_n = np.append(dC_n, dCov_i(txpos[N], [x,y], n))
            C_inv = np.linalg.inv( np.diag(C) )
            F[m,n] = np.dot(np.transpose(dmu_T), np.dot(C_inv, dmu) ) + 0.5 * np.trace( C_inv.dot(np.diag(dC_m)).dot(C_inv).dot(np.diag(dC_n)) )

    return F


CRLB = np.zeros((100,100))

for i in range(100):
    for j in range(100):
        # CRLB is the worst case of the covariance matrix
        CRLB[i,j] = np.amax(np.linalg.inv(fisher_matrix(X[i,j],Y[i,j])))

maxVar = np.amin(CRLB)
CRLB = CRLB/maxVar

plt.pcolor(X, Y, CRLB)
plt.xlabel('$x$ in mm')
plt.ylabel('$y$ in mm')
plt.colorbar()

#plt.show()

from matplotlib2tikz import save as tikz_save
tikz_save('crlb.tex')
