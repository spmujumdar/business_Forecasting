from test_stationarity import test_stationarity
import ReverseForecasting1
import os
import tkFont 
import tkFileDialog
import subprocess
from Tkinter import *
from PIL import Image, ImageTk
import xlsxwriter
import Tkinter 
import tkMessageBox
import Tkinter as tk
from statsmodels.tsa.stattools import adfuller
from numpy import arange, sin, pi
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime
from dateutil.relativedelta import relativedelta

from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure



from tkFileDialog import * 
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

matplotlib.rcParams['figure.facecolor'] = 'w'


def endProgam():
    root.destroy()       

    """

def Next_To_To_Next_Window():
    window3 = tk.Toplevel()
    


    window3.geometry('1300x600')

    B1 = Tkinter.Button(window3, text = "Close", command = endProgam)
    B1.pack()
    B1.place(x= 500, y= 430, anchor = CENTER)

    
    B2= Tkinter.Button(window3, text = "Turnover Live Plot", command ="" )
    B2.pack()
    B2.place(x= 200, y= 200, anchor = CENTER)
        

    B3= Tkinter.Button(window3, text = "Profit Live Plot", command = "")
    B3.pack()
    B3.place(x= 200, y= 300, anchor = CENTER)


    B4= Tkinter.Button(window3, text = "Reverse Forecasting", command = "")
    B4.pack()
    B4.place(x= 70, y= 300, anchor = CENTER)

    
    B5= Tkinter.Button(window3, text = "Generate Output in Excel", command = "")
    B5.pack()
    B5.place(x= 150, y= 400, anchor = CENTER)

    
    B6= Tkinter.Button(window3, text = "Generate Output as PDF", command = "")
    B6.pack()
    B6.place(x= 150, y= 430, anchor = CENTER)

    """
def Next_Window():
    window2 = tk.Toplevel(root)
    window2.geometry('1300x700')
    window2.title("Reverse Forecasting")

    im2 = Image.open('Presentation2.jpg')
    tkimage2 = ImageTk.PhotoImage(im2)
    myvar2=tk.Label(window2,image = tkimage2)
    myvar2.pack()
    myvar2.place(x=0, y=0, relwidth=1, relheight=1)    

    global text_widget1
    text_widget1 = Tkinter.Text(window2)
    text_widget1.pack(anchor = "w", padx = 40, pady = 10)
    text_widget1.insert('insert',"Insert Files for Reverse Forecasting.\nPlease select the category of input data file by clicking the respective button.\n")

    labelframe1 = LabelFrame(window2, text="Reverse Forecasting Functions", font= "Helvetica", height = "5",bg='white' )
    labelframe1.pack(fill="both", expand="yes")


    
    B7= Tkinter.Button(window2,width=15, text="Reverse Forecasting",height= 3, bg='white',activebackground='grey',command=reverese_forecasting)
    B7.pack()
    B7.place(x= 400, y= 460, anchor = CENTER)

    B8= Tkinter.Button(window2,width=15, text="View in PDF", bg='white',activebackground='grey', height=3, command=view_reverse_forecasting_in_pdf)
    B8.pack()
    B8.place(x= 400, y= 540, anchor = CENTER)

    B9= Tkinter.Button(window2,width=15, height=3, text="View in Excel", bg='white',activebackground='grey',command="")
    B9.pack()
    B9.place(x= 400, y= 620, anchor = CENTER)


    B10= Tkinter.Button(window2, width=15,bg='white', activebackground='grey', text = "Dealer File", command =browsedealers)
    B10.pack()
    B10.place(x= 200, y= 450, anchor = CENTER)
 
    """       
    B3= Tkinter.Button(window2, text = "Balance Data", bg='white', activebackground='grey',width=10, command=browse_for_window2_balance_data_file)
    B3.pack()
    B3.place(x= 200, y= 510, anchor = CENTER)

    B4= Tkinter.Button(window2, text = "Profit File",  bg='white',activebackground='grey', width=10, command =browse_for_window2_profit_file )
    B4.pack()
    B4.place(x= 200, y= 560, anchor = CENTER)
        
    B5= Tkinter.Button(window2, text = "Sales File",  bg='white',activebackground='grey', width=10, command = browse_for_window2_sales_file)
    B5.pack()
    B5.place(x= 200, y= 610, anchor = CENTER)
    """


    B11 = Tkinter.Button(window2, text = "Close",  bg='white',activebackground='red', width = 10, command = window2.destroy)
    B11.pack()
    B11.place(x= 1000, y= 630, anchor = CENTER)

    Label(window2, text="Enter Expected Sales").place(x=900,y=240)
    global e1
    e1 = Entry(window2)
    e1.place(x=900,y=260)

    """
    B12 = Tkinter.Button(window2, text = "Enter",  bg='white',activebackground='red', width = 10, command = read_rev_entry)
    B12.pack()
    B12.place(x= 900, y= 300, anchor = CENTER)
    """


    window2.mainloop()
    

