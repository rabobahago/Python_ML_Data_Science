# What is a confusion matrix?
# It is a table that is used in classification problems to assess where errors in the model were made.
# The rows represent the actual classes the outcomes should have been.
# While the columns represent the predictions we have made. Using this table it is easy to see which predictions are wrong.
# Creating a Confusion Matrix
# Confusion matrixes can be created by predictions made from a logistic regression.

# For now we will generate actual and predicted values by utilizing NumPy:

import numpy
from sklearn import metrics
import matplotlib.pyplot as plt

actual_values = numpy.random.binomial(1, 0.9, size=(1000))
predicted = numpy.random.binomial(1, 0.9, size = 1000)
confusion_matrix = metrics.confusion_matrix(actual_values, predicted)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])
cm_display.plot()
plt.show()