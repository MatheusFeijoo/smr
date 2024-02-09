import data
import streamlit as st


def Leadership(df_pol, dfL1Best, dfL2Best, dfL3Best, dfL4Best):

    L1S1 = (((df_pol['L1Q1'])/(data.dfL1Best[0]-2)>=1 and (1,) or (0,))[0])
    L1M1 = (((df_pol['L1Q1'])/(data.dfL1Best[0]-2)>=1 and (((df_pol['L1Q1']-1)/(data.dfL1Best[0]-2)<1 and ((df_pol['L1Q1'])/(data.dfL1Best[0]-1),) or (1,))[0],) or (0,))[0])
    L1A1 = (((df_pol['L1Q1'])/(data.dfL1Best[0]-2)>=1 and ((df_pol['L1Q1'])/(data.dfL1Best[0]),) or (0,))[0])
    L1Q2MEAN = (df_pol['L1Q2'] + df_pol['L1Q3'])/2
    L1S2 = (((L1Q2MEAN)/(data.dfL1Best[1]-3)>=1 and (1,) or (0,))[0])
    L1M2 = (((L1Q2MEAN)/(data.dfL1Best[1]-3)>=1 and (((L1Q2MEAN-1)/(data.dfL1Best[1]-3)>1 and (1,) or ((L1Q2MEAN)/(data.dfL1Best[1]-2),))[0],) or (0,))[0])
    L1A2 = (((L1Q2MEAN)/(data.dfL1Best[1]-3)>=1 and (((L1Q2MEAN-1)/(data.dfL1Best[1]-2)>1 and (1,) or ((L1Q2MEAN)/(data.dfL1Best[1]-1),))[0],) or (0,))[0])
    L1R2 = (((L1Q2MEAN)/(data.dfL1Best[1]-3)>=1 and (((L1Q2MEAN-1)/(data.dfL1Best[1]-1)>1 and (1,) or ((L1Q2MEAN)/(data.dfL1Best[1]),))[0],) or (0,))[0])
    L1T2 = ((L1R2>=0.75 and (((df_pol['L1Q5']>1 and ((df_pol['L1Q5'])/(data.dfL1Best[3]),) or (0,))[0]),) or (0,))[0])
    L1M3 = ((df_pol['L1Q4']==0 and (0,) or ((df_pol['L1Q4'])/(data.dfL1Best[2]),))[0])
    #L2
    L2M1 = (((((df_pol['L2Q1'])/(data.dfL2Best[0]-3)>=1 and (1,) or (0,))[0])+(((df_pol['L2Q2'])/(data.dfL2Best[1]-3)>=1 and (1,) or (0,))[0]))/2)
    L2A1 = (((((df_pol['L2Q1'])/(data.dfL2Best[0]-3)>=1 and (((df_pol['L2Q1']-1)/(data.dfL2Best[0]-3)>1 and (1,) or ((df_pol['L2Q1'])/(data.dfL2Best[0]-2),))[0],) or (0,))[0])+(((df_pol['L2Q2'])/(data.dfL2Best[1]-3)>=1 and (((df_pol['L2Q2']-1)/(data.dfL2Best[1]-3)>1 and (1,) or ((df_pol['L2Q2'])/(data.dfL2Best[1]-2),))[0],) or (0,))[0]))/2)
    L2R1 = (((((df_pol['L2Q1'])/(data.dfL2Best[0]-3)>=1 and (((df_pol['L2Q1']-1)/(data.dfL2Best[0]-2)>1 and (1,) or ((df_pol['L2Q1'])/(data.dfL2Best[0]-1),))[0],) or (0,))[0])+(((df_pol['L2Q2'])/(data.dfL2Best[1]-3)>=1 and (((df_pol['L2Q2']-1)/(data.dfL2Best[1]-2)>1 and (1,) or ((df_pol['L2Q2'])/(data.dfL2Best[1]-1),))[0],) or (0,))[0]))/2)
    L2T1 = (((((df_pol['L2Q1'])/(data.dfL2Best[0]-3)>=1 and (((df_pol['L2Q1']-1)/(data.dfL2Best[0]-1)>1 and (1,) or ((df_pol['L2Q1'])/(data.dfL2Best[0]),))[0],) or (0,))[0])+(((df_pol['L2Q2'])/(data.dfL2Best[1]-3)>=1 and (((df_pol['L2Q2']-1)/(data.dfL2Best[1]-1)>1 and (1,) or ((df_pol['L2Q2'])/(data.dfL2Best[1]),))[0],) or (0,))[0]))/2)
    #L3
    L3S1 = (((df_pol['L3Q1'])/(data.dfL3Best[0])>=1 and (1,) or (0,))[0])
    L3M1 = (((df_pol['L3Q1'])/(data.dfL3Best[0]-1)>=1 and (((df_pol['L3Q1'])/(data.dfL3Best[0])),) or (0,))[0])
    L3T1 = ((L3M1>=0.75 and ((df_pol['L3Q1']>=3 and (((df_pol['L3Q3']>1 and (((df_pol['L3Q3'])/(data.dfL3Best[2])),) or (0,))[0]),) or (0,))[0],) or (0,))[0])
    L3M2 = ((df_pol['L3Q2']>1 and ((((df_pol['L3Q2'])/(data.dfL3Best[1]-1)>=1 and (1,) or ((df_pol['L3Q2'])/(data.dfL3Best[1]),))[0]),) or (0,))[0])
    L3A2 = ((((df_pol['L3Q2']>1 and ((((df_pol['L3Q2']-1)/(data.dfL3Best[1]-1)>=1 and (1,) or ((df_pol['L3Q2'])/data.dfL3Best[1],))[0]),) or (0,))[0])+((df_pol['L3Q4']>1 and ((((df_pol['L3Q4'])/(data.dfL3Best[3]-1)>=1 and (1,) or ((df_pol['L3Q4'])/(data.dfL3Best[3]),))[0]),) or (0,))[0]))/2)
    L3R2 = ((df_pol['L3Q4']>1 and ((df_pol['L3Q4']-1)/(data.dfL3Best[3]-1),) or (0,))[0])
    L3T2 = ((L3R2>=0.75 and (((df_pol['L3Q5']>1 and ((df_pol['L3Q5']/data.dfL3Best[4]),) or (0,))[0]),) or (0,))[0])
    #L4
    L4S1 = ((df_pol['L4Q6']>1 and ((((df_pol['L4Q6'])/(data.dfL4Best[5]-2)>1 and (1,) or ((df_pol['L4Q6'])/(data.dfL4Best[5]-2),))[0]),) or (0,))[0])
    L4A1 = ((df_pol['L4Q6']>1 and (((df_pol['L4Q6']-1)/(data.dfL4Best[5]-1)),) or (0,))[0])
    L4S2 = ((df_pol['L4Q1']>1 and (((df_pol['L4Q1']-1)/(data.dfL4Best[0]-1)),) or (0,))[0])
    L4M2 = ((((L4S2>=0.75 and (((df_pol['L4Q2']>1 and (((df_pol['L4Q2']/(data.dfL4Best[1]-2)<1 and ((df_pol['L4Q2']/(data.dfL4Best[1]-2)),) or (1,))[0]),) or (0,))[0]),) or (0,))[0])+(((df_pol['L4Q4'])/(data.dfL4Best[3]-1)>=1 and (1,) or ((df_pol['L4Q4'])/(data.dfL4Best[3]-1),))[0]))/2)
    L4A2 = (((L4M2>=0.75 and ((((df_pol['L4Q2']-1)/(data.dfL4Best[1]-2)>1 and (1,) or ((df_pol['L4Q2']-1)/(data.dfL4Best[1]-2),))[0]),) or (0,))[0]+(df_pol['L4Q4']/data.dfL4Best[3]))/2)
    L4R2 = ((L4A2>=0.75 and (((df_pol['L4Q2']>1 and ((df_pol['L4Q2']-1)/(data.dfL4Best[1]-1),) or (0,))[0]),) or (0,))[0])
    L4M3 = ((df_pol['L4Q3'])/(data.dfL4Best[2]))
    L4T3 = ((L4M3>=0.75 and (((df_pol['L4Q7']>1 and (((df_pol['L4Q7']-1)/(data.dfL4Best[6]-1)),) or (0,))[0]),) or (0,))[0])
    L4A4 = ((df_pol['L4Q5']>1 and (((df_pol['L4Q5']-1)/(data.dfL4Best[4]-1)),) or (0,))[0])
    print(df_pol)
    print()
    leadershipResults = ({'L1S1': [L1S1], 'L1M1': [L1M1], 'L1A1': [L1A1], 'L1S2': [L1S2], 'L1M2': [L1M2], 'L1A2': [L1A2], 'L1R2': [L1R2], 'L1T2': [L1T2], 'L1M3': [L1M3],
                          'L2M1': [L2M1], 'L2A1': [L2A1], 'L2R1': [L2R1], 'L2T1': [L2T1],
                          'L3S1': [L3S1], 'L3M1': [L3M1], 'L3T1': [L3T1], 'L3M2': [L3M2], 'L3A2': [L3A2], 'L3R2': [L3R2], 'L3T2': [L3T2],
                          'L4S1': [L4S1], 'L4A1': [L4A1], 'L4S2': [L4S2], 'L4M2': [L4M2], 'L4A2': [L4A2], 'L4R2': [L4R2], 'L4M3': [L4M3], 'L4T3': [L4T3], 'L4A4': [L4A4]})

    #Classifying by achieved policy by completeness
    starting = moderate = advanced = robust = vertebrate = 0
    for i in leadershipResults:
        if "S" in i and leadershipResults[i][0] == 1:
            starting = starting + 1
        elif "M" in i and leadershipResults[i][0] == 1:
            moderate = moderate + 1
        elif "A" in i and leadershipResults[i][0] == 1:
            advanced = advanced + 1 
        elif "R" in i and leadershipResults[i][0] == 1:
            robust = robust + 1
        elif "T" in i and leadershipResults[i][0] == 1:
            vertebrate = vertebrate + 1
    completeness = [starting, moderate, advanced, robust, vertebrate]
    print(leadershipResults)
    return leadershipResults, completeness

