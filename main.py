import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as pex

def Plot2bars(df1, df2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    fig.suptitle('Correção do Estadiamento ', fontsize=20)
    ax1.set(ylim=(0, 5500))
    ax1.set_title('Antes')
    ax2.set(ylim=(0, 5500))
    ax2.set_title('Depois')
    sns.countplot(ax=ax1,x="Estadiamento", data=df1, order=['IV', 'IIIC', 'IIIB', 'IIIA', 'III', 'IIC', 'IIB', 'IIA', 'II', 'IC', 'IB', 'IA', 'I', '0', 'nan'])
    sns.countplot(ax=ax2,x="Estadiamento", data=df2, order=['IV', 'IIIC', 'IIIB', 'IIIA', 'III', 'IIC', 'IIB', 'IIA', 'II', 'IC', 'IB', 'IA', 'I', '0', 'nan'])
    for p in ax1.patches:
        ax1.annotate(f'\n{p.get_height()}', (p.get_x() + 0.35, p.get_height()+150), ha='center', va='top', color='black',
                    size=7)
    for p in ax2.patches:
        ax2.annotate(f'\n{p.get_height()}', (p.get_x() + 0.35, p.get_height()+150), ha='center', va='top', color='black',
                    size=7)
    plt.show()





def check_tnm(df, correct=False):
    for i in range(len(df)):
        if df['YTNMPatologico'][i] == 0:
            if df['pM'][i] == 'M1':
                new_estadiamento['IV'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IV'

            if df['pM'][i] == 'M0':
                tmn_starting_from_N(df, i, correct=correct)

            if df['pM'][i] =='Mx' or pd.isnull(df['pM'][i]): #se o patologico M for desconhecido, ver o clínico M
                if df['cM'][i] == 'M1':
                    new_estadiamento['IV'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IV'

                if df['cM'][i] in ['Mx', 'M0'] or pd.isnull(df['cM'][i]):
                    tmn_starting_from_N(df, i, correct=correct)

        if df['YTNMPatologico'][i] == 1:
            if df['cM'][i] == 'M1':
                new_estadiamento['IV'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IV'

            elif df['cM'][i] in ['Mx', 'M0'] or pd.isnull(df['cM'][i]):

                if df['cN'][i] in ['N3a', 'N3b', 'N3c']:
                    new_estadiamento['IIIC'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IIIC'

                elif df['cN'][i] in ['N2', 'N2a', 'N2b']:
                    if df['cT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                        new_estadiamento['IIIB'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'IIIB'
                    elif df['cT'][i] not in ['T4', 'T4a', 'T4b', 'T4c', 'T4d', 'Tx'] or not pd.isnull(df['cT'][i]):
                        new_estadiamento['IIIA'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'IIIA'
                    else:
                        new_estadiamento['III'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'III'

                elif df['cN'][i] in ['N1']:
                    if df['cT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                        new_estadiamento['IIIB'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'IIIB'
                    elif df['cT'][i] == 'T3':
                        new_estadiamento['IIIA'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'IIIA'
                    elif df['cT'][i] == 'T2':
                        new_estadiamento['IIB'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'IIB'
                    elif df['cT'][i] in ['T1mi', 'T1a', 'T1b', 'T1c', 'T0']:
                        new_estadiamento['IIA'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'IIA'
                    else:
                        new_estadiamento['II'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'II'

                elif df['cN'][i] in ['N0']:
                    if df['cT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                        new_estadiamento['IIIB'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'IIIB'
                    elif df['cT'][i] == 'T3':
                        new_estadiamento['IIB'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'IIB'
                    elif df['cT'][i] == 'T2':
                        new_estadiamento['IIA'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'IIA'
                    elif df['cT'][i] in ['T1mi', 'T1a', 'T1b', 'T1c']:
                        new_estadiamento['IA'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'IA'
                    elif df['cT'][i] in ['TisD', 'TisL', 'TisP']:
                        new_estadiamento['0'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = '0'
                    elif df['cT'][i] =='Tx' or pd.isnull(df['cT'][i]): #is nullllllllllll
                        new_estadiamento['nan'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'nan'

                elif df['cN'][i] =='Nx' or pd.isnull(df['cN'][i]):
                    if df['cT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                        new_estadiamento['III'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'III'
                    else:
                        new_estadiamento['nan'].append(i)
                        if correct:
                            df.loc[i, 'Estadiamento'] = 'nan'

    if not correct:
        print('IV', len(new_estadiamento['IV']))
        print('IIIC', len(new_estadiamento['IIIC']))
        print('IIIB', len(new_estadiamento['IIIB']))
        print('IIIA', len(new_estadiamento['IIIA']))
        print('III', len(new_estadiamento['III']))
        print('IIA', len(new_estadiamento['IIA']))
        print('IIB', len(new_estadiamento['IIB']))
        print('II', len(new_estadiamento['II']))
        print('IA', len(new_estadiamento['IA']))
        print('IB', len(new_estadiamento['IB']))
        print('I', len(new_estadiamento['I']))
        print('0', len(new_estadiamento['0']))
        print('N/A', len(new_estadiamento['nan']))

        fixed_indices = list(new_estadiamento.values())
        flat_list = [item for sublist in fixed_indices for item in sublist]

        print('Total', len(flat_list))
        df_check_for_missed = df.drop(df.index[flat_list]).reset_index()
        print('missed cases', len(df_check_for_missed))

def tmn_starting_from_N(df, i, correct=False):
    if df['pN'][i] in ['N3a', 'N3b', 'N3c']:
        new_estadiamento['IIIC'].append(i)
        if correct:
            df.loc[i, 'Estadiamento'] = 'IIIC'

    if df['pN'][i] in ['N2', 'N2a', 'N2b']:
        if df['pT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
            new_estadiamento['IIIB'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = 'IIIB'
        elif df['pT'][i] not in ['T4', 'T4a', 'T4b', 'T4c', 'T4d', 'Tx'] or not pd.isnull(df['pT'][i]):
            new_estadiamento['IIIA'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = 'IIIA'
        elif df['pT'][i] == 'Tx' or pd.isnull(df['pT'][i]):  # se o patologico for desconhecido ir ver o clinico
            if df['cT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                new_estadiamento['IIIB'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIIB'
            elif df['cT'][i] not in ['T4', 'T4a', 'T4b', 'T4c', 'T4d', 'Tx'] or not pd.isnull(df['cT'][i]):
                new_estadiamento['IIIA'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIIA'
            else:
                new_estadiamento['III'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'III'

    if df['pN'][i] in ['N1', 'N1a', 'N1b', 'N1c']:
        if df['pT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
            new_estadiamento['IIIB'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = 'IIIB'
        elif df['pT'][i] == 'T3':
            new_estadiamento['IIIA'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = 'IIIA'
        elif df['pT'][i] == 'T2':
            new_estadiamento['IIB'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = 'IIB'
        elif df['pT'][i] in ['T1mi', 'T1a', 'T1b', 'T1c', 'T0']:
            new_estadiamento['IIA'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = 'IIA'
        elif df['pT'][i] =='Tx' or pd.isnull(df['pT'][i]):  # se o patologico for desconhecido ir ver o clinico
            if df['cT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                new_estadiamento['IIIB'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIIB'
            elif df['cT'][i] == 'T3':
                new_estadiamento['IIIA'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIIA'
            elif df['cT'][i] == 'T2':
                new_estadiamento['IIB'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIB'
            elif df['cT'][i] in ['T1mi', 'T1a', 'T1b', 'T1c', 'T0']:
                new_estadiamento['IIA'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIA'
            else:
                new_estadiamento['II'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'II'

    if df['pN'][i] == 'N1m':
        new_estadiamento['IB'].append(i)
        if correct:
            df.loc[i, 'Estadiamento'] = 'IB'

    if df['pN'][i] == 'N0':
        if df['pT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
            new_estadiamento['IIIB'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = 'IIIB'
        elif df['pT'][i] == 'T3':
            new_estadiamento['IIB'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = 'IIB'
        elif df['pT'][i] == 'T2':
            new_estadiamento['IIA'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = 'IIA'
        elif df['pT'][i] in ['T1mi', 'T1a', 'T1b', 'T1c']:
            new_estadiamento['IA'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = 'IA'
        elif df['pT'][i] in ['TisD', 'TisL', 'TisP','T0']:
            new_estadiamento['0'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = '0'
        elif df['pT'][i] =='Tx' or pd.isnull(df['pT'][i]):
            if df['cT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                new_estadiamento['IIIB'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIIB'
            elif df['cT'][i] == 'T3':
                new_estadiamento['IIB'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIB'
            elif df['cT'][i] == 'T2':
                new_estadiamento['IIA'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIA'
            elif df['cT'][i] in ['T1mi', 'T1a', 'T1b', 'T1c']:
                new_estadiamento['IA'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IA'
            elif df['cT'][i] in ['TisD', 'TisL', 'TisP']:
                new_estadiamento['0'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = '0'
            elif df['cT'][i] == 'Tx' or pd.isnull(df['cT'][i]): ######NULLLLLLSSSSSSSS
                new_estadiamento['nan'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'nan'

    if df['pN'][i] == 'Nx' or pd.isnull(df['pN'][i]):  # se o patologico N for desconhecido ir ver o clinico N
        if df['cN'][i] in ['N3a', 'N3b', 'N3c']:
            new_estadiamento['IIIC'].append(i)
            if correct:
                df.loc[i, 'Estadiamento'] = 'IIIC'
        if df['cN'][i] in ['N2', 'N2a', 'N2b']:
            if df['pT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                new_estadiamento['IIIB'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIIB'
            elif df['pT'][i] not in ['T4', 'T4a', 'T4b', 'T4c', 'T4d', 'Tx'] or not pd.isnull(df['pT'][i]):
                new_estadiamento['IIIA'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIIA'
            elif df['pT'][i] =='Tx' or pd.isnull(df['pT'][i]):
                if df['cT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                    new_estadiamento['IIIB'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IIIB'
                elif df['cT'][i] not in ['T4', 'T4a', 'T4b', 'T4c', 'T4d', 'Tx'] or not pd.isnull(df['cT'][i]):
                    new_estadiamento['IIIA'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IIIA'
                else:
                    new_estadiamento['III'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'III'

        if df['cN'][i] in ['N1']:
            if df['pT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                new_estadiamento['IIIB'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIIB'
            elif df['pT'][i] == 'T3':
                new_estadiamento['IIIA'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIIA'
            elif df['pT'][i] == 'T2':
                new_estadiamento['IIB'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIB'
            elif df['pT'][i] in ['T1mi', 'T1a', 'T1b', 'T1c']:
                new_estadiamento['IIA'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIA'
            elif df['pT'][i] == 'Tx' or pd.isnull(df['pT'][i]):  # se o patologico for desconhecido ir ver o clinico
                if df['cT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                    new_estadiamento['IIIB'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IIIB'
                elif df['cT'][i] == 'T3':
                    new_estadiamento['IIIA'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IIIA'
                elif df['cT'][i] == 'T2':
                    new_estadiamento['IIB'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IIB'
                elif df['cT'][i] in ['T1mi', 'T1a', 'T1b', 'T1c', 'T0']:
                    new_estadiamento['IIA'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IIA'
                else:
                    new_estadiamento['II'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'II'

        if df['cN'][i] in ['N0']:
            if df['pT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                new_estadiamento['IIIB'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIIB'
            elif df['pT'][i] == 'T3':
                new_estadiamento['IIIA'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIIA'
            elif df['pT'][i] == 'T2':
                new_estadiamento['IIB'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIB'
            elif df['pT'][i] in ['T1mi', 'T1a', 'T1b', 'T1c']:
                new_estadiamento['IIA'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'IIA'
            elif df['pT'][i] in ['TisD', 'TisL', 'TisP']:
                new_estadiamento['0'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = '0'
            elif df['pT'][i] == 'Tx' or pd.isnull(df['pT'][i]):
                if df['cT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                    new_estadiamento['IIIB'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IIIB'
                elif df['cT'][i] == 'T3':
                    new_estadiamento['IIB'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IIB'
                elif df['cT'][i] == 'T2':
                    new_estadiamento['IIA'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IIA'
                elif df['cT'][i] in ['T1mi', 'T1a', 'T1b', 'T1c']:
                    new_estadiamento['IA'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'IA'
                elif df['cT'][i] in ['TisD', 'TisL', 'TisP']:
                    new_estadiamento['0'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = '0'
                elif df['cT'][i] =='Tx' or pd.isnull(df['cT'][i]): #NUUUULLLLLLSSS
                    new_estadiamento['nan'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'nan'

        if df['cN'][i] =='Nx' or pd.isnull(df['cN'][i]):
            # se o clinico N tambem for desconhecido, ver só o T, primeiro o patologico, se esse tmb for desconhecido, ver o clinico
            if df['pT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                new_estadiamento['III'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'III'
            if df['pT'][i] =='Tx' or pd.isnull(df['pT'][i]):
                if df['cT'][i] in ['T4', 'T4a', 'T4b', 'T4c', 'T4d']:
                    new_estadiamento['III'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'III'
                else:
                    new_estadiamento['nan'].append(i)
                    if correct:
                        df.loc[i, 'Estadiamento'] = 'nan'  ###NUUULLLLLS
            else:
                new_estadiamento['nan'].append(i)
                if correct:
                    df.loc[i, 'Estadiamento'] = 'nan'



df = pd.read_csv(r'2021 0218_DraMargaridaBrito_Mama_Nacional_ROR-Sul_2010-2014.csv')


columns_to_drop = ['Top', 'Morf','cT_Desc', 'cN_Desc', 'cM_Desc', 'pT_Desc', 'pN_Desc', 'pM_Desc', 'MotivoNãoTratamento', 'RORSul', 'TipoTrat16', 'DataTrat16', 'InstituicaoTrat16', 'Estadio']
clean_up_nums = {
    'Estadiamento': {
        '1': 'I',
        '?': 'Desconhecido',
        'DESCONHECIDO': 'Desconhecido',
        '3': 'III',
        ' Não mencionado no processo': 'Desconhecido',
        'IA1':'IA',
        'IA (BIRADS 6)':'IA',
        'III C': 'IIIC',
        'III B': 'IIIB',
        'III A': 'IIIA',
        'IIB?': 'IIB',
        'CI':'IC',
        'G2': 'II',
        'G II': 'II',
        'IIIB/IIIA': 'III',
        'II B': 'IIB',
        'II A':'IIA',



    },
    'Estado': {
        1:0,
        2:1
    },
    'RE': {
        'Positivo': 'RE_Positivo', #depois faço one hot encoding e é para ficar com este nome na coluna por oposição a só "positivo" porque depois não saberia o que era positivo
        'Negativo': 'RE_Negativo',
        'Desconhecido': 'nan',
        'Não Avaliado': 'nan'
        # 'Desconhecido': 'RE_Desconhecido',
        # 'Não Avaliado':'RE_Desconhecido'
    },
    'RP': {
        'Positivo': 'RP_Positivo',
        'Negativo': 'RP_Negativo',
        'Desconhecido': 'nan',
        'Não Avaliado': 'nan'
        # 'Desconhecido': 'RP_Desconhecido',
        # 'Não Avaliado':'RP_Desconhecido'
    },
    'Her2': {
        'Positivo': 'Her2_Positivo',
        'Negativo': 'Her2_Negativo',
        'Desconhecido': 'nan',
        'Não Avaliado': 'nan'
        # 'Desconhecido': 'Her2_Desconhecido',
        # 'Não Avaliado':'Her2_Desconhecido'
    },
    'cT': {
        'T1m':'T1mi'
    },
    'pT': {
        'T1m':'T1mi',
        'T2c':'T2'
    },
    'FreguesiasRurais':{
        'Ver':'nan',
        'Não Encontra':'nan',
        'Sem Freguesia Registada':'nan'
    }
}

df = df[(df[['RORSul']] != 0).all(axis=1)]
df = df.drop(columns_to_drop, axis=1)
df = df.replace(clean_up_nums).reset_index(drop=True)
df['Estadiamento'] = df['Estadiamento'].replace(np.nan, 'nan', regex=True)




new_estadiamento = {
    'IV': [],
    'IIIC': [],
    'IIIB':[],
    'IIIA':[],
    'III':[],
    'IIA':[],
    'IIB':[],
    'II':[],
    'IA':[],
    'IB':[],
    'I':[],
    '0':[],
    'nan':[]
}



#check_tnm(df, correct=False)


df2=df.copy()
check_tnm(df2, correct=True)

'Drop more columns that we don\'t need after staging correction'
# columns_to_drop_2 = ['cT', 'cN', 'cM','pT', 'pN', 'pM','YTNMPatologico']
# df2 = df2.drop(columns_to_drop_2, axis=1)
#
# Plot2bars(df, df2)

df2[['RP', 'RE', 'Her2']] = df2[['RP', 'RE', 'Her2']].replace(np.nan, 'nan', regex=True)
df2[['cT', 'cN', 'cM','pT', 'pN', 'pM','YTNMPatologico']] = df2[['cT', 'cN', 'cM','pT', 'pN', 'pM','YTNMPatologico']].replace(np.nan, 'nan', regex=True)
df2['PS'] = df2['PS'].replace(np.nan, '5 Desconhecido (Karnofsky desconhecido)', regex=True)

nans = df.loc[df2['Estadiamento'] == 'nan']
nans2 = nans.loc[nans['Estadiamento'].notna()]

'susbtituir o nome dos tratamentos por #'
Tratamento_sankey = {}
for a in range(2,16):
    Tratamento_sankey.update({f'TipoTrat{a}': {
        'Tratamento Sistémico': f'{a}º Tratamento Sistémico',
        'Cirurgia': f'{a}º Cirurgia',
        'Radioterapia': f'{a}º Radioterapia',
        'Outro': f'{a}º Outro',
    },})

df2 = df2.replace(Tratamento_sankey).reset_index(drop=True)


for a in range(1, 16):
    df2[f'TipoTrat{a}']=df2[f'TipoTrat{a}'].replace(np.nan, 'Não Fez', regex=True)

'construir uma dict para sankey diagram'
sankey_dict ={'Source':[],
              'Destination': [],
              'Counts': []}



for i in range(1,15):
    group = df2.groupby([f'TipoTrat{i}', f'TipoTrat{i + 1}']).groups
    pairs = list(group.keys())

    for pair in pairs:
        sankey_dict['Source'].append(pair[0])
        sankey_dict['Destination'].append(pair[1])
        sankey_dict['Counts'].append(len(group[pair].tolist()))


sankey_df = pd.DataFrame(sankey_dict)
sankey_df = sankey_df[(sankey_df[['Source']] != 'Não Fez').all(axis=1)]

all_nodes = sankey_df.Source.values.tolist() + sankey_df.Destination.values.tolist()
source_indices = [all_nodes.index(source) for source in sankey_df.Source]
target_indices = [all_nodes.index(dest) for dest in sankey_df.Destination]

colors = pex.colors.qualitative.Alphabet
node_colors_mappings = dict([(node,np.random.choice(colors, replace=False)) for node in all_nodes])
color_node = [node_colors_mappings[node] for node in all_nodes]
color_link = [node_colors_mappings[node] for node in sankey_df.Source]

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = all_nodes,
      #color =color_node


    ),
    link = dict(
      source = source_indices,
      target = target_indices,
      value = sankey_df.Counts,
      #color = color_link
  ))])

fig.update_layout(title_text="Treatment Sankey Diagram", font_size=10)
fig.show()



