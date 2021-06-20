import datetime
from collections import namedtuple
from statistics import mean
import csv
import matplotlib.pyplot as plt
from pandas import DataFrame as df
import pandas as pd
from matplotlib import pyplot,style
import PySimpleGUI as sg
import os.path

# Define the window's contents

layout = [[sg.Text("Expense Tracker")],
          #[sg.CalendarButton("Calender",size=(18,1)),sg.Input()],
          [sg.CalendarButton("Calender",size=(18,1))],
          [sg.Text('Category',size=(18, 1)),
           sg.Drop(values=('Food', 'Transport', 'Hobbies', 'Income'), auto_size_text=True)],
          [sg.Text("Item",size=(18,1)),sg.InputText(do_not_clear=False)],
          [sg.Text("expense",size=(18,1)),sg.InputText(do_not_clear=False)],
          [sg.Text("")],
          [sg.Button('Submit'), sg.Button('Cancel')]]

# Create the window

window = sg.Window('Window Title', layout)
print(window,type(window))


#Display and interact with the Window using an Event Loop

while True:
    event, values = window.read()
    #print(event,values,type(event),type(values))
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        window.close()
        print(event,values,type(event),type(values))
        break

    with open('expense.csv', 'a') as csvfile:
        print(values)
        headers = ["Date", "Category", "Item", "Expense"]
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=headers)
        #writer.writeheader()
        writer.writerow({'Date': values['Calender'], 'Category': values[0], 'Item': values[1], 'Expense': values[2]})

#loading the data into data frame

expense_file = pd.read_csv('expense.csv')

#print("dataframe:",X)

expense_sum=expense_file.groupby(['Category'])['Expense'].sum()
print(expense_sum)

print('Income spent on Food:',expense_sum["Food"]/expense_sum["Income"] * 100.0, "%")
print('Income spent on Transport:',expense_sum["Transport"]/expense_sum["Income"] * 100.0, "%")
print('Income spent on Hobbies:',expense_sum["Hobbies"]/expense_sum["Income"] * 100.0, "%")

#Graphical representation of expenses using metplotlib

expense_sum.index
ax = expense_sum.plot.bar(y="Out")
#print(ax)
plt.xticks(rotation=45)
plt.show()



