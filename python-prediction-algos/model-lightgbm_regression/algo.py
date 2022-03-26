from dataiku.doctor.plugins.custom_prediction_algorithm import BaseCustomPredictionAlgorithm  
from modellightgbm import DkuLGBMRegressor
    
class CustomPredictionAlgorithm(BaseCustomPredictionAlgorithm):    
    
    def __init__(self, prediction_type=None, params=None):      
        self.params = params
        self.clf = DkuLGBMRegressor(**self.params)
        super(CustomPredictionAlgorithm, self).__init__(prediction_type, self.params)
        
    def get_clf(self):
        return self.clf