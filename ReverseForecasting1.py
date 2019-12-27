import Forecast_GUI

from fpdf import FPDF

from statsmodels.tsa.stattools import adfuller
from numpy import arange, sin, pi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import csv
from dateutil.relativedelta import relativedelta

from matplotlib.backends.backend_pdf import PdfPages



import statsmodels.api as sm  
from statsmodels.tsa.stattools import acf  
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from matplotlib.pylab import rcParams
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import matplotlib.figure as mplfig
import scipy.spatial.distance as dist
import matplotlib.backends.backend_wxagg as mwx



pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.write(8,'Reverse Forecasting Results\n')
pdf.set_font('Arial','', 12)

def initialize_data():
    df = Forecast_GUI.read_dealer_file() 


    line_cnt = sum(1 for line in open('DealerFY_2015-16.csv'))

    global df_Debit_sum
    df_Debit_sum= df.sum()

    global df_classA,df_classB,df_classC
    df_classA = pd.DataFrame(columns= ['Name', 'Debit', 'Credit', 'Ratio'])
    df_classB = pd.DataFrame(columns= ['Name', 'Debit', 'Credit', 'Ratio'])
    df_classC = pd.DataFrame(columns= ['Name', 'Debit', 'Credit', 'Ratio'])

    

    i=0
    j=0
    #for j in range (0,line_cnt):
    while(j<line_cnt-1):
        if(df["Debit"].loc[j]> 1500000):
            df_classA.loc[i] = df.iloc[j]
            i=i+1
        j=j+1


    global count_classA,count_classB,count_classC
    count_classA= df_classA.count()
    Forecast_GUI.text_widget1.insert('insert',"Information of dealers with Debit > 15 Lakhs\n")
    Forecast_GUI.text_widget1.insert('insert',df_classA)
    Forecast_GUI.text_widget1.insert('insert',"\n\n\n")
    
    """
    pdf.write(8,'Information of dealers with Debit > 15 Lakhs\n')

    df_classA_str = ''
    df_classA_str = df_classA.to_string()
    #df_classA = df_classA.astype(str)
    pdf.multi_cell(140,8,df_classA_str,1,'R')
    """


    i=0
    j=0
    #for j in range (0,line_cnt):
    while(j<line_cnt-1):
        if(df["Debit"].loc[j]> 500000 and df["Debit"].loc[j]< 1500000):
            df_classB.loc[i] = df.iloc[j]
            i=i+1
        j=j+1

    count_classB= df_classB.count()
    Forecast_GUI.text_widget1.insert('insert',"Information of dealers with Debit > 5 Lakhs\n")
    Forecast_GUI.text_widget1.insert('insert',df_classB)
    Forecast_GUI.text_widget1.insert('insert',"\n\n\n")

    """
    pdf.write(8,'\nInformation of dealers with Debit > 5 Lakhs\n')

    df_classB_str = ''
    df_classB_str = df_classB.to_string()
    #df_classA = df_classA.astype(str)
    pdf.multi_cell(140,8,df_classB_str,1,'R')
    #pdf.output('Reverse_Forecasting.pdf','F')
    """

    i=0
    j=0
    while(j<line_cnt-1):
        if(df["Debit"].loc[j]< 500000 and df["Ratio"].loc[j]> 0):
            df_classC.loc[i] = df.iloc[j]
            i=i+1
        j=j+1

    count_classC= df_classC.count()
    Forecast_GUI.text_widget1.insert('insert',"Information of dealers with Debit < 5 Lakhs\n")
    Forecast_GUI.text_widget1.insert('insert',df_classC)
    Forecast_GUI.text_widget1.insert('insert',"\n\n\n")


    """
    pdf.write(8,'\nInformation of dealers with Debit < 5 Lakhs\n')

    df_classC_str = ''
    df_classC_str = df_classC.to_string()
    #df_classA = df_classA.astype(str)
    pdf.multi_cell(140,8,df_classC_str,1,'R')
    #pdf.output('Reverse_Forecasting.pdf','F')
    """

