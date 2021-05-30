import numpy as np

class excitanal(object):
  def __init__(self, filename, threshmo, threshexcit):
    ## read the excitation output of ADF
    f = open(filename)
    f1 = f.readlines()
    f.close()
    ## read the index, energy, oscillator strength, transition dipole moment of each excitation
    self.excit = {}
    for i in range(len(f1)):
      if 'Transition dipole moments mu' in f1[i]:
        ii = 0
        while True:
          if any(char.isdigit() for char in f1[ii+i+5]):
            index = int(f1[ii+i+5].strip('\n').split()[0])
            energy =  float(f1[ii+i+5].strip('\n').split()[1]) # energy in a.u.
            osci = float(f1[ii+i+5].strip('\n').split()[2])
            dipole =  np.array([float(f1[ii+i+5].strip('\n').split()[3]),float(f1[ii+i+5].strip('\n').split()[4]),float(f1[ii+i+5].strip('\n').split()[5])]) # dipole in a.u.
            self.excit.update({index : (energy, osci, dipole)})
            ii = ii + 1
          else:
            break

    ## call moanal to classify the MOs 
    from adfexcit.moanal import moanal
    test = moanal(filename, threshmo)
    ## locate the block which contains the information of the components of each excitation
    for i in range(len(f1)):
      if 'Major MO -> MO transitions for the above excitations' in f1[i]:
        start = i + 9
        break
    ii = 0
    while True:
      ii += 1
      if 'All SINGLET-SINGLET excitation energies' in f1[start+ii]:
        end = start + ii -2
        break
    ## each excitation contains multiple transitions between MOs
    self.excitlist = []
    self.translist = []
    self.wgtlist = []
    for i in range(start, end):
      if len(f1[i]) > 7:
        self.excitlist.append(int(f1[i].strip('\n').split()[0].strip(':')))
        self.translist.append( (f1[i].strip('\n').split()[1], f1[i].strip('\n').split()[3]) )
        self.wgtlist.append(float( f1[i].strip('\n').split()[4] )) ## weights of transitions of each excitation
    ## identify the class (belongs to molecule or cluster) of MOs involved in transitions
    self.transcompolist = []
    for i in range(len(self.translist)):
      if self.translist[i][0] in test.mocompo.keys() and self.translist[i][1] in test.mocompo.keys():
        self.transcompolist.append((test.mocompo[self.translist[i][0]] , test.mocompo[self.translist[i][1]] )) ## e.g. transition 3a -> 12a, given 3a belongs to mol and 12a belongs to clu, the transiiton will be rewritten as mol -> clu
    
    self.transclasslist = []
    ''' 
    classify the transitions (mol: transitions in the molecule, int: transitions between the molecule and the cluster, clu: transitions in the cluster)
    e.g. mol -> mol is classified as mol, mol -> clu is classified as int, clu -> clu is classfied as clu
    '''
    for i in range(len(self.translist)):
      if self.translist[i][0] in test.moclass.keys() and self.translist[i][1] in test.moclass.keys():
        if   test.moclass[self.translist[i][0]] == 'mol' and test.moclass[self.translist[i][1]] == 'mol':
          self.transclasslist.append('mol')
        elif test.moclass[self.translist[i][0]] == 'clu' and test.moclass[self.translist[i][1]] == 'clu':
          self.transclasslist.append('clu')
        elif test.moclass[self.translist[i][0]] == 'mol' and test.moclass[self.translist[i][1]] == 'clu':
          self.transclasslist.append('int')
        elif test.moclass[self.translist[i][0]] == 'clu' and test.moclass[self.translist[i][1]] == 'mol':
          self.transclasslist.append('int')
        elif test.moclass[self.translist[i][0]] == 'int' or  test.moclass[self.translist[i][1]] == 'int':
          self.transclasslist.append('int')
      else:
        self.transclasslist.append('none')
    
    self.excitclass = {}
    self.excitcompo = {}
    self.excittrans = {}
    ## sum the weights of transitions belonging to the same class
    for i in range(1, max(self.excitlist)+1):
      mol = 0.0
      clu = 0.0
      inter = 0.0
      temp = [] ## a temporary list for containing the transition and its weights
      for j in range(len(self.excitlist)):
        if self.excitlist[j] == i:
          temp.append((self.translist[j], self.wgtlist[j]))
          if self.transclasslist[j] == 'mol':
            mol += self.wgtlist[j]
          elif self.transclasslist[j] == 'clu':
            clu += self.wgtlist[j]
          else:
            inter += self.wgtlist[j]

      self.excitcompo.update({i:(mol, inter, clu)})
      ## e.g. an excitation has transtions 30% in the molecule (mol), 40% between fragments (int) and 30% in the cluster (clu)
      self.excittrans.update({i: temp}) ## the weights before summed are stored here, seldom used but useful for advanced analysis

      ## classify the excitation by comparing the percentages of transition classes with the given threshold value
      ## if one excitation has 60% transitions in the cluster, given the threshold = 0.5 the excitation is classified as clu
      if abs(mol) > threshexcit:
        self.excitclass.update({i: 'mol'})
      elif abs(clu) > threshexcit:
        self.excitclass.update({i: 'clu'})
      else:
        self.excitclass.update({i: 'int'})
    
