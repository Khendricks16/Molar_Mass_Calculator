# Webscraped dict
ELEMENTS_DICT = dict({'H': '1.00797', 'He': '4.00260', 'Li': '6.941',
                     'Be': '9.01218', 'B': '10.81', 'C': '12.011',
                     'N': '14.0067', 'O': '15.9994', 'F': '18.998403',
                     'Ne': '20.179', 'Na': '22.98977', 'Mg': '24.305',
                     'Al': '26.98154', 'Si': '28.0855', 'P': '30.97376',
                     'S': '32.06', 'Cl': '35.453', 'K': '39.0983',
                     'Ar': '39.948', 'Ca': '40.08', 'Sc': '44.9559',
                     'Ti': '47.90', 'V': '50.9415', 'Cr': '51.996',
                     'Mn': '54.9380', 'Fe': '55.847', 'Ni': '58.70',
                     'Co': '58.9332', 'Cu': '63.546', 'Zn': '65.38',
                     'Ga': '69.72', 'Ge': '72.59', 'As': '74.9216',
                     'Se': '78.96', 'Br': '79.904', 'Kr': '83.80',
                     'Rb': '85.4678', 'Sr': '87.62', 'Y': '88.9059',
                     'Zr': '91.22', 'Nb': '92.9064', 'Mo': '95.94',
                     'Tc': '(98)', 'Ru': '101.07', 'Rh': '102.9055',
                     'Pd': '106.4', 'Ag': '107.868', 'Cd': '112.41',
                     'In': '114.82', 'Sn': '118.69', 'Sb': '121.75',
                     'I': '126.9045', 'Te': '127.60', 'Xe': '131.30',
                     'Cs': '132.9054', 'Ba': '137.33', 'La': '138.9055',
                     'Ce': '140.12', 'Pr': '140.9077', 'Nd': '144.24',
                     'Pm': '(145)', 'Sm': '150.4', 'Eu': '151.96',
                     'Gd': '157.25', 'Tb': '158.9254', 'Dy': '162.50',
                     'Ho': '164.9304', 'Er': '167.26', 'Tm': '168.9342',
                     'Yb': '173.04', 'Lu': '174.967', 'Hf': '178.49',
                     'Ta': '180.9479', 'W': '183.85', 'Re': '186.207',
                     'Os': '190.2', 'Ir': '192.22', 'Pt': '195.09',
                     'Au': '196.9665', 'Hg': '200.59', 'Tl': '204.37',
                     'Pb': '207.2', 'Bi': '208.9804', 'Po': '(209)',
                     'At': '(210)', 'Rn': '(222)', 'Fr': '(223)',
                     'Ra': '226.0254', 'Ac': '227.0278', 'Pa': '231.0359',
                     'Th': '232.0381', 'Np': '237.0482', 'U': '238.029',
                     'Pu': '(242)', 'Am': '(243)', 'Bk': '(247)',
                     'Cm': '(247)', 'No': '(250)', 'Cf': '(251)',
                     'Es': '(252)', 'Hs': '(255)', 'Mt': '(256)',
                     'Fm': '(257)', 'Md': '(258)', 'Lr': '(260)',
                     'Rf': '(261)', 'Bh': '(262)', 'Db': '(262)',
                     'Sg': '(263)', 'Uun': '(269)', 'Uuu': '(272)',
                     'Uub': '(277)'})


def compound_convert(element: str) -> float :
    """Returns the molar mass for a elements with one subscript"""
    
    if element.find("(") == -1:
      return float(ELEMENTS_DICT[element[:-1]]) * int(element[-1])

    _collective_mass = 0
    
    for i, char in enumerate(element[1:element.index(")")]):
        if char.isdigit():
          pass
        elif char.islower():
          pass
        elif element[i+2].islower() is True and element[i+3].isdigit() is True:
            _collective_mass +=\
              float(ELEMENTS_DICT[element[i+1:i+3]]) * int(element[-1]) * int(element[i + 3])
        else:
            _collective_mass += float(ELEMENTS_DICT[char]) * int(element[-1]) * int(element[i + 2])
          
    return _collective_mass




def count_subscripts(compound: str) -> int :
    """Returns the number of subscripts from a given compound.

       - Any subscripts inside of parenthesis do not count
           ex.
               (O1H3)2 -> 1
               H1(B8Fe9)1 -> 2 """
        
    _num_subscripts = 0
    _modified_user_compound = compound
    
    while True:
      if _modified_user_compound.find("(") != -1:
        _start, _end  = _modified_user_compound.index("("), _modified_user_compound.index(")")
        _modified_user_compound = _modified_user_compound[:_start] + _modified_user_compound[_end + 1:]
      else:
        for char in _modified_user_compound:
          try:
            if int(char):
              _num_subscripts += 1
          except ValueError:
            continue

        break

    return _num_subscripts


#Gets the compound that the molar mass will be found for 
user_compound = input("Compound: ")


# Main for loop
molar_mass = 0

for i in range(count_subscripts(user_compound)):
    for char in user_compound:
        try:
            next_num = int(char)
            break
        except ValueError:
            pass
    next_num = user_compound.index(str(next_num))
    if user_compound[:next_num + 1].find("(") != -1:
      next_num = user_compound.index(")") + 1
      
    molar_mass += compound_convert(user_compound[:next_num + 1])
    user_compound = user_compound[next_num + 1:]

        
# Return final molar mass
print(molar_mass)

