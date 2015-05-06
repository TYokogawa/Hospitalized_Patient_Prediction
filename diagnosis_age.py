categ = ['Circulatory', 'Respiratory', 'Digestive', 'Diabetes', 'Injury', 'Musculoskeletal', 'Genitourinary', 'Neoplasms', 'Mental','Other', 'No_data', 'External causes', 'Obesity']

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
            newdiag.append(categ[0])
        elif diag_num ==785:       
            newdiag.append(categ[0])
        elif diag_num >=460 and diag_num <= 519:       
            newdiag.append(categ[1])
        elif diag_num ==786:       
            newdiag.append(categ[1])
        elif diag_num >=520 and diag_num <= 579:       
            newdiag.append(categ[2])
        elif diag_num ==787:       
            newdiag.append(categ[2])
        elif diag_num >=250 and diag_num < 251:       
            newdiag.append(categ[3])
        elif diag_num >=800 and diag_num <= 999:       
            newdiag.append(categ[4])
        elif diag_num >=710 and diag_num <= 739:       
            newdiag.append(categ[5])
        elif diag_num >=580 and diag_num <= 629:       
            newdiag.append(categ[6])
        elif diag_num ==788:       
            newdiag.append(categ[6])
        elif diag_num >=140 and diag_num <= 239:       
            newdiag.append(categ[7])
        elif diag_num ==780 or diag_num == 781 or diag_num == 784:       
            newdiag.append(categ[7])
        elif diag_num >=790 and diag_num <= 799:       
            newdiag.append(categ[7])
        elif diag_num >=240 and diag_num < 250:       
            newdiag.append(categ[7])
        elif diag_num >= 251 and diag_num <= 279:       
            newdiag.append(categ[7])
        elif diag_num >=680 and diag_num <= 709:       
            newdiag.append(categ[7])  
        elif diag_num ==782:       
            newdiag.append(categ[7])
        elif diag_num >=1 and diag_num <= 139 and diag_num !=38:       
            newdiag.append(categ[7])
        elif diag_num ==38:       
            newdiag.append(categ[12])            
        elif diag_num >=290 and diag_num <= 319:       
            newdiag.append(categ[8])    
        elif diag_num ==0:       
            newdiag.append(categ[11])  
        elif diag_num ==0.5:                  
            newdiag.append(categ[10])
        else:
            newdiag.append(categ[9])
        assert len(newdiag) == i+1
    return newdiag


def rename_age(ddata,colnum):
    newage = []
    diag_num=0
    dage = ddata.iloc[:,colnum]
    for i in range(len(ddata)):
        try:
            if dage.iloc[i] == '?':
                newage.append(0)   
            elif dage.iloc[i] == '[10-20)':      
                newage.append(int(15))
            elif dage.iloc[i] == '[20-30)':      
                newage.append(int(25))
            elif dage.iloc[i] == '[30-40)':      
                newage.append(int(35))
            elif dage.iloc[i] == '[40-50)':      
                newage.append(int(45))
            elif dage.iloc[i] == '[50-60)':      
                newage.append(int(55))
            elif dage.iloc[i] == '[60-70)':      
                newage.append(int(65))
            elif dage.iloc[i] == '[70-80)':      
                newage.append(int(75))
            elif dage.iloc[i] == '[80-90)':      
                newage.append(int(85))
            elif dage.iloc[i] == '[90-100)':      
                newage.append(int(95))
            else:
                newage.append(0) 
        except:
            pass

        assert len(newage) == i+1  
    return newage
