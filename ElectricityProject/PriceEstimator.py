from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class PriceEstimator:
    def predictPrice(self, dataSet):
        a = dataSet[["DD", "YYYY", "WindProductionPrediction", "SystemLoad",
                     "PPSCL", "Temperature", "Windspeed", "CO2Potency",
                     "OriginalWindProduction", "SystemLoad2"]]
        b = dataSet["PPSCL2"]

        aTraining, aTest, bTraining, bTest = train_test_split(a, b,
                                                              test_size=0.0002,
                                                              random_state=55)

        model = RandomForestRegressor()
        model.fit(aTraining, bTraining)
        valueSet = {'bootstrap': True, 'ccp_alpha': 0.0, 'criterion': 'mse', 'max_depth': None,
                    'max_features': 'auto', 'max_leaf_nodes': None,
                    'max_samples': None, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1,
                    'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0,
                    'n_estimators': 100, 'n_jobs': None, 'oob_score': False,
                    'random_state': None, 'verbose': 0, 'warm_start': False}
        RandomForestRegressor(valueSet)

        predictedPrice = model.predict(aTest)
        predictedPrice2 = model.predict(aTraining)
        yearSet = aTest["YYYY"]
        return yearSet, predictedPrice, predictedPrice2