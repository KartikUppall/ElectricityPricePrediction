# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.

import pandas as pd
from CorrectingDataType import *
from CreateBarGraph import *
from PriceEstimator import *
from CreateFiles import *


dataSet = pd.read_csv('Files/data_set.csv')

# To change all data to numeric
cdt =  CorrectingDataType()
dataSet = cdt.changeDataToNumeric(dataSet)

# To Predict electricity price
priceEstimator = PriceEstimator()
yearSet, predictPrice, predictedPrice2 = priceEstimator.predictPrice(dataSet)

# To create bar graph
createBarGraph = CreateBarGraph()
predictPriceForGraph = np.round(predictPrice, 2)
createBarGraph.priceVsYear(yearSet, predictPriceForGraph)

# To create CSV and HD5 File
createFiles = CreateFiles()
createFiles.createCSVFile(predictedPrice2)
createFiles.createHD5File(predictedPrice2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