def read_rev_entry():
    global rev_entry
    rev_entry = e1.get()
    text_widget1.insert('insert',"The expected sales value is: %s\n"%rev_entry)
    return rev_entry


def browsedealers():
        global filename1
        filename1 = tkFileDialog.askopenfilename(filetypes = (("CSV files", "*.csv")
                                                             ,("All files", "*.*") ))
        if filename1: 
            try: 
                text_widget1.insert('insert',"File path is:\n %s\n"%filename1)
                text_widget1.insert('insert',"Opened File Succesfully\n")
                text_widget1.insert('insert',"Please enter the expected sales value: \n")
                return
            except: 
                tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename1)
                return




def browsesales():
        global filename
        filename = tkFileDialog.askopenfilename(filetypes = (("CSV files", "*.csv")
                                                             ,("All files", "*.*") ))
        if filename: 
            try: 
                text_widget.insert('insert',"File path is:\n %s\n"%filename)
                text_widget.insert('insert',"Opened File Succesfully\n")
                return
            except: 
                tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename)
                return



def browsepurch():
        global filename2
        filename2 = tkFileDialog.askopenfilename(filetypes = (("CSV files", "*.csv")
                                                             ,("All files", "*.*") ))
        if filename2: 
            try: 
                text_widget.insert('insert',"File path is:\n %s\n"%filename2)
                text_widget.insert('insert',"Opened File Succesfully\n")
                return
            except: 
                tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename2)
                return


def browseprof():
        global filename3
        filename3 = tkFileDialog.askopenfilename(filetypes = (("CSV files", "*.csv")
                                                             ,("All files", "*.*") ))
        if filename3: 
            try: 
                text_widget.insert('insert',"File path is:\n %s\n"%filename3)
                text_widget.insert('insert',"Opened File Succesfully\n")
                return
            except: 
                tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename3)
                return



def read_dealer_file():
    df = pd.read_csv(filename1, index_col=False)
    return df







def readfile_sales():
    df = pd.read_csv(filename, index_col=0)
    df.index.name=None
    df.reset_index(inplace=True)
    df.drop(df.index[76], inplace=True)

    start = datetime.datetime.strptime("2010-04-01", "%Y-%m-%d")
    date_list = [start + relativedelta(months=x) for x in range(0,76)]
    df['index'] =date_list
    df.set_index(['index'], inplace=True)
    df.index.name=None
    df.columns= ['Sales']
    return df



def readfile_purch():
    df1 = pd.read_csv(filename2, index_col=0)
    df1.index.name=None
    df1.reset_index(inplace=True)
    df1.drop(df1.index[76], inplace=True)

    start = datetime.datetime.strptime("2010-04-01", "%Y-%m-%d")
    date_list = [start + relativedelta(months=x) for x in range(0,76)]
    df1['index'] =date_list
    df1.set_index(['index'], inplace=True)
    df1.index.name=None
    df1.columns= ['Purchases']
    return df1



def readfile_prof():
    df2 = pd.read_csv(filename3, index_col=0)
    df2.index.name=None
    df2.reset_index(inplace=True)
    df2.drop(df2.index[5], inplace=True)

    start = datetime.datetime.strptime("2010-03-01", "%Y-%m-%d")
    date_list = [start + relativedelta(months=x) for x in range(0,5)]
    df2['index'] =date_list
    df2.set_index(['index'], inplace=True)
    df2.index.name=None
    df2.columns= ['Profit']
    return df2