def Preparedness (df_pol, dfP1Best, dfP2Best):
    preparednessResults = preparednessCompleteness = 14
    return preparednessResults, preparednessCompleteness

def Infra (df_pol, dfI1Best, dfI2Best):
    infraResults = infraCompleteness = 16
    return infraResults, infraCompleteness

def Cooperation (df_pol, dfC1Best, dfC2Best):
    cooperationResults = cooperationCompleteness = 13
    return cooperationResults, cooperationCompleteness

def Urban (df_pol, dfU1Best, dfE1Best):
    #U1
    U1Q1Q2MEAN = (df_pol['U1Q1'] + df_pol['U1Q2'])/2
    U1S1 = (U1Q1Q2MEAN>1 and ((U1Q1Q2MEAN-1)/(data.dfU1Best[0]-1),) or (0,))[0]
    U1M1 = (U1S1>=0.75 and ((((df_pol['U1Q3'])/(data.dfU1Best[0]-2)>=1 and (((df_pol['U1Q3']-1)/(data.dfU1Best[0]-2)<1 and ((df_pol['U1Q3']-1)/(data.dfU1Best[0]-2),) or (1,))[0],) or (0,))[0])))
    U1A1 = (U1M1>=0.75 and (((df_pol['U1Q3']>1 and ((df_pol['U1Q3']-1)/(data.dfU1Best[2]-1),) or (0,))[0]),) or (0,))[0]
    U1R1 = (U1A1>=0.75 and (((df_pol['U1Q4']>1 and ((df_pol['U1Q4']-1)/(data.dfU1Best[3]-1),) or (0,))[0]),) or (0,))[0]
    U1M2 = (df_pol['U1Q5']>1 and ((df_pol['U1Q5']-1)/(data.dfU1Best[4]-1),) or (0,))[0]
    U1A2 = (U1M2>=0.75 and (((df_pol['U1Q6']>1 and (((df_pol['U1Q6']-1)/(data.dfU1Best[5]-2)>1 and (1,) or ((df_pol['U1Q6']-1)/(data.dfU1Best[5]-2),))[0],) or (0,))[0]),) or (0,))[0]
    # U1R2 = (U1A2>=0.75 and (((df_pol['U1Q6']>1 and ((df_pol['U1Q6']-1)/(data.dfU1Best[5]-1),) or (0,))[0]),) or (0,))[0]
    U1S3 = (U1S1>=0.75 and ((((df_pol['U1Q7'])/(data.dfU1Best[0]-2)>=1 and (((df_pol['U1Q7']-1)/(data.dfU1Best[0]-2)<1 and ((df_pol['U1Q7']-1)/(data.dfU1Best[0]-2),) or (1,))[0],) or (0,))[0])))
    U1M3 = (df_pol['U1Q7']>1 and ((df_pol['U1Q7']-1)/(data.dfU1Best[6]-1),) or (0,))[0]
    U1S4 = (df_pol['U1Q8']>1 and ((df_pol['U1Q8']-1)/(data.dfU1Best[7]-1),) or (0,))[0]
    U1M4 = (df_pol['U1Q9']>1 and ((df_pol['U1Q9']-1)/(data.dfU1Best[7]-1),) or (0,))[0]
    # U1A4 = (U1M4>=0.75 and (((df_pol['U1Q9']>1 and ((df_pol['U1Q9']-1)/(data.dfU1Best[8]-1),) or (0,))[0]),) or (0,))[0]
    U1M5 = (df_pol['U1Q10']>1 and ((df_pol['U1Q10']-1)/(data.dfU1Best[7]-1),) or (0,))[0]
    U1M6 = (df_pol['U1Q11']>1 and ((df_pol['U1Q11']-1)/(data.dfU1Best[7]-1),) or (0,))[0]

    #E1
    E1S1 = ((df_pol['E1Q1'])/(data.dfE1Best[0]-3)<1 and ((df_pol['E1Q1'])/(data.dfE1Best[0]-3),) or (1,))[0]
    E1A1 = ((df_pol['E1Q1'])/(data.dfE1Best[0]-1)<1 and ((df_pol['E1Q1'])/(data.dfE1Best[0]-1),) or (1,))[0]
    E1T1 = (df_pol['E1Q1'])/(data.dfE1Best[0])
    E1M2 = (df_pol['E1Q2']>1 and ((df_pol['E1Q2']-1)/(data.dfE1Best[1]-1),) or (0,))[0]
    E1A2 = (E1M2>=0.75 and (((df_pol['E1Q3']>1 and ((df_pol['E1Q3']-1)/(data.dfE1Best[2]-1),) or (0,))[0]),) or (0,))[0]
    E1R2 = (E1A2>=0.75 and ((((df_pol['E1Q4']>1 and ((df_pol['E1Q4']-1)/(data.dfE1Best[3]-1),) or (0,))[0]))))
    E1S3 = (df_pol['E1Q5']>1 and ((df_pol['E1Q5']-1)/(data.dfE1Best[5]-1),) or (0,))[0]
    E1M3 = (E1S3>=0.75 and ((((df_pol['E1Q6']>1 and ((df_pol['E1Q6']-1)/(data.dfE1Best[6]-1),) or (0,))[0]))))

    E1A3 = (E1M3>=0.75 and ((((df_pol['E1Q7']>1 and ((df_pol['E1Q7']-1)/(data.dfE1Best[8]-1),) or (0,))[0])+((df_pol['E1Q8']>1 and ((df_pol['E1Q8']-1)/(data.dfE1Best[9]-1),) or (0,))[0])+((df_pol['E1Q9']>1 and ((df_pol['E1Q9']-1)/(data.dfE1Best[10]-1),) or (0,))[0]))/3,) or (0,))[0]
    E1R3 = (E1A3>=0.75 and (((df_pol['E1Q11']>1 and ((df_pol['E1Q11']-1)/(data.dfE1Best[10]-1),) or (0,))[0]),) or (0,))[0]
    E1A4 = (df_pol['E1Q10']>1 and ((df_pol['E1Q10']-1)/(data.dfE1Best[10]-1),) or (0,))[0]

    urbanResults = ({'U1S1': [U1S1], 'U1M1': [U1M1], 'U1A1': [U1A1], 'U1R1': [U1R1], 'U1M2': [U1M2], 'U1A2': [U1A2], 'U1S3': [U1S3], 'U1M3': [U1M3], 'U1S4': [U1S4], 'U1M4': [U1M4], 'U1M5': [U1M5], 'U1M6': [U1M6],
                    'E1S1': [E1S1], 'E1A1': [E1A1], 'E1T1': [E1T1], 'E1M2': [E1M2], 'E1A2': [E1A2], 'E1R2': [E1R2], 'E1S3': [E1S3], 'E1M3': [E1M3], 'E1A3': [E1A3], 'E1R3': [E1R3], 'E1A4': [E1A4]})

    starting = moderate = advanced = robust = vertebrate = 0
    for i in urbanResults:
      if "S" in i and urbanResults[i][0] == 1:
          starting = starting + 1
      elif "M" in i and urbanResults[i][0] == 1:
          moderate = moderate + 1
      elif "A" in i and urbanResults[i][0] == 1:
          advanced = advanced + 1 
      elif "R" in i and urbanResults[i][0] == 1:
          robust = robust + 1
      elif "T" in i and urbanResults[i][0] == 1:
          vertebrate = vertebrate + 1
    urbanCompleteness = [starting, moderate, advanced, robust, vertebrate]

    return urbanResults, urbanCompleteness