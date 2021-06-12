import unittest
from moanal import *
from excitanal import *
from placzek import *

class testadfexcit(unittest.TestCase):
  def setUp(self):
    self.mo = moanal('unitTests/excit_COAg4.out', 0.6)
    self.excit = excitanal('unitTests/excit_COAg4.out', 0.6, 0.6)
    self.placzek = placzek(0.004, self.excit.excit[3][0], self.excit.excit[3][0], self.excit.excit[3][2][0])

  def test_mo(self):
    self.assertLess(abs(self.mo.mocompo['1a'][0] - (-30.652)), 1e-10, 'incorrect MO energy')
    self.assertLess(abs(self.mo.mocompo['1a'][1] - 2), 1e-10, 'incorrect MO occupation')
    self.assertLess(abs(self.mo.mocompo['1a'][2] - 1.0135), 1e-10, 'incorrect mol percent of MO')
    self.assertLess(abs(self.mo.mocompo['1a'][3] - 0), 1e-10, 'incorrect clu percent of MO')
    self.assertEqual(self.mo.moclass['1a'], 'mol', 'incorrect MO class')
  def test_excit(self):
    self.assertLess(abs(self.excit.excit[1][0] - 0.468080333499E-01), 1e-10, 'incorrect excitation energy')
    self.assertLess(abs(self.excit.excit[1][1] - 0.73587E-03), 1e-10, 'incorrect oscillator strength')
    self.assertLess(abs(self.excit.excit[1][2][0] - 0.110641565511), 1e-10, 'incorrect transition dipole in x direction')
    self.assertLess(abs(self.excit.excit[1][2][1] - (-0.106488838883)), 1e-10, 'incorrect transition dipole in y direction')
    self.assertLess(abs(self.excit.excit[1][2][2] - (-0.324788357009E-06)), 1e-10, 'incorrect transition dipole in z direction')
    self.assertLess(abs(self.excit.excitcompo[1][0] - 0), 1e-10, 'incorrect mol percent of excitation')
    self.assertLess(abs(self.excit.excitcompo[1][1] - 0.9990), 1e-10, 'incorrect int percent of excitation')
    self.assertLess(abs(self.excit.excitcompo[1][2] - 0), 1e-10, 'incorrect clu percent of excitation')
    self.assertEqual(self.excit.excitclass[1], 'int', 'incorrect excitation class')
    self.assertEqual(self.excit.excittrans[1][0][0], ('27a', '28a'), 'incorrect transition')
    self.assertLess(abs(self.excit.excittrans[1][0][1] - 0.9958), 1e-10, 'incorrect transition percent')
    self.assertEqual(self.excit.excittrans[1][1][0], ('26a', '28a'), 'incorrect transition')
    self.assertLess(abs(self.excit.excittrans[1][1][1] - 0.0032), 1e-10, 'incorrect transition percent')
  def test_placzek(self):
    self.assertLess(abs(self.placzek.alpha_real - 0.12245288560805735), 1e-10, 'incorrect polarizability, real part')
    self.assertLess(abs(self.placzek.alpha_imag - 4.04009919915069), 1e-10, 'incorrect polarizability, real part')
    self.assertLess(abs(self.placzek.dalpha_dE_real - 1010.0265030095543), 1e-10, 'incorrect polarizability, real part')
    self.assertLess(abs(self.placzek.dalpha_dE_imag - 0.056194554558612705), 1e-10, 'incorrect polarizability, real part')
    self.assertLess(abs(self.placzek.dalpha_dmu_real - 1.9256334296789077), 1e-10, 'incorrect polarizability, real part')
    self.assertLess(abs(self.placzek.dalpha_dmu_imag - 63.53259899488761), 1e-10, 'incorrect polarizability, real part')


if __name__ == '__main__':
  unittest.main()