def basicplot():
    with PdfPages('Basic_Plot.pdf') as pdf:
        df = readfile_sales()
        text_widget.insert('insert',"Plotting Basic Data\n")


        f = Figure(figsize=(6.5,4.5), dpi=100)
        a = f.add_subplot(111)
        a.plot(df.Sales)
        #f.text(.1,.1,txt)
        canvas = FigureCanvasTkAgg(f, root)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx = 40, pady = 10)
        canvas.get_tk_widget().place(x=700, y= 200,  anchor=W)
        f1=plt.figure(figsize=(8,6))
        plt.plot(df.Sales)
        plt.figtext(0.5, 0,"Basic Plot Successful\n", wrap=True,
                    horizontalalignment='center', fontsize=12)
        pdf.savefig(f1)
        text_widget.insert('insert',"Output saved to the file: Basic_Plot.pdf\n")






def sales_forecast():
    with PdfPages('Forecasted_Plot.pdf') as pdf:
        df=readfile_sales()

        df.Sales_log= df.Sales.apply(lambda x: np.log(x))
        df['first_difference'] = df.Sales - df.Sales.shift(1)
        df['log_first_difference'] = df.Sales_log - df.Sales_log.shift(1)
        df['seasonal_difference'] = df.Sales - df.Sales.shift(12)
        df['log_seasonal_difference'] = df.Sales_log - df.Sales_log.shift(12)
        df['seasonal_first_difference'] = df.first_difference - df.first_difference.shift(12)
        df['log_seasonal_first_difference'] = df.log_first_difference - df.log_first_difference.shift(12)
        #test_stationarity(df.log_seasonal_first_difference.dropna(inplace=False))
        """
        plt.figure("ACF & PACF Plots")
        ax1 = plt.subplot(211)
        sm.graphics.tsa.plot_acf(df.seasonal_first_difference.iloc[13:], lags=40, ax=ax1)
        ax2 = plt.subplot(212)
        fig = sm.graphics.tsa.plot_pacf(df.seasonal_first_difference.iloc[13:], lags=40, ax=ax2)
        plt.show()
        """
        mod = sm.tsa.statespace.SARIMAX(df.Sales, trend='n', order=(2,1,2), seasonal_order=(0,1,1,12))
        results = mod.fit(disp=0)
        #print results.summary()


        #df['forecast'] = results.predict(start = 35, end= 76, dynamic= True)  
        #df[['Sales', 'forecast']].plot(figsize=(12, 8))
        #plt.show()


        start = datetime.datetime.strptime("2016-09-01", "%Y-%m-%d")
        date_list = [start + relativedelta(months=x) for x in range(0,12)]
        future = pd.DataFrame(index=date_list, columns= df.columns)
        df = pd.concat([df, future])


        f = Figure(figsize=(6.5,4.5), dpi=100)
        a = f.add_subplot(111)
        df['forecast'] = results.predict(start = 56, end = 90, dynamic= True)  
        #df[['Sales', 'forecast']].plot()
        a.plot(df.Sales)
        a.plot(df.forecast,color='green') 
        text_widget.insert('insert',"Forecasting Sales for 2017...\n")
        #df[['Sales', 'forecast']].ix[-24:].plot(figsize=(12, 8)) 
        #plt.show()

        canvas = FigureCanvasTkAgg(f, root)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx = 40, pady = 10)
        canvas.get_tk_widget().place(x=700, y= 200,  anchor=W)
        df['forecast'].dropna(inplace=True)
        #print (df['forecast'])
        global forecasted_sales
        forecasted_sales=0
        for i in range(18,30):
            forecasted_sales= forecasted_sales + df['forecast'].iloc[i]
        text_widget.insert('insert',"Forecasted Sales for FY 2017: %d\n"%forecasted_sales)
        f2=plt.figure(figsize=(10,8))
        plt.plot(df.Sales)
        plt.plot(df.forecast,color='green')
        plt.figtext(0.5, 0,"Forecast Successful\nForecasted Sales for FY 2017: %d\n"%forecasted_sales, wrap=True,
                    horizontalalignment='center', fontsize=12)
        pdf.savefig(f2)
        text_widget.insert('insert',"Output saved to the file: Forecasted_Plot.pdf\n")



