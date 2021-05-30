from adfexcit.excitanal import *
print('========')
print('Two state model helps to estimate the chemical enhancements by comparing the HUMO-LUMO gaps of molecules and lowest charge transfer excitation energies of SERS systems.')
print('More information about the two state model is available from paper Understanding the Molecule−Surface Chemical Coupling in SERS, J. Am. Chem. Soc., 131, 4090')

print('Example system: CO-Ag4.')
print('In this example, threshold=0.6 is applied for classifying the MOs and threshold=0.5 is applied for classifying the excitations')
print('========')


print('Use excitanal script to search for the lowest charge transfer excitation.')
print('Searching criteria: the class of excitations is int;  the excitations have nontrivial oscillator strength; the excitations have nontrivial transition dipole moment in the molecule-cluster direction.')
test = excitanal('excit_COAg4.out', 0.6, 0.5)
candidates = []
for i in test.excitclass.keys():
  if i < 50: ## low excitations 
    if test.excitclass[i] == 'int' and test.excit[i][1] > 0.001 and test.excit[i][2][2] > 1e-3: 
      candidates.append(i)


print('The found excitations are: ')
for i in candidates:
  print(i, test.excit[i])

print('Say we select excitation', candidates[0])
omegae = test.excit[candidates[0]][0]
print('The lowest charge transfer excitation energy omegae / a.u. is', omegae)


omegax = 0.25444 ## unit: a.u.

print('The HOMO-LUMO gap of CO (which can be obtained from a single point calculation), named omegax / a.u. is', omegax)

print('The enhancement factor for CO on Ag4 can be estimated as a product of a prefactor and (omegax / omegae)**4.')
print('The prefactor can be canceled out when comparing EFs among similar systems such as CO-Ag4 under electric fields.')




