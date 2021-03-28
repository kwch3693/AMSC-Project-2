#!/usr/bin/env python

import numpy as np
import pandas as pd

# Data Wrangling

# Group A
VFIAX = pd.read_csv("Data/VFIAX.csv")
VFIAX.columns = ['Date','Open','High','Low','Close','VFIAX Close','Volume']
VBTLX = pd.read_csv("Data/VBTLX.csv")
VBTLX.columns = ['Date','Open','High','Low','Close','VBTLX Close','Volume']
VGSLX = pd.read_csv("Data/VGSLX.csv")
VGSLX.columns = ['Date','Open','High','Low','Close','VGSLX Close','Volume']

# Group B
VIMAX = pd.read_csv("Data/VIMAX.csv")
VIMAX.columns = ['Date','Open','High','Low','Close','VIMAX Close','Volume']
VSMAX = pd.read_csv("Data/VSMAX.csv")
VSMAX.columns = ['Date','Open','High','Low','Close','VSMAX Close','Volume']
VGHCX = pd.read_csv("Data/VGHCX.csv")
VGHCX.columns = ['Date','Open','High','Low','Close','VGHCX Close','Volume']

# Group C
AMZN = pd.read_csv("Data/AMZN.csv")
AMZN.columns = ['Date','Open','High','Low','Close','AMZN Close','Volume']
WMT = pd.read_csv("Data/WMT.csv")
WMT.columns = ['Date','Open','High','Low','Close','WMT Close','Volume']
CVS = pd.read_csv("Data/CVS.csv")
CVS.columns = ['Date','Open','High','Low','Close','CVS Close','Volume']

close = pd.concat([VFIAX['Date'], VFIAX['VFIAX Close'], VBTLX['VBTLX Close'], VGSLX['VGSLX Close'], VIMAX['VIMAX Close'], VSMAX['VSMAX Close'], VGHCX['VGHCX Close'], AMZN['AMZN Close'], WMT['WMT Close'], CVS['CVS Close'] ], axis=1)
#print(close)


## generate mean daily return
dailyReturn = pd.DataFrame(columns = ['Date', 'VFIAX Daily Return','VBTLX Daily Return','VGSLX Daily Return', 'VIMAX Daily Return', 'VSMAX Daily Return', 'VGHCX Daily Return','AMZN Daily Return', 'WMT Daily Return','CVS Daily Return'])
for index, row in close.iterrows():
    if index == 0: continue
    #print((close['VFIAX Close'][index] - close['VFIAX Close'][index-1])/ (close['VFIAX Close'][index-1]))
    dailyReturn = dailyReturn.append({'Date': close['Date'][index],
                'VFIAX Daily Return': ((close['VFIAX Close'][index] - close['VFIAX Close'][index-1])/(close['VFIAX Close'][index-1])),
                'VBTLX Daily Return': ((close['VBTLX Close'][index] - close['VBTLX Close'][index-1])/(close['VBTLX Close'][index-1])),
                'VGSLX Daily Return': ((close['VGSLX Close'][index] - close['VGSLX Close'][index-1])/(close['VGSLX Close'][index-1])),
                'VIMAX Daily Return': ((close['VIMAX Close'][index] - close['VIMAX Close'][index-1])/(close['VIMAX Close'][index-1])),
                'VSMAX Daily Return': ((close['VSMAX Close'][index] - close['VSMAX Close'][index-1])/(close['VSMAX Close'][index-1])),
                'VGHCX Daily Return': ((close['VGHCX Close'][index] - close['VGHCX Close'][index-1])/(close['VGHCX Close'][index-1])),
                'AMZN Daily Return': ((close['AMZN Close'][index] - close['AMZN Close'][index-1])/(close['AMZN Close'][index-1])),
                'WMT Daily Return': ((close['WMT Close'][index] - close['WMT Close'][index-1])/(close['WMT Close'][index-1])),
                'CVS Daily Return': ((close['CVS Close'][index] - close['CVS Close'][index-1])/(close['CVS Close'][index-1]))},ignore_index=True)

equalWeights = [(1/9), (1/9), (1/9), (1/9), (1/9), (1/9), (1/9), (1/9), (1/9)]

ExpectedReturn = pd.DataFrame(columns = ['Date', 'ER'])

for index, row in dailyReturn.iterrows():
    if index == 0: continue
    ExpectedReturn = ExpectedReturn.append({'Date':dailyReturn['Date'][index],'ER':np.sum([dailyReturn['VFIAX Daily Return'][index]*equalWeights[0],
                dailyReturn['VBTLX Daily Return'][index]*equalWeights[1],
                dailyReturn['VGSLX Daily Return'][index]*equalWeights[2],
                dailyReturn['VIMAX Daily Return'][index]*equalWeights[3],
                dailyReturn['VSMAX Daily Return'][index]*equalWeights[4],
                dailyReturn['VGHCX Daily Return'][index]*equalWeights[5],
                dailyReturn['AMZN Daily Return'][index]*equalWeights[6],
                dailyReturn['WMT Daily Return'][index]*equalWeights[7],
                dailyReturn['CVS Daily Return'][index]*equalWeights[8]])},ignore_index=True)
# print(ExpectedReturn)

