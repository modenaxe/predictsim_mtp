def getSettings_predictsim_no_mtp():
    settings = {
            # lower cost than "2"
            '0': {'contactConfiguration': 'specific',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4},
            '1': {'contactConfiguration': 'generic',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4},
            '2': {'contactConfiguration': 'specific',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4},
            # lower cost than "1"
            '3': {'contactConfiguration': 'generic',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4},
            # lower cost than "6", lowest cost among 0,2,4,6
            '4': {'contactConfiguration': 'specific',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 100,
                  'tol': 4},
            # lower cost than "7" (almost =), lowest cost among 1,3,5,7
            '5': {'contactConfiguration': 'generic',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 100,
                  'tol': 4},
            '6': {'contactConfiguration': 'specific',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 100,
                  'tol': 4},
            '7': {'contactConfiguration': 'generic',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 100,
                  'tol': 4}}
    return settings

def getSettings_predictsim_mtp():
    settings = {
            # lower cost than "1"
            '0': {'contactConfiguration': 'specific',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000},            
            '1': {'contactConfiguration': 'specific',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000},                  
            '2': {'contactConfiguration': 'specific',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 100,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000},   
            # lower cost than "2", lowest cost among 0-3
            '3': {'contactConfiguration': 'specific',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 100,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000},
            # lower cost than 5
            '4': {'contactConfiguration': 'specific',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': True,
                  'AchillesTendonCompliance': 0.8*35,
                  'mtpExcitationTerm': 1000000},            
            '5': {'contactConfiguration': 'specific',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': True,
                  'AchillesTendonCompliance': 0.8*35,
                  'mtpExcitationTerm': 1000000},
            '6': {'contactConfiguration': 'generic',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000},  
            # lower cost than 6
            '7': {'contactConfiguration': 'generic',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000},
            # lower cost than 9
            '8': {'contactConfiguration': 'specific',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': True,
                  'AchillesTendonCompliance': 0.6*35,
                  'mtpExcitationTerm': 1000000},            
            '9': {'contactConfiguration': 'specific',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': True,
                  'AchillesTendonCompliance': 0.6*35,
                  'mtpExcitationTerm': 1000000},
            '10': {'contactConfiguration': 'specific',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': True,
                  'AchillesTendonCompliance': 0.4*35,
                  'mtpExcitationTerm': 1000000},  
            # lower cost than 10 (almost =)
            '11': {'contactConfiguration': 'specific',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': True,
                  'AchillesTendonCompliance': 0.4*35,
                  'mtpExcitationTerm': 1000000},
            '12': {'contactConfiguration': 'generic',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 100,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000}, 
            # lower cost than 12, lowest cost among 6-7-12-13
            '13': {'contactConfiguration': 'generic',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 100,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000},
            # lower cost than 15
            '14': {'contactConfiguration': 'generic_cm4',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000},  
            '15': {'contactConfiguration': 'generic_cm4',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000},
            '16': {'contactConfiguration': 'generic_cm4',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 100,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000},
            # lower cost than 16, lowest cost among 14-15-16-17
            '17': {'contactConfiguration': 'generic_cm4',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 100,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000},
            # lower cost than 19
            '18': {'contactConfiguration': 'specific',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 10000},            
            '19': {'contactConfiguration': 'specific',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 10000},
            '20': {'contactConfiguration': 'specific',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000000},            
            '21': {'contactConfiguration': 'specific',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1000000000},
            '22': {'contactConfiguration': 'specific',
                  'guessType': 'dataDriven',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1},            
            '23': {'contactConfiguration': 'specific',
                  'guessType': 'quasiRandom',
                  'targetSpeed': 1.33,
                  'N': 50,
                  'tol': 4,
                  'adjustAchillesTendonCompliance': False,
                  'mtpExcitationTerm': 1}}
    return settings
