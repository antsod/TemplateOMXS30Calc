import pandas as pd
import numpy as np
import datamodels as dm
import openpyxl as op
import datetime
import time
import datetime
import math
import glob
import os

todaysDate = datetime.datetime.now()
lastWeekdayDate = todaysDate-1;

#todaysDate = datetime.datetime(2022, 6, 8)
#manualCalculationDate = datetime.datetime(2022, 6, 7)

#if 'manualCalculationDate' in locals():
#    lastWeekdayDate = manualCalculationDate

todaysDateWithLine = todaysDate.strftime('%Y-%m-%d')
todaysDateNoLine = todaysDate.strftime('%Y%m%d')
lastWeekdayDateWithLine = lastWeekdayDate.strftime('%Y-%m-%d')
lastWeekdayDateNoLine = lastWeekdayDate.strftime('%Y%m%d')
lastWeekdayDateWithLineUS =  lastWeekdayDate.strftime('%d-%m-%Y')

print("Idag är: " + str(todaysDateWithLine) + ", Beräkningen är för: " + str(lastWeekdayDateWithLine))

fileshare = os.getcwdb()
lastReportedDatefileAtAll= fileshare + '/Reported Values/ReportedPositions_' + '*'

#Hämtar senaste filen för en viss dag. Reported File är alltid senast skapade filen
list_of_files = glob.glob(lastReportedDatefileAtAll)
ReportedPositionsExcel = max(list_of_files, key=os.path.getctime)

print("Idag är: " + str(todaysDateWithLine) + ", Beräkningen är för: " + str(lastWeekdayDateWithLine))
print("Använda ReportedPositionsExcel: " + ReportedPositionsExcel)

list_of_files = glob.glob('/home/jovyan/shared/Kort Netto Beräkning/Reported Values/ReportedPositions_20220603*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

print(latest_file)