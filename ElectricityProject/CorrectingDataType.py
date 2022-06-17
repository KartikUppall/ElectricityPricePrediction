import pandas as pd


class CorrectingDataType:

    def changeDataToNumeric(self, dataSet):

        dataSet["Windspeed"] = pd.to_numeric(dataSet["Windspeed"], errors='coerce')
        dataSet["CO2Potency"] = pd.to_numeric(dataSet["CO2Potency"], errors='coerce')
        dataSet["SystemLoad"] = pd.to_numeric(dataSet["SystemLoad"], errors='coerce')
        dataSet["SystemLoad2"] = pd.to_numeric(dataSet["SystemLoad2"], errors='coerce')
        dataSet["PPSCL"] = pd.to_numeric(dataSet["PPSCL"], errors='coerce')
        dataSet["PPSCL2"] = pd.to_numeric(dataSet["PPSCL2"], errors='coerce')
        dataSet["Temperature"] = pd.to_numeric(dataSet["Temperature"], errors='coerce')
        dataSet["WindProductionPrediction"] = pd.to_numeric(dataSet["WindProductionPrediction"], errors='coerce')
        dataSet["OriginalWindProduction"] = pd.to_numeric(dataSet["OriginalWindProduction"], errors='coerce')

        dataSet = dataSet.dropna()

        return dataSet
