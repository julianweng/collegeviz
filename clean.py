import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def toFloat(df,cols):
    for col in cols:
        df[col] = pd.to_numeric(df[col],errors='coerce')

df = pd.read_csv("collegedata170m.csv")
df["% Tech"] = (df['PCIP11'] + df['PCIP14'] + df['PCIP15'] + df['PCIP27'] + df['PCIP40'] + df['PCIP41'])
df["% Business"] = df['PCIP52']
df["% Biology"] = df['PCIP26']
df["% STEM"] = df["% Tech"] + df["% Business"] + df["% Biology"]

df.dropna(axis=1, how='all', thresh=500, inplace=True) # drop columns (axis=1) if less than 500 entries have values (non-null/NaN)
df.dropna(axis=0, how='all', thresh=1500, inplace=True) # drop rows (axis=0) if less than 1500 attributes have values (non-null/NaN)

regionMap = {0:"U.S. Service Schools",1:"New Englend",2:"Mid East",3:"Great Lakes",4:"Plains",
    5:"Southeast",6:"Southwest",7:"Rocky Mountains",8:"Far West",9:"Outlying"}
df['REGION'] = df['REGION'].map(regionMap)

toFloat(df,['FAMINC','MD_FAMINC','MD_EARN_WNE_P10','PCT25_EARN_WNE_P6','PCT25_EARN_WNE_P10','RPY_3YR_RT_SUPP',
    'PELL_RPY_3YR_RT_SUPP', 'PCT_BLACK','PCT_WHITE','PCT_HISPANIC','PCT_ASIAN','MN_EARN_WNE_P10',
    'PCT90_EARN_WNE_P6','PCT90_EARN_WNE_P10'])

selected = ['OPEID6','INSTNM','UGDS','CITY','STABBR','ZIP','PREDDEG','REGION','ADM_RATE','MN_EARN_WNE_P10','MD_EARN_WNE_P10',
            'PCT90_EARN_WNE_P6','PCT90_EARN_WNE_P10','PCT25_EARN_WNE_P6','PCT25_EARN_WNE_P10',
            'NPT45_PRIV','NPT45_PUB','NPT43_PRIV','NPT43_PUB','NPT41_PRIV','NPT41_PUB','NPT4_PUB','NPT4_PRIV',
            'FAMINC','MD_FAMINC','RPY_3YR_RT_SUPP','PELL_RPY_3YR_RT_SUPP','CDR3',
            'PCIP11','PCIP15','PCIP27','PCIP40','PCT_WHITE','PCT_BLACK','PCT_HISPANIC','PCT_ASIAN',
            'UGDS_WHITE','UGDS_ASIAN','UGDS_BLACK','UGDS_HISP','C150_4_BLACK','C150_4_HISP','C150_4_ASIAN','C150_4_WHITE',
            '% Tech','% Business','% Biology','% STEM']

display = {'INSTNM':'College','UGDS':'Undergraduate Enrollment','PREDDEG':'Predominant degree','ADM_RATE':'Admission rate',
           'MN_EARN_WNE_P10':'Mean Earnings 10Yr','MD_EARN_WNE_P10':'Median Earnings 10Yr',
            'PCT90_EARN_WNE_P6':'90% earnings 6Yr','PCT90_EARN_WNE_P10':'90% earnings 10Yr','PCT25_EARN_WNE_P6':'25% earnings 6Yr',
            'PCT25_EARN_WNE_P10':'25% earnings 10Yr','NPT45_PRIV':'Net Price 110k family (Private)','NPT45_PUB':'Net Price 110k family (Public)',
            'NPT43_PRIV':'Net Price 48-75k family (Private)','NPT43_PUB':'Net Price 48-75k family (Public)',
            'NPT41_PRIV':'Net Price 0-30k family (Private)','NPT41_PUB':'Net Price 0-30k family (Public)',
            'NPT4_PUB':'Net Price All Income (Public)','NPT4_PRIV':'Net Price All Income (Private)',
            'FAMINC':'Avg Family Income','MD_FAMINC':'Median Family Income','RPY_3YR_RT_SUPP':'3Yr Repayment Rate',
            'PELL_RPY_3YR_RT_SUPP':'3Yr Repayment Rate (Pell Students)','CDR3':'3Yr Default Rate',
            'PCIP11':'% CS/IT','PCIP14':'% Engineering','PCIP15':'% Engineering Related','PCIP27':'% Math/Stats','PCIP40':'% Physical Science',
            'PCT_WHITE':'% students neighbors Whites','PCT_BLACK':'% students neighbors Blacks','PCT_HISPANIC':'% students neighbors Hispanic',
            'PCT_ASIAN':'% students neighbors Asians','UGDS_WHITE':'% undergrades Whites','UGDS_ASIAN':'% undergrades Asians',
            'UGDS_BLACK':'% undergrades Blacks','UGDS_HISP':'% undergrades Hispanic','C150_4_BLACK':'6Yr Completion % Blacks',
            'C150_4_HISP':'6Yr Completion % Hispanics','C150_4_ASIAN':'6Yr Completion % Asians','C150_4_WHITE':'6Yr Completion % Whites'}

out = df[selected].copy()
out.set_index('OPEID6', inplace=True)
out.rename(columns=display, inplace=True)

out['Net Price (All Income)'] = out['Net Price All Income (Public)'].fillna(0) + out['Net Price All Income (Private)'].fillna(0)
out['Net Price 0-30k'] = out['Net Price 0-30k family (Public)'].fillna(0) + out['Net Price 0-30k family (Private)'].fillna(0)
out['Net Price 110K+'] = out['Net Price 110k family (Public)'].fillna(0) + out['Net Price 110k family (Private)'].fillna(0)

mrc_display = {'tier_name':'Tier Name', 'female':'% Female','k_married':'% Married','mr_kq5_pq1':'Mobility rate (80%->20%)',
               'mr_ktop1_pq1':'Upper-tail mobility rate (80%->1%)','par_mean':'Mean parental income','par_median':'Median parent household income',
               'par_rank':'Mean parental income rank','k_rank':'Mean kid earnings rank','k_mean':'Mean kid earnings',
               'k_median':'Median child individual earnings'}

mrc = pd.read_csv("mrc_table2.csv")
mrc.rename(columns={'super_opeid':'OPEID6'}, inplace=True)
mrc.set_index('OPEID6', inplace=True)
mrc.rename(columns=mrc_display, inplace=True)

out.join(mrc, how='inner').to_csv("reportcard.csv")