from adfexcit.placzek import *
from adfexcit.excitanal import *

print('========')
print('Use the placzek script to calculate the contribution of an excitation to the polarizability and the derivatives of the polarizability contribution of the excitation wrt excitation energy and transition dipole.')
print('Example system: CO-Ag4.')
print('In this example, excitation 3 is selected. The x component of the transition dipole is considered and thus the xx component of polarizability is calculated.')
print('Lifetime is 0.004 a.u. and the incident frequency is the excitation energy of excitation 3.')
print('========')

testexcit = excitanal('excit_COAg4.out', 0.6, 0.5)

i = 3
testplaczek = placzek(0.004, testexcit.excit[i][0], testexcit.excit[i][0], testexcit.excit[i][2][0])
print('The contribution of excitation {1:} to the polarization is {0:}'.format(testplaczek.alpha_real + 1j * testplaczek.alpha_imag, i))
print('The derivative of the polarzability contribution of excitation {1:} wrt excitation energy is {0:}'.format(testplaczek.dalpha_dE_real + 1j * testplaczek.dalpha_dE_imag, i))
print('The derivative of the polarzability contribution of excitation {1:} wrt transition dipole is {0:}'.format(testplaczek.dalpha_dmu_real + 1j * testplaczek.dalpha_dmu_imag, i))


