'''
Use Placzek formula to calculate the contrbution of an excitation to the polarizability and the prefactors of polarizability deriatives wrt excitation energy (dalpha_dE) or transition dipole (dlapha_dmu) for the excitation
more information is avilable from paper 'A polarizability theory of the resonance Raman effect' (J. Chem. Phys. 74, 4930)

Given the frequency of incident light / a.u., the lifetime of excited states / a.u., the energy /a.u. and transition dipole / a.u. (usually in one direction) of each excitation, polarizability (real and imaginary parts) can be calculated using Placzek formula.

Notice the calculation of the off-diagonal elements of the polarizability has not been coded.
'''

class placzek():
  def __init__(self, lifetime, incfreq, energy, dip):
    if incfreq == 0.0:
      self.lifetime = 0.0
    else:
      self.lifetime = lifetime
    self.incfreq = incfreq
    self.energy = energy
    self.dip = dip
  ### Sum-over-states formula for pol ###
    self.alpha_real =  self.dip*self.dip*( (self.energy-self.incfreq) / ((self.energy-self.incfreq)**2.0 + self.lifetime**2.0) + (self.energy + self.incfreq) / ((self.energy + self.incfreq)**2.0 + self.lifetime**2.0))
    self.alpha_imag =  self.dip*self.dip*( self.lifetime*(1j) / ((self.energy-self.incfreq)**2.0 + self.lifetime**2.0) - self.lifetime * (1j) / ((self.energy + self.incfreq)**2.0 + self.lifetime**2.0))

  ### prefactors for AB terms ###
    self.dalpha_dE_real = self.dip * self.dip * ((self.lifetime**2.0 - (self.energy - self.incfreq)**2.0) / ((self.energy - self.incfreq)**2.0 + self.lifetime**2.0)**2.0 + (self.lifetime**2.0 - (self.energy + self.incfreq)**2.0) / ((self.energy + self.incfreq)**2.0 + self.lifetime**2.0)**2.0 )

    self.dalpha_dE_imag = self.dip * self.dip * (-2j*self.lifetime*(self.energy - self.incfreq) / ((self.energy - self.incfreq)**2.0 + self.lifetime**2.0)**2.0 + 2j*self.lifetime*(self.energy + self.incfreq) / ((self.energy + self.incfreq)**2.0 + self.lifetime**2.0)**2.0)

    self.dalpha_dmu_real = 2 * self.dip * ((self.energy - self.incfreq) / ((self.energy - self.incfreq)**2.0 + self.lifetime**2.0) + (self.energy + self.incfreq) / ((self.energy + self.incfreq)**2.0 + self.lifetime**2.0))

    self.dalpha_dmu_imag = 2 * self.dip * (1j*self.lifetime / ((self.energy - self.incfreq)**2.0 + self.lifetime**2.0) - 1j*self.lifetime / ((self.energy + self.incfreq)**2.0 + self.lifetime**2.0) )