def purch_forecast():
    with PdfPages('Forecasted_Purch_Plot.pdf') as pdf:
        df1=readfile_purch()

        df1.Purchases_log= df1.Purchases.apply(lambda x: np.log(x))
        df1['first_difference'] = df1.Purchases - df1.Purchases.shift(1)
        df1['log_first_difference'] = df1.Purchases_log - df1.Purchases_log.shift(1)
        df1['seasonal_difference'] = df1.Purchases - df1.Purchases.shift(12)
        df1['log_seasonal_difference'] = df1.Purchases_log - df1.Purchases_log.shift(12)
        df1['seasonal_first_difference'] = df1.first_difference - df1.first_difference.shift(12)
        df1['log_seasonal_first_difference'] = df1.log_first_difference - df1.log_first_difference.shift(12)
        #test_stationarity(df1.log_seasonal_first_difference.dropna(inplace=False))
        """
        plt.figure("ACF & PACF Plots")
        ax1 = plt.subplot(211)
        sm.graphics.tsa.plot_acf(df1.seasonal_first_difference.iloc[13:], lags=40, ax=ax1)
        ax2 = plt.subplot(212)
        fig = sm.graphics.tsa.plot_pacf(df1.seasonal_first_difference.iloc[13:], lags=40, ax=ax2)
        plt.show()
        """
        mod = sm.tsa.statespace.SARIMAX(df1.Purchases, trend='n', order=(2,1,2), seasonal_order=(2,1,1,12),enforce_stationarity= False, enforce_invertibility= False )
        results = mod.fit(disp=0)
        #print results.summary()


        df1['forecast'] = results.predict(start = 35, end= 76, dynamic= True)  
        #df1[['Purchases', 'forecast']].plot(figsize=(12, 8))
        #plt.show()


        start = datetime.datetime.strptime("2016-09-01", "%Y-%m-%d")
        date_list = [start + relativedelta(months=x) for x in range(0,12)]
        future = pd.DataFrame(index=date_list, columns= df1.columns)
        df1 = pd.concat([df1, future])


        f = Figure(figsize=(6.5,4.5), dpi=100)
        a = f.add_subplot(111)
        df1['forecast'] = results.predict(start = 65, end = 85, dynamic= True)  
        #df1[['Purchases', 'forecast']].plot()
        a.plot(df1.Purchases)
        a.plot(df1.forecast,color='green') 
        text_widget.insert('insert',"Forecasting Purchases for 2017...\n")
        #df1[['Purchases', 'forecast']].ix[-24:].plot(figsize=(12, 8)) 
        #plt.show()

        canvas = FigureCanvasTkAgg(f, root)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx = 40, pady = 10)
        canvas.get_tk_widget().place(x=700, y= 200,  anchor=W)
        df1['forecast'].dropna(inplace=True)
        #print (df1['forecast'])
        global forecasted_Purchases
        forecasted_Purchases=0
        for i in range(df1['forecast'].count()-13,df1['forecast'].count()-1):
            forecasted_Purchases= forecasted_Purchases + df1['forecast'].iloc[i]
        text_widget.insert('insert',"Forecasted Purchases for FY 2017: %d\n"%forecasted_Purchases)
        f2=plt.figure(figsize=(10,8))
        plt.plot(df1.Purchases)
        plt.plot(df1.forecast,color='green')
        plt.figtext(0.5, 0,"Forecast Successful\nForecasted Purchases for FY 2017: %d\n"%forecasted_Purchases, wrap=True,
                    horizontalalignment='center', fontsize=12)
        pdf.savefig(f2)
        text_widget.insert('insert',"Output saved to the file: Forecasted_Purch_Plot.pdf\n")



