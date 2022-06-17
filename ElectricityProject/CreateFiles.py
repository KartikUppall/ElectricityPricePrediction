import pandas as pd
import h5py as h5py
import numpy as np
class CreateFiles:

    def createCSVFile(self, predictPrice):
        dataFrame = pd.DataFrame(predictPrice)
        dataFrame.to_csv('Files/ElectricityPricePredictedData.csv', mode='a', index=False, header=False)

    def createHD5File(self, predictPrice):
        d1 = np.random.random(size=(1000, 20))
        hf = h5py.File('Files/HD5 Price Prediction.h5', 'w')
        hf.create_dataset('dataset', data=predictPrice)
        hf.close()
