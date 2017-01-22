# Particle Filter Class
#
class RF_ParticleFilter:

def __init__(self, LocEar, ExplorationNoise, nParticles, bplot=True, blog=False, bprintdata=False): #RF_ParticleFilter is able to call the methods of locear
    self.locear = locear
    self.nParticles = nParticles
    self.ExplorationNoise = ExplorationNoise

def start(self, world_x, world_y):
    """ Particle Ini """
    particles = []  # initialize Particle set
    for i in range(self.nParticles)     # create particles with uniformly distributed position
        particles.append( ParticleClass(random.uniform(world_x), random.uniform(world_y)) )

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
