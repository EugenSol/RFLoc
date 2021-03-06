import rf
import rf_tools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

txpos_offset = np.array([0, 0])

txpos_tuning = [[0, 0],  # 433.9MHz
                [0, 0],  # 434.1MHz
                [0, 0],  # 434.3MHz
                [0, 0]]  # 434.5MHz

analyze_tx = [1, 2, 3, 4]

#rf_tools.analyse_measdata_from_file(analyze_tx, txpos_tuning)


freqtx = [434.1e6, 434.15e6, 434.4e6, 434.45e6]
#cal = rf.CalEar(freqtx)

#cal.plot_psd()

#cal.get_performance()
#cal.plot_txrss_live()


freqspan = 2e4
freqcenter = np.mean(freqtx)

alpha = [0.013854339628529109, 0.0071309466013866158, 0.018077579531274993, 0.016243668091798915]
gamma = [-1.5898021024559508, 2.0223747861988461, -5.6650866655302714, -5.1158161676293972]
tx_abs_pos = [[1060, 470],  # 433.9MHz
              [1060, 1260],  # 434.1MHz
              [2340, 470],  # 434.3MHz
              [2340, 1260]]  # 434.5MHz


loc = rf.LocEar(freqtx, freqspan, alpha, gamma, tx_abs_pos)

#loc.plot_txdist_live()

x0 = np.array([600, 400])  # initial estimate
loc.set_size(16)
loc.map_path_ekf(x0, 'h_rss', True, False, False)