def calc_expec_sales():

    #Forecast_GUI.text_widget1.insert('insert',"Enter the expected sales value\n")
    expec_sales= int(Forecast_GUI.read_rev_entry())


    Forecast_GUI.text_widget1.insert('insert',"Forecasted Sales are: %d\n"%Forecast_GUI.forecasted_sales)
    pdf.write(8,'Forecasted Sales are: ' + str(Forecast_GUI.forecasted_sales) + '\n')

    Forecast_GUI.text_widget1.insert('insert',"Required sales are: " + str(expec_sales) + "\n")
    pdf.write(8,'Required Sales are: ' + str(expec_sales) + '\n')
    extra_sales= expec_sales - Forecast_GUI.forecasted_sales

    Forecast_GUI.text_widget1.insert('insert',"Extra sales required to achieve the target: " + str(extra_sales) + "\n")


    """
    act_prof=500000
    sales=5000000
    pred_sales = expec_prof*sales/act_prof
    """
    df_classA_sales=0
    df_classB_sales=0
    df_classC_sales=0
    #line_cnt_classA = df_classA.count(axis=0)
    #Forecast_GUI.text_widget1.insert('insert',line_cnt_classA)

    df_classA_sales = df_classA.sum()
    df_classB_sales = df_classB.sum()
    df_classC_sales = df_classC.sum()
    Forecast_GUI.text_widget1.insert('insert',"Total revenue from class A dealers: " + str(df_classA_sales['Debit']) + "\n")
    Forecast_GUI.text_widget1.insert('insert',"Total revenue from class B dealers: %d\n"%df_classB_sales['Debit']) 
    Forecast_GUI.text_widget1.insert('insert',"Total revenue from class C dealers: %d\n"%df_classC_sales['Debit'])  
    pdf.write(8,'Total revenue from class A dealers: ' + str(df_classA_sales['Debit']) + '\n')
    pdf.write(8,'Total revenue from class B dealers: ' + str(df_classB_sales['Debit']) + '\n')
    pdf.write(8,'Total revenue from class C dealers: ' + str(df_classC_sales['Debit']) + '\n')


    global df_classA_expec_sales, df_classB_expec_sales, df_classC_expec_sales
    """
    df_classA_expec_sales= (df_classA_sales['Debit']/Forecast_GUI.forecasted_sales) * expec_sales
    df_classB_expec_sales= (df_classB_sales['Debit']/Forecast_GUI.forecasted_sales) * expec_sales
    df_classC_expec_sales= (df_classC_sales['Debit']/Forecast_GUI.forecasted_sales) * expec_sales

    """

    
    df_classA_expec_sales= (df_classA_sales['Debit']/df_Debit_sum['Debit']) * expec_sales
    df_classB_expec_sales= (df_classB_sales['Debit']/df_Debit_sum['Debit']) * expec_sales
    df_classC_expec_sales= (df_classC_sales['Debit']/df_Debit_sum['Debit']) * expec_sales


    Forecast_GUI.text_widget1.insert('insert',"\nNew expected revenue from class  A dealers: %d\n"%df_classA_expec_sales)
    Forecast_GUI.text_widget1.insert('insert',"\nNew expected revenue from class  B dealers: %d\n"%df_classB_expec_sales)
    Forecast_GUI.text_widget1.insert('insert',"\nNew expected revenue from class  C dealers: %d\n"%df_classC_expec_sales)
    pdf.write(8,'\nNew expected revenue from class A dealers: ' + str(df_classA_expec_sales) + '\n')
    pdf.write(8,'\nNew expected revenue from class B dealers: ' + str(df_classB_expec_sales) + '\n')
    pdf.write(8,'\nNew expected revenue from class C dealers: ' + str(df_classC_expec_sales) + '\n\n')



