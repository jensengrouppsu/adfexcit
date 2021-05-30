from adfexcit.moanal import *
print('========')
print('Use the moanal script to collect the index, energy, weights of AOs of each MO.')
print('The moanal script is designed for studies of SERS systems which consist of molecules (mol) and clusters (clu).')
print('Example system: CO-Ag4.')
print('AOs belonging to same fragments (mol or clu) are grouped and their weights are summed')
print('In this example, threshold=0.6 is applied for classifying the MOs (mol or clu).')
test = moanal('excit_COAg4.out', thresh=0.6)
print('========')
print('mocompo is a dictionary whose structure is (mo index : (energy / a.u., occupation, percent of AOs in mol, percent of AOs in clu))')
print('Take MO 3a in this system as an example')
print('mocompo of 3a is', test.mocompo['3a'])
print('moclass is a dictionary whose structure is (mo index: moclass)')
print('moclass of 3a is', test.moclass['3a'])