def profit_forecast():
    with PdfPages('Forecasted_Prof_Plot.pdf') as pdf:
        df2=readfile_prof()

        df2.Profit_log= df2.Profit.apply(lambda x: np.log(x))
        df2['first_difference'] = df2.Profit - df2.Profit.shift(1)
        df2['log_first_difference'] = df2.Profit_log - df2.Profit_log.shift(1)
        df2['seasonal_difference'] = df2.Profit - df2.Profit.shift(12)
        df2['log_seasonal_difference'] = df2.Profit_log - df2.Profit_log.shift(12)
        df2['seasonal_first_difference'] = df2.first_difference - df2.first_difference.shift(12)
        df2['log_seasonal_first_difference'] = df2.log_first_difference - df2.log_first_difference.shift(12)
        #test_stationarity(df2.log_seasonal_first_difference.dropna(inplace=False))
        """
        plt.figure("ACF & PACF Plots")
        ax1 = plt.subplot(211)
        sm.graphics.tsa.plot_acf(df2.seasonal_first_difference.iloc[13:], lags=40, ax=ax1)
        ax2 = plt.subplot(212)
        fig = sm.graphics.tsa.plot_pacf(df2.seasonal_first_difference.iloc[13:], lags=40, ax=ax2)
        plt.show()
        """
        mod = sm.tsa.statespace.SARIMAX(df2.Profit, trend='n', order=(1,0,1), seasonal_order=(1,0,0,1),enforce_stationarity= False, enforce_invertibility= False )
        results = mod.fit(disp=0)
        #print results.summary()


        df2['forecast'] = results.predict(start = 1, end= 6, dynamic= True)  
        #df2[['Profit', 'forecast']].plot(figsize=(12, 8))
        #plt.show()


        start = datetime.datetime.strptime("2016-03-01", "%Y-%m-%d")
        date_list = [start + relativedelta(years=x) for x in range(0,1)]
        future = pd.DataFrame(index=date_list, columns= df2.columns)
        df2 = pd.concat([df2, future])


        f = Figure(figsize=(6.5,4.5), dpi=100)
        a = f.add_subplot(111)
        df2['forecast'] = results.predict(start =3, end = 7, dynamic= True)  
        #df2[['Profit', 'forecast']].plot()
        x = ['Frogs', 'Hogs', 'Bogs', 'Slogs','Vlogs']
        a.plot(df2.Profit)
        a.plot(df2.forecast,color='green')
        
        plt.xticks([1,2,3,4,5,6,7],label=x, rotation='vertical') 
        text_widget.insert('insert',"Forecasting Profit for 2017...\n")
        #df2[['Profit', 'forecast']].ix[-24:].plot(figsize=(12, 8)) 
        #plt.show()

        canvas = FigureCanvasTkAgg(f, root)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx = 40, pady = 10)
        canvas.get_tk_widget().place(x=700, y= 200,  anchor=W)
        df2['forecast'].dropna(inplace=True)
        #print (df2['forecast'])
        global forecasted_Profit
        forecasted_Profit=0
        text_widget.insert('insert',"Forecasted Profit for FY 2017: \n")
        text_widget.insert('insert',str(df2['forecast']) + "\n")
        f2=plt.figure(figsize=(10,8))
        #plt.plot(df2.Profit)
        plt.plot(df2.forecast,color='green')
        pdf.savefig(f)
        text_widget.insert('insert',"Output saved to the file: Forecasted_Prof_Plot.pdf\n")


def reverese_forecasting():
    ReverseForecasting1.initialize_data()
    ReverseForecasting1.calc_expec_sales()
    ReverseForecasting1.reverseforecast()

    



def turn_over_plot():
    df = readfile_sales()
    j=1
    turnover = [0,0,0,0,0,0]
    while (j < 6):
        for i in range (12*(j-1),12*j):
            turnover[j-1]= turnover[j-1] + df['Sales'].iloc[i]
        j=j+1
    turnover[5] = forecasted_sales
    """
    top=[('2010',turnover[0]),('2011',turnover[1]),('2012',turnover[2]),('2013',turnover[3]),('2014',turnover[4])]
    labels, ys = zip(*top)
    xs = np.arange(len(labels)) 
    width = 1

    plt.bar(xs, ys, width, align='center')

    plt.xticks(xs, labels) #Replace default x-ticks with xs, then replace xs with labels
    plt.yticks(ys)
    plt.show()
    """
    f = Figure(figsize=(6.5,4.5), dpi=100)
    a = f.add_subplot(111)
    x=range(6)
    a.plot(turnover)
    canvas = FigureCanvasTkAgg(f, root)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx = 40, pady = 10)
    canvas.get_tk_widget().place(x=700, y= 200,  anchor=W)
    j=2010
    for i in range (0,5):
        text_widget.insert('insert',"Turnover for year " + str(j) + ": %d\n")
     
    




