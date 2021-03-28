#!/usr/bin/env python

import numpy as np
import pandas as pd

# Data Wrangling

# Group A
VFIAX = pd.read_csv("VFIAX.csv")
VFIAX.columns = ['Date','Open','High','Low','Close','VFIAX Close','Volume']
VBTLX = pd.read_csv("VBTLX.csv")
VBTLX.columns = ['Date','Open','High','Low','Close','VBTLX Close','Volume']
VGSLX = pd.read_csv("VGSLX.csv")
VGSLX.columns = ['Date','Open','High','Low','Close','VGSLX Close','Volume']

# Group B
VIMAX = pd.read_csv("VIMAX.csv")
VIMAX.columns = ['Date','Open','High','Low','Close','VIMAX Close','Volume']
VSMAX = pd.read_csv("VSMAX.csv")
VSMAX.columns = ['Date','Open','High','Low','Close','VSMAX Close','Volume']
VGHCX = pd.read_csv("VGHCX.csv")
VGHCX.columns = ['Date','Open','High','Low','Close','VGHCX Close','Volume']

# Group C
AMZN = pd.read_csv("AMZN.csv")
AMZN.columns = ['Date','Open','High','Low','Close','AMZN Close','Volume']
WMT = pd.read_csv("WMT.csv")
WMT.columns = ['Date','Open','High','Low','Close','WMT Close','Volume']
CVS = pd.read_csv("CVS.csv")
CVS.columns = ['Date','Open','High','Low','Close','CVS Close','Volume']

df = pd.concat([VFIAX['Date'], VFIAX['VFIAX Close'], VBTLX['VBTLX Close'], VGSLX['VGSLX Close'], VIMAX['VIMAX Close'], VSMAX['VSMAX Close'], VGHCX['VGHCX Close'], AMZN['AMZN Close'], WMT['WMT Close'], CVS['CVS Close'] ], axis=1)
print(df)


## generate mean daily return

for index, row in df.iterrows():
    if index == 0: continue # skip first row
    
