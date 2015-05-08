categ = ['Circulatory', 'Respiratory', 'Digestive', 'Diabetes', 'Injury', 'Musculoskeletal', 'Genitourinary',
         'Neoplasms', 'Mental','Other', 'No_data', 'External causes', 'Obesity BODY MASS INDEX 38.0-38.9',
'CONGESTIVE HEART FAILURE UNSPECIFIED','CORONARY ATHEROSCLEROSIS',
'RESPIRATORY ABNORMALITY UNSPECIFIED','ACUTE MYOCARDIAL INFARCTION OF ANTEROLATERAL WALL EPISODE',
'PNEUMONIA ORGANISM UNSPECIFIED','PAROXYSMAL SUPRAVENTRICULAR TACHYCARDIA',
'SIMPLE CHRONIC BRONCHITIS','OSTEOARTHROSIS GENERALIZED INVOLVING UNSPECIFIED SITE',
'CELLULITIS AND ABSCESS OF FACE','CEREBRAL THROMBOSIS WITHOUT CEREBRAL INFARCTION',
'COMA,DIZZINESS,FEVER,SLEEP','MECHANICAL COMPLICATIONS OF UNSPECIFIED CARDIAC DEVICE IMPLANT AND GRAFT',
'HYPEROSMOLALITY AND/OR HYPERNATREMIA','DIABETES OTHER SPECIFIED MANIFESTATIONS',
'URINARY TRACT INFECTION SITE NOT SPECIFIED','ACUTE KIDNEY FAILURE WITH LESION OF TUBULAR NECROSIS',
'DIABETES NEUROLOGICAL MANIFESTATIONS, TYPE II OR UNSPECIFIED TYPE',
'PULMONARY COLLAPSE','FRACTURE OF UNSPECIFIED INTRACAPSULAR SECTION OF NECK OF FEMUR CLOSED',
'ACUTE PANCREATITIS','EXTRINSIC ASTHMA UNSPECIFIED',
'BASILAR ARTERY SYNDROME','DIVERTICULOSIS OF SMALL INTESTINE (WITHOUT HEMORRHAGE)',
'CALCULUS OF GALLBLADDER','BIPOLAR I DISORDER, SINGLE MANIC EPISODE, UNSPECIFIED',
'INTUSSUSCEPTION','DIABETES PERIPHERAL CIRCULATORY DISORDERS, TYPE II OR UNSPECIFIED TYPE',
'DIABETES WITH KETOACIDOSIS, TYPE I [JUVENILE TYPE]',
'ATHEROSCLEROSIS OF AORTA']

def rename_diagno(ddata,colnum):
    newdiag = []
    diag_num=0
    diag1 = ddata.iloc[:,colnum]
    for i in range(len(ddata)):

        try:
            if diag1.iloc[i] == '?':
                diag_num =0.5
            else:
                diag_num = float(diag1.iloc[i])
        except:
            diag_num =0
        if diag_num >=390 and diag_num <= 459:
            if diag_num ==428.00:
                newdiag.append(categ[13])
            elif diag_num ==414.00:
                newdiag.append(categ[14])
            elif diag_num ==410.00:
                newdiag.append(categ[16])
            elif diag_num ==427.00:
                newdiag.append(categ[18])
            elif diag_num ==434.00:
                newdiag.append(categ[22])
            elif diag_num ==435.00:
                newdiag.append(categ[34])
            elif diag_num ==440.00:
                newdiag.append(categ[41])
            else:
                newdiag.append(categ[0])
        elif diag_num ==785:       
            newdiag.append(categ[0])
        elif diag_num >=460 and diag_num <= 519:       
            if diag_num ==486.00:
                newdiag.append(categ[17])
            elif diag_num ==491.00:
                newdiag.append(categ[19])
            elif diag_num ==493.00:
                newdiag.append(categ[33])
            else:
                newdiag.append(categ[1])
        elif diag_num ==786:       
            newdiag.append(categ[15])
        elif diag_num ==518.00:       
            newdiag.append(categ[30])          
        elif diag_num >=520 and diag_num <= 579:
            if diag_num ==577.00:
                newdiag.append(categ[32])
            elif diag_num ==562.00:
                newdiag.append(categ[35])
            elif diag_num ==574.00:
                newdiag.append(categ[36])
            elif diag_num ==560.00:
                newdiag.append(categ[38])
            else:
                newdiag.append(categ[2])
        elif diag_num ==787:       
            newdiag.append(categ[2])
        elif diag_num >=250 and diag_num < 251:
            if diag_num ==250.80:
                newdiag.append(categ[26])
            elif diag_num ==250.60:
                newdiag.append(categ[29])
            elif diag_num ==250.70:
                newdiag.append(categ[39])
            elif diag_num ==250.13:
                newdiag.append(categ[40])
            else:
                newdiag.append(categ[3])
        elif diag_num >=800 and diag_num <= 999:
            if diag_num ==996.00:
                newdiag.append(categ[24])
            elif diag_num ==820.00:
                newdiag.append(categ[31])            
            else:
                newdiag.append(categ[4])
        elif diag_num >=710 and diag_num <= 739:
            if diag_num ==715.00:
                newdiag.append(categ[20])
            else:
                newdiag.append(categ[5])
        elif diag_num >=580 and diag_num <= 629:
            if diag_num ==599.00:
                newdiag.append(categ[27])
            elif diag_num ==584.00:
                newdiag.append(categ[28])
            else:
                newdiag.append(categ[6])
        elif diag_num ==788:       
            newdiag.append(categ[6])
        elif diag_num >=140 and diag_num <= 239:       
            newdiag.append(categ[7])
        elif diag_num ==780: 
            newdiag.append(categ[23])
        elif diag_num == 781 or diag_num == 784: 
            newdiag.append(categ[7])
        elif diag_num >=790 and diag_num <= 799:       
            newdiag.append(categ[7])
        elif diag_num >=240 and diag_num < 250:       
            newdiag.append(categ[7])
        elif diag_num >= 251 and diag_num <= 279:
            if diag_num ==276.00:
                newdiag.append(categ[25])
            else:
                newdiag.append(categ[7])            
        elif diag_num >=680 and diag_num <= 709:
            if diag_num ==682.00:
                newdiag.append(categ[21])
            else:
                newdiag.append(categ[7])
        elif diag_num ==782:       
            newdiag.append(categ[7])
        elif diag_num >=1 and diag_num <= 139 and diag_num !=38:       
            newdiag.append(categ[7])
        elif diag_num ==38:       
            newdiag.append(categ[12])            
        elif diag_num >=290 and diag_num <= 319:
            if diag_num ==296.00:
                newdiag.append(categ[37])
            else:
                newdiag.append(categ[8])
        elif diag_num ==0:       
            newdiag.append(categ[11])  
        elif diag_num ==0.5:                  
            newdiag.append(categ[10])
        else:
            newdiag.append(categ[9])
        #print i
        assert len(newdiag) == i+1
    return newdiag
    
