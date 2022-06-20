import pandas as pd
import numpy as np
import sys

  
def mergerfeature(ref,features):
    
    ref_df = pd.read_csv(ref)
    features_df = pd.read_csv(features)

    features_df = features_df.drop_duplicates()

    listnameref_df = ref_df['TargetFile']
    listvalor = []
    listindex =[]
    listaux =[]

    for i in listnameref_df:
        if "/" in i:
            listaux.append(i)
    listaux = np.array(listaux)
    listaux = np.unique(listaux)
            
    for i in listaux:
        for index, valor in enumerate(features_df["TargetFile"]):
            if i in valor:
                listvalor.append(i)
                listindex.append(index)
            
    
    features_df['TargetFile'] = features_df['TargetFile'].str.split('/').str[-1]

    for index,valor in enumerate(listindex):
        features_df['TargetFile'][valor] = listvalor[index]
   
    df = pd.merge(ref_df,features_df ,on=['TargetFile'])

    df = df.loc[((df['FeatFrom']>= df['LineFrom']) & (df['FeatFrom']<= df['LineTo']) & (df['FeatTo'] <= df['LineTo']))]
    df['LineTo'] = df['LineTo'].astype(int)
    del df["Unnamed: 0"]
    del df["Commit Nr"]
    df = df.reset_index(drop=True)

    return df

def mergerteste(ref,features):
    
    ref_df = pd.read_csv(ref)
    features_df = pd.read_csv(features)

    features_df = features_df.drop_duplicates()

    listnameref_df = ref_df['TargetFile']
    listvalor = []
    listindex =[]
    listaux =[]

    for i in listnameref_df:
        if "/" in i:
            listaux.append(i)
    listaux = np.array(listaux)
    listaux = np.unique(listaux)
            
    for i in listaux:
        for index, valor in enumerate(features_df["TargetFile"]):
            if i in valor:
                listvalor.append(i)
                listindex.append(index)
            
    
    features_df['TargetFile'] = features_df['TargetFile'].str.split('/').str[-1]

    for index,valor in enumerate(listindex):
        features_df['TargetFile'][valor] = listvalor[index]

    df = pd.merge(ref_df,features_df ,on=['TargetFile'])

    df = df.loc[((df['LineFrom']>= df['FeatFrom']) & (df['LineFrom']<= df['FeatTo']) & (df['LineTo'] <= df['FeatTo']))]
    df['LineTo'] = df['LineTo'].astype(int)
    del df["Unnamed: 0"]
    del df["Commit Nr"]
    df = df.reset_index(drop=True)

    return df


def main():

    df = mergerfeature(sys.argv[1],sys.argv[2])

    df.to_csv('result/test2feature.csv')

    df = mergerteste(sys.argv[1],sys.argv[2])

    df.to_csv('result/feature2test.csv')

main()


