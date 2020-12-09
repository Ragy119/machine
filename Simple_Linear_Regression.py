class Simple_Linear_Regression :
    # Attributes  if any
    import numpy as np   # For Matrices Manipulations
    import pandas as pd  # For Data frames etc 
    import xlrd  # For Excel Files
    import os   # For Changing to the Correct Directory 

    def __init__(self,X_train,X_test,y_train,y_test):
        self.X_train = X_train 
        self.X_test  = X_test
        self.y_train = y_train
        self.y_test  = y_test
    
    def Mean(self,values):
        return(np.sum(values)/len(values))
    
    def Variance(self,values):
        ME = self.Mean(values)
        return(np.sum((values-ME)**2)/len(values))
    
    def Covariance(self,values1,values2):
        ME1 = self.Mean(values1)
        ME2 = self.Mean(values2)
        co = np.sum((values1-ME1)*(values2-ME2))/len(values1)
        return co
    
    # calculate the cofficent  
    def Coefficents(self):
        b1 = self.Covariance(self.X_train,self.y_train)/self.Variance(self.X_train)
        b0 = self.Mean(self.y_train)-(self.Mean(self.X_train)*b1)
        return b1,b0
    
    # predicte y from X_test
    def simple_linear_regression(self):
        b1,b0 =self.Coefficents()
        self.y_pre=(b1*self.X_test)+b0
        return self.y_pre
    
    
    def MSE(self,actual,predicted):
        SE = 0
        for i in range(len(actual)):
            SE += (actual[i]-predicted[i])**2
        #return(np.sum((actual-predicted)**2)/len(actual))
        return SE/len(actual)
    
    # calculate MSE between y_test and y_predicted
    def Evaluate(self):
        y_pre= self.simple_linear_regression()
        return (self.MSE(self.y_test,y_pre))
    
    def Vizualize(self):
        y_pre= self.simple_linear_regression()
        plt.figure(figsize=(10,8))
        plt.title('PREDICTION VS ACTUAL ', fontsize=24 , fontstyle='italic')
        plt.scatter(self.X_test,self.y_test)
        plt.plot(self.X_test, y_pre, linewidth=2.0)  ## REPLACE X AND Y WITH  X_test AND PREDS ARRAYS! 
        plt.show          # You can make this on your own by plotting  Points and Line 
                        # plt.scatter () , plt.plot()
         
