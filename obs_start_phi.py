from astropy import units as u
from astropy.time import Time
import numpy
import math


#################################################################
## Orbital ephemeris from Falanga et al 2015
# orb_epoch = 48900.373 ## units MJD
# Porb_0 = 3.411581 ## unit days D
# Porb_rch = -3.3E-6 ## unit yrs^-1
# Porb_rch *= 1/365.242374 ## units D^-1
##################################################################

#################################################################
## Orbital ephemeris from Islam and Paul 2016
orb_epoch = 49149.412 ## units MJD
Porb_0 = 3.411660 ## unit days D
Porb_rch = -4.7E-7 ## unit yrs^-1
Porb_rch *= 1/365.242374 ## units D^-1
#################################################################

######## This is the code for turning XRISM start time into MJD
xrism_obs_start = Time('2025-02-10T11:46:04.0', format='isot', scale='utc')
obs_start_MJD = xrism_obs_start.mjd

print(f'Obs start date {obs_start_MJD} (MJD)')

time_since_epoch = obs_start_MJD - orb_epoch

Porb_current = Porb_0 + (time_since_epoch*Porb_rch)
print(f'Current orbital period {Porb_current}')

orbs_since_epoch = math.floor(time_since_epoch/Porb_current)
## print(f'orbs since epoch = {orbs_since_epoch}')

t_last_orb = orb_epoch + Porb_current*orbs_since_epoch
## print(f'time of last eclipse = {t_last_orb}')

orb_phase_start = (obs_start_MJD - t_last_orb)/Porb_current
print(f'Obs starts at orbital phase {orb_phase_start}')
