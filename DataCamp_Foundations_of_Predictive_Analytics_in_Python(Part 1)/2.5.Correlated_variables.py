'''The first 10 variables that are added to the model are the following:

['max_gift', 'number_gift', 'time_since_last_gift', 'mean_gift', 'income_high', 'age', 'country_USA', 'gender_F', 'income_low', 'country_UK']
As you can see, min_gift is not added. Does this mean that it is a bad variable? 
You can test the performance of the variable by using it in a model as a single variable and calculating the AUC. 
How does the AUC of min_gift compare to the AUC of income_high? 
To this end, you can use the function auc():

auc(variables, target, basetable)
It can happen that a good variable is not added because it is highly correlated with a variable that is already in the model. 
You can test this calculating the correlation between these variables:

import numpy
numpy.corrcoef(basetable["variable_1"],basetable["variable_2"])[0,1]'''
#TASK
# Calculate the AUC of the model using the variable min_gift only.
# Calculate the AUC of the model using the variable income_high only.
# Calculate the correlation between the variable min_gift and mean_gift.

import numpy as np

# Calculate the AUC of the model using min_gift only
auc_min_gift = auc([____], ["target"], ____)
print(round(auc_min_gift,2))

# Calculate the AUC of the model using income_high only
auc_income_high = ____([____], [____], ____)
print(round(auc_income_high,2))

# Calculate the correlation between min_gift and mean_gift
correlation = np.corrcoef(basetable["____"], basetable["____"])[0,1]
print(round(correlation,2))






#SOULTION
import numpy as np

# Calculate the AUC of the model using min_gift only
auc_min_gift = auc(['min_gift'], ["target"], basetable)
print(round(auc_min_gift,2))

# Calculate the AUC of the model using income_high only
auc_income_high = auc(['income_high'], ['target'], basetable)
print(round(auc_income_high,2))

# Calculate the correlation between min_gift and mean_gift
correlation = np.corrcoef(basetable["min_gift"], basetable["mean_gift"])[0,1]
print(round(correlation,2))