def reverseforecast():
    temp_revA=0
    temp_revB=0
    temp_revC=0
    df_classA_rev = 0
    df_classB_rev = 0
    df_classC_rev = 0

    global df_classA_new,df_classB_new,df_classC_new

    df_classA_new = pd.DataFrame(columns= ['Name', 'Debit'])
    df_classB_new = pd.DataFrame(columns= ['Name', 'Debit'])
    df_classC_new = pd.DataFrame(columns= ['Name', 'Debit'])

    i=0

    #For Class A

    df_classA_new=df_classA[['Name','Debit']].copy()
    #Forecast_GUI.text_widget1.insert(df_classA_new)

    i=0
    pd.options.mode.chained_assignment = None # Suppress Copy Warning
    while(temp_revA < df_classA_expec_sales and i<count_classA['Debit']):
        if(df_classA['Ratio'].loc[i] > 0.7):
            df_classA_new['Debit'].loc[i] = df_classA_new['Debit'].iloc[i] * 1.20
            temp_revA= temp_revA + df_classA_new['Debit'].iloc[i]
        i=i+1

    i=0    
    while(temp_revA < df_classA_expec_sales and i<count_classA['Debit']):
        if(df_classA['Ratio'].loc[i] > 0.5 and df_classA['Ratio'].loc[i] < 0.7):
            df_classA_new['Debit'].loc[i] = df_classA_new['Debit'].iloc[i] * 1.25 
            temp_revA= temp_revA + df_classA_new['Debit'].iloc[i]
        i=i+1

    i=0    
    while(temp_revA < df_classA_expec_sales and i<count_classA['Debit']):
        if(df_classA['Ratio'].loc[i] > 0.25 and df_classA['Ratio'].loc[i] < 0.5):
            df_classA_new['Debit'].loc[i] = df_classA_new['Debit'].iloc[i] * 1.40 
            temp_revA= temp_revA + df_classA_new['Debit'].iloc[i]
        i=i+1

    df_classA_rev = df_classA_new.sum(axis=0,numeric_only=True)

    


    #For Class B

    df_classB_new=df_classB[['Name','Debit']].copy()
    #Forecast_GUI.text_widget1.insert(df_classB_new)

    i=0
    pd.options.mode.chained_assignment = None # Suppress Copy Warning
    while(temp_revB < df_classB_expec_sales and i<count_classB['Debit']):
        if(df_classB['Ratio'].loc[i] > 0.7):
            df_classB_new['Debit'].loc[i] = df_classB_new['Debit'].iloc[i] * 1.20
            temp_revB= temp_revB + df_classB_new['Debit'].loc[i] 
        i=i+1

    i=0    
    while(temp_revB < df_classB_expec_sales and i<count_classB['Debit']):
        if(df_classB['Ratio'].loc[i] > 0.5 and df_classB['Ratio'].loc[i] < 0.7):
            df_classB_new['Debit'].loc[i] = df_classB_new['Debit'].iloc[i] * 1.25
            temp_revB= temp_revB + df_classB_new['Debit'].loc[i]  
        i=i+1

    i=0    
    while(temp_revB < df_classB_expec_sales and i<count_classB['Debit']):
        if(df_classB['Ratio'].loc[i] > 0.25 and df_classB['Ratio'].loc[i] < 0.5):
            df_classB_new['Debit'].loc[i] = df_classB_new['Debit'].iloc[i] * 1.40
            temp_revB= temp_revB + df_classB_new['Debit'].loc[i]  
        i=i+1

    df_classB_rev = df_classB_new.sum(axis=0,numeric_only=True)

    #For Class C

    df_classC_new=df_classC[['Name','Debit']].copy()
    #Forecast_GUI.text_widget1.insert(df_classA_new)

    i=0
    pd.options.mode.chained_assignment = None # Suppress Copy Warning
    while(temp_revC < df_classC_expec_sales and i<count_classC['Debit']):
        if(df_classC['Ratio'].loc[i] > 0.7):
            df_classC_new['Debit'].loc[i] = df_classC_new['Debit'].iloc[i] * 1.20
            temp_revC= temp_revC + df_classC_new['Debit'].loc[i]  
        i=i+1

    i=0    
    while(temp_revC < df_classC_expec_sales and i<count_classC['Debit']):
        if(df_classC['Ratio'].loc[i] > 0.5 and df_classC['Ratio'].loc[i] < 0.7):
            df_classC_new['Debit'].loc[i] = df_classC_new['Debit'].iloc[i] * 1.25 
            temp_revC= temp_revC + df_classC_new['Debit'].loc[i] 
        i=i+1

    i=0    
    while(temp_revC < df_classC_expec_sales and i<count_classC['Debit']):
        if(df_classC['Ratio'].loc[i] > 0.25 and df_classC['Ratio'].loc[i] < 0.5 ):
            df_classC_new['Debit'].loc[i] = df_classC_new['Debit'].iloc[i] * 1.40 
            temp_revC= temp_revC + df_classC_new['Debit'].loc[i] 
        i=i+1

    df_classC_rev = df_classC_new.sum(axis=0,numeric_only=True)
    Forecast_GUI.text_widget1.insert('insert',"Reverse forecasted revenue from Class A: %d\n"%df_classA_rev)
    Forecast_GUI.text_widget1.insert('insert',"Reverse forecasted revenue from Class B: %d\n"%df_classB_rev)
    Forecast_GUI.text_widget1.insert('insert',"Reverse forecasted revenue from Class C: %d\n"%df_classC_rev)

    total_revenue= df_classA_rev + df_classB_rev + df_classC_rev
    Forecast_GUI.text_widget1.insert('insert',"Total revenue possible from all the dealers: %d\n"%total_revenue)
    pdf.write(8,'Reverse forecasted revenue from Class A: ' + str(df_classA_rev['Debit']) + '\n')
    pdf.write(8,'Reverse forecasted revenue from Class B: ' + str(df_classB_rev['Debit']) + '\n')
    pdf.write(8,'Reverse forecasted revenue from Class C: ' + str(df_classC_rev['Debit']) + '\n')


    pdf.set_font('Arial', 'B', 14)
    pdf.write(8,'\n\nTotal revenue possible from all the dealers: ' + str(total_revenue['Debit']) + '\n')


    pdf.write(8,'\nMost promising dealers in each class are: \n')
    pdf.write(8,'\nClass A: \n')
    for i in range (0,4):
        pdf.write(8,str(df_classA['Name'].iloc[i]) + '\n')
    
    pdf.add_page()
    pdf.write(8,'\nClass B: \n')
    for i in range (0,4):
        pdf.write(8,str(df_classB['Name'].iloc[i]) + '\n')


    pdf.write(8,'\nClass C: \n')
    for i in range (0,4):
        pdf.write(8,str(df_classC['Name'].iloc[i]) + '\n')
    pdf.output('Reverse_Forecasting.pdf','F')

