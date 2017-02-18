# Particle Filter Class
#
from scipy.stats import norm

class RF_ParticleFilter:
def __init__(self, LocEar, ExplorationNoise, MeasurementNoise, nParticles, bplot=True, blog=False, bprintdata=False): #RF_ParticleFilter is able to call the methods of locear
    self.locear = locear
    self.nParticles = nParticles
    self.ExplorationNoise = ExplorationNoise
    self.MeasurementNoise = MeasurementNoise

def comp_mean(self, particles):
    m_x, m_y, count = 0, 0, 0

    for i in range(self.nParticles)
        count += count
        m_x += m_x
        m_y += m_y

    return m_x/count, m_y/count


def start(self, world_x, world_y):
    """ Particle Ini """
    particles = []  # initialize Particle set
    for i in range(self.nParticles)     # create particles with uniformly distributed position
        particles.append( ParticleClass(self, random.uniform(world_x), random.uniform(world_y)) )

    """ Start Particle Filter Loop """
    tracking = True
    while tracking:
        """ Prediction Step """
        p_temp = []
        for i in range(self.nParticles)
            p_temp.append( particles[i].move( np.random.normal(0, self.ExplorationNoise), np.random.normal(0, self.ExplorationNoise) ))
        particles = p_temp

        """ Update Step """
        """ Compute predicted Measurements """
        predict_meas = []
        for i in range(self.nParticles)
            predict_meas.append( particles[i].predict() )
        """ Generate Particle Weights depending on robots measurement """

#---------------------------
class ParticleClass:
    def __init__(self, pffilter, x, y, weight=1, txposition):
        self.pffilter = pffilter
        self.x = x
        self.y = y
        self.weight = weight
        self.txposition = txposition

    def move(self, in_x_dir, in_y_dir):
        self.x += in_x_dir
        self.y += in_y_dir

                # measurement function to compute predicted measurement from particle
    def predict_meas(self):
                n_tx = self.txposition.shape[0]
                RSS_vec = []
                for idx_tx in range(n_tx):
                    txpos_i = self.txposition[idx_tx]
                    dist = np.sqrt( (rxpos[0]-txpos_i[0])**2 + (rxpos[1]-txpos_i[1])**2 )
                    if dist == 0:
                        dist = 1
                    RSS = -20 * np.log10(dist) - 20 * dist * self.pffilter.locear._LocEar__alpha[idx_tx] * np.log10(np.exp(1) + self.pffilter.locear._LocEar__xi[idx_tx]
                    RSS_vec = np.append(z_vec, z)
                return RSS_vec

    def w_comp(self, measurement, meas_cov, predict_meas):
                probability = 1
                n_tx = self.txposition.shape[0]
                for idx_tx in range(n_tx):
                    probability *= scipy.stats.norm( measurement[idx_tx], meas_cov[idx_tx] ).pdf(predict_meas[idx_tx])
                return w = probability