def view_reverse_forecasting_in_pdf():

    os.startfile('Reverse_Forecasting.pdf')



def view_file():
    if(open('Basic_Plot.pdf')):
        os.startfile('Basic_Plot.pdf')
    os.startfile('Forecasted_Plot.pdf')








#MAIN WINDOW

root = Tkinter.Tk()
root.geometry('1300x700')
root.title('BUSINESS FORECASTING USING BI & DM')

im = Image.open('Presentation1.jpg')
tkimage = ImageTk.PhotoImage(im)
myvar=Tkinter.Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)



text_widget = Tkinter.Text(root)
text_widget.pack(anchor = "w", padx = 40, pady = 10)
text_widget.insert('insert',"Welcome to Business Forecasting.\nPlease select the input data file by clicking the browse button.\n")


labelframe = LabelFrame(root, text="Welcome to Forecasting", font= "Helvetica", height = "5",bg='white' )
labelframe.pack(fill="both", expand="yes")
label1 = Tkinter.Label(root, text = "Step 1. Upload sales file in CSV format\n Step 2. Enter values. \n Step 3. Forecast ")
label1.pack()

B1 = Tkinter.Button(root, text ="Basic Plot", bg='white', command = basicplot,width=10)
B1.pack()
B1.place(x=200,y=450,anchor=CENTER)

B2 = Tkinter.Button(root, text = "Sales Forecast", bg='white', command = sales_forecast, width = 10)
B2.pack()
B2.place(x=400, y= 550,  anchor=CENTER)


B3 = Tkinter.Button(root, text ="Quit", bg='white', activebackground='red', command = endProgam, width = 10)
B3.pack()
B3.place(x=200, y=550,anchor=CENTER)



#img1_next = PhotoImage("C:\Users\admin\Downloads\Forecast_GUI\Forecast_GUI\images\next.jpg")
B4 = Tkinter.Button(root,width=10, text="Next", bg='white',activebackground='grey',command=Next_Window)
#B5.config(image=img1_next)
B4.pack()
B4.place(x= 1000, y=600, anchor = CENTER)


browsebutton= Tkinter.Button(root, text = "Sales File",bg='white', command = browsesales, width = 10)
browsebutton.pack()
browsebutton.place(x= 400, y= 450, anchor = CENTER)

B5 = Tkinter.Button(root,width=10, text="View PDFs", bg='white',activebackground='grey',command=view_file)
#B5.config(image=img1_next)
B5.pack()
B5.place(x= 1000, y=450, anchor = CENTER)


purchase_button= Tkinter.Button(root, text = "Purchase File",  bg='white',activebackground='grey', width=10, command =browsepurch )
purchase_button.pack()
purchase_button.place(x= 500, y= 450, anchor = CENTER)

prof_button= Tkinter.Button(root, text = "Profit File",  bg='white',activebackground='grey', width=10, command =browseprof )
prof_button.pack()
prof_button.place(x= 600, y= 450, anchor = CENTER)

purch = Tkinter.Button(root, text = "Purchase Forecast", bg='white', command = purch_forecast, width = 12)
purch.pack()
purch.place(x=500, y= 550,  anchor=CENTER)


prof = Tkinter.Button(root, text = "Profit Forecast", bg='white', command = profit_forecast, width = 10)
prof.pack()
prof.place(x=600, y= 550,  anchor=CENTER)


turnover_button= Tkinter.Button(root, text = "Turnover Plot",  bg='white',activebackground='grey', width=10, command =turn_over_plot )
turnover_button.pack()
turnover_button.place(x= 700, y= 450, anchor = CENTER)


pathlabel = Label(root)
pathlabel.pack()


root.mainloop()




