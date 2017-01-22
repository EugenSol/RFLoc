# Particle Filter Class
#
from scipy.stats import norm

class RF_ParticleFilter:
def __init__(self, LocEar, ExplorationNoise, MeasurementNoise, nParticles, bplot=True, blog=False, bprintdata=False): #RF_ParticleFilter is able to call the methods of locear
    self.locear = locear
    self.nParticles = nParticles
    self.ExplorationNoise = ExplorationNoise
    self.MeasurementNoise = MeasurementNoise


def start(self, world_x, world_y):
    """ Particle Ini """
    particles = []  # initialize Particle set
    for i in range(self.nParticles)     # create particles with uniformly distributed position
        particles.append( ParticleClass(random.uniform(world_x), random.uniform(world_y)) )

        # measurement function to compute predicted measurement from particle
    def predict_meas(rx_pos, txposition):
        n_tx = txposition.shape[0]
        RSS_vec = []
        for idx_tx in range(n_tx):
            txpos_i = txposition[idx_tx]
            dist = np.sqrt( (rxpos[0]-txpos_i[0])**2 + (rxpos[1]-txpos_i[1])**2 )
            if dist == 0:
                dist = 1
            RSS = -20 * np.log10(dist) - 20 * dist * self.locear._LocEar__alpha[idx_tx] * np.log10(np.exp(1) + self.locear._LocEar__xi[idx_tx]
            RSS_vec = np.append(z_vec, z)
        return RSS_vec

    def w_comp(measurement, predict_meas, n_tx):
        prob = 1
        for idx_tx = in range(n_tx):
            prob *= scipy.stats.norm( measurement[idx_tx], meas_cov[idx_tx]).pdf(predict_meas[idx_tx])
        return w = prob


    """ Start Particle Filter Loop """
    tracking = True
    while tracking:



#---------------------------
class ParticleClass:
    def __init__(self, x, y, weight=1):
        self.x = x
        self.y = y
        self.weight = weight

    def move(self, in_x_dir, in_y_dir):
        self.x += in_x_dir
        self.y += in_y_dir
