class moanal(object):

  def __init__(self, filename, thresh):
    ## read the output file of ADF
    f = open(filename) 
    f1 = f.readlines()
    f.close()
    ## locate the block which contains the infor of MOs
    for i in range(len(f1)):
      if 'List of all MO' in f1[i]:
        start = i + 13
    
    ii = 0
    while True:
      ii = ii + 1
      if '====' in f1[start+ii]:
        end = start + ii - 3
        break
    
    
    ## 'indicator' list shows the line numbers where each MO starts
    indicator = []
    for i in range(start, end):
      length = len(f1[i]) - f1[i].count(' ')
      if length > 32 and length < 55:
        indicator.append(i)
    self.mocompo = {}
    self.moclass = {}
    ## read the energy, occupation, and the weights of AOs of each MO
    for i in range(len(indicator)):
      mo = f1[indicator[i]].strip('\n').split()[2] + 'a' 
      ## ! NOTICE assuming no symmetry is applied in the calculation otherwise the labeling of MOs has to be changed !
      occ = float(f1[indicator[i]].strip('\n').split()[1])
      energy = float(f1[indicator[i]].strip('\n').split()[0])
      molper = 0.0
      cluper = 0.0
      if i < len(indicator)-1:
        temprange = range(indicator[i], indicator[i+1]) 
      else:
        temprange = range(indicator[i], end)
    
      for j in temprange:
        if f1[j].strip('\n').split()[-1] == 'core': ## the weights of core electrons are not considered
          pass
        else:
          element = f1[j].strip('\n').split()[-1]
          if element in ['C', 'H', 'O', 'N']:
            molper += (float(f1[j].strip('\n').split()[-7].strip('%')) / 100.0) ## sum the weights of AOs from the molecule
          elif element in ['Ag', 'Au']:
            cluper += (float(f1[j].strip('\n').split()[-7].strip('%')) / 100.0) ## sum the weights if AOs from the metal cluster
          else:
            print('err', element)

      self.mocompo.update({mo : (energy, occ, molper, cluper) })
      ## classify the MOs by comparing the percent of AOs from the molecule / cluster with the given threshold value
      if   abs(molper) > thresh:
        self.moclass.update({mo : 'mol'})
      elif abs(cluper) > thresh:
        self.moclass.update({mo : 'clu'})
      else:
        self.moclass.update({mo : 'int'})




