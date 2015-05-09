
admid = ['Emergency','Urgent','Elective','Newborn','Trauma Center','Not Available']

def rename_admissionid(ddata,colnum):
    newadmid = []
    dadm = ddata.iloc[:,colnum]
    for i in range(len(ddata)):
        try:
            if dadm.iloc[i] == '?':
                newadmid.append(admid[5])  
            elif dadm.iloc[i] ==1:      
                newadmid.append(admid[0])
            elif dadm.iloc[i] ==2:      
                newadmid.append(admid[1])
            elif dadm.iloc[i] ==3:      
                newadmid.append(admid[2])
            elif dadm.iloc[i] ==4:      
                newadmid.append(admid[3])
            elif dadm.iloc[i] ==5:      
                newadmid.append(admid[5])
            elif dadm.iloc[i] ==6:      
                newadmid.append(admid[5])
            elif dadm.iloc[i] ==7:      
                newadmid.append(admid[4])
            else:
                newadmid.append(admid[5]) 
        except:
            pass

        assert len(newadmid) == i+1  
    return newadmid



discid = ['Discharged to home',
          'Discharged/transferred to another short term hospital',
          'Discharged/transferred to SNF(skilled nursing facility)',
          'Discharged/transferred to ICF(Intermediate Care Facility)',
          'Discharged/transferred to another type of inpatient care institution',
          'Discharged/transferred to home with home health service',
          'Left AMA (Discharge against medical advice)',
          'Discharged/transferred to home under care of Home IV (intravenous) provider',
          'Expired (death)',
          'Discharged to Hospice',
          'Discharged/transferred within this institution',
          'Discharged/transferred/referred to a psychiatric hospital',
          'Not Available']



def rename_dischargeid(ddata,colnum):
    newdiscid = []
    disc = ddata.iloc[:,colnum]
    for i in range(len(ddata)):
        try:
            if disc.iloc[i] == '?':
                newdiscid.append(discid[12])  
            elif disc.iloc[i] ==1:      
                newdiscid.append(discid[0])
            elif disc.iloc[i] ==2:      
                newdiscid.append(discid[1])
            elif disc.iloc[i] ==3:      
                newdiscid.append(discid[2])                
            elif disc.iloc[i] ==4:      
                newdiscid.append(discid[3])
            elif disc.iloc[i] ==5:      
                newdiscid.append(discid[4])
            elif disc.iloc[i] ==6:      
                newdiscid.append(discid[5])  
            elif disc.iloc[i] ==7:      
                newdiscid.append(discid[6])
            elif disc.iloc[i] ==8:      
                newdiscid.append(discid[7])
            elif disc.iloc[i] ==9:      
                newdiscid.append(discid[11])  
            elif disc.iloc[i] ==10:      
                newdiscid.append(discid[4])
            elif disc.iloc[i] ==11:      
                newdiscid.append(discid[8])
            elif disc.iloc[i] ==12:      
                newdiscid.append(discid[12])
            elif disc.iloc[i] ==13:      
                newdiscid.append(discid[9])                
            elif disc.iloc[i] ==14:      
                newdiscid.append(discid[9])
            elif disc.iloc[i] ==15:      
                newdiscid.append(discid[10])
            elif disc.iloc[i] ==16:      
                newdiscid.append(discid[4])  
            elif disc.iloc[i] ==17:      
                newdiscid.append(discid[12])
            elif disc.iloc[i] ==18:      
                newdiscid.append(discid[12])
            elif disc.iloc[i] ==19:      
                newdiscid.append(discid[8])  
            elif disc.iloc[i] ==20:      
                newdiscid.append(discid[8])
            elif disc.iloc[i] ==21:      
                newdiscid.append(discid[12])
            elif disc.iloc[i] ==22:      
                newdiscid.append(discid[12])
            elif disc.iloc[i] ==23:      
                newdiscid.append(discid[12])                
            elif disc.iloc[i] ==24:      
                newdiscid.append(discid[12])
            elif disc.iloc[i] ==25:      
                newdiscid.append(discid[12])
            elif disc.iloc[i] ==26:      
                newdiscid.append(discid[12])  
            elif disc.iloc[i] ==27:      
                newdiscid.append(discid[12])
            elif disc.iloc[i] ==28:      
                newdiscid.append(discid[11])
            elif disc.iloc[i] ==29:      
                newdiscid.append(discid[12])  
            else:
                newdiscid.append(discid[12]) 
        except:
            pass

        assert len(newdiscid) == i+1  
    return newdiscid


adsource = ['Physician Referral',
          'Clinic Referral',
          'HMO Referral',
          'Transfer from a hospital',
          'Transfer from a Skilled Nursing Facility (SNF)',
          'Transfer from another health care facility',
          'Emergency Room',
          'Court/Law Enforcement',
          'Not Available',
          'Transfer from critial access hospital',
          'Delivery/Baby', 'Transfer/readmission From Another Home Health Agency']


def rename_adsourceid(ddata,colnum):
    newadsoid = []
    adso = ddata.iloc[:,colnum]
    for i in range(len(ddata)):
        try:
            if adso.iloc[i] == '?':
                newadsoid.append(adsource[8])  
            elif adso.iloc[i] ==1:      
                newadsoid.append(adsource[0])
            elif adso.iloc[i] ==2:      
                newadsoid.append(adsource[1])
            elif adso.iloc[i] ==3:      
                newadsoid.append(adsource[2])  
            elif adso.iloc[i] ==4:      
                newadsoid.append(adsource[3])
            elif adso.iloc[i] ==5:      
                newadsoid.append(adsource[4])
            elif adso.iloc[i] ==6:      
                newadsoid.append(adsource[5])  
            elif adso.iloc[i] ==7:      
                newadsoid.append(adsource[6])
            elif adso.iloc[i] ==8:      
                newadsoid.append(adsource[7])
            elif adso.iloc[i] ==9:      
                newadsoid.append(adsource[8])  
            elif adso.iloc[i] ==10:      
                newadsoid.append(adsource[9])
            elif adso.iloc[i] ==11:      
                newadsoid.append(adsource[10])
            elif adso.iloc[i] ==12:      
                newadsoid.append(adsource[10]) 
            elif adso.iloc[i] ==13:      
                newadsoid.append(adsource[10])
            elif adso.iloc[i] ==14:      
                newadsoid.append(adsource[10])
            elif adso.iloc[i] ==15:      
                newadsoid.append(adsource[8])  
            elif adso.iloc[i] ==16:      
                newadsoid.append(adsource[8])
            elif adso.iloc[i] ==17:      
                newadsoid.append(adsource[8])
            elif adso.iloc[i] ==18:      
                newadsoid.append(adsource[11]) 
            elif adso.iloc[i] ==19:      
                newadsoid.append(adsource[11])
            elif adso.iloc[i] ==20:      
                newadsoid.append(adsource[8])
            elif adso.iloc[i] ==21:      
                newadsoid.append(adsource[8])  
            elif adso.iloc[i] ==22:      
                newadsoid.append(adsource[8])
            elif adso.iloc[i] ==23:      
                newadsoid.append(adsource[10])
            elif adso.iloc[i] ==24:      
                newadsoid.append(adsource[10])
            elif adso.iloc[i] ==25:      
                newadsoid.append(adsource[3])
            elif adso.iloc[i] ==26:      
                newadsoid.append(adsource[8])
            else:
                newadsoid.append(adsource[8]) 
        except:
            pass

        assert len(newadsoid) == i+1  
    return newadsoid
