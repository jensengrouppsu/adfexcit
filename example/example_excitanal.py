from adfexcit.excitanal import *
print('========')
print('Use the excitanal script to collect the index, energy, oscillator strength, transition dipole, and component of each excitation')
print('The excitanal script is designed for studies of SERS systems which consist of molecules (mol) and clusters (clu).')
print('Example system: CO-Ag4.')
print('In this example, threshold=0.6 is applied for classifying the MOs and threshold=0.5 is applied for classifying the excitations')
print('========')

test = excitanal('excit_COAg4.out', 0.6, 0.5)

print('excit is a dictionary whose structure is excitation index : (energy / a.u., oscillator strength / a.u., transition dipole / a.u. )')
print('Take excitation 3 in this system as an example')
print('Energy, oscillator strength, transition dipole of excitation 3 are', test.excit[3])
print('excitcompo is a dictionary whose structure is excitation index: (percent of transitions in the molecule, percent of transitions between fragments, percent of transitions in the cluster)')
print('The component of excitation 3 is', test.excitcompo[3])
print('excitclass is a dictionary whose structure is excitation index: class of the excitation. The meaning of the class of excitations is that excitations can happen mainly in the molecule (mol), between fragments (int), or in the cluster (clu).')
print('The class of excitation 3 is', test.excitclass[3])

