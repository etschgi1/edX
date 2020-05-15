import pylab as plt
datapoints = [1, 2, 2, 4, 5.3, 7, 8, 6, 12, 15.2]
time = [i+1 for i in range(10)]


def _calc_error(data, predict):
    """takes in experiment data and predicted datapoint returns
    the average mean square error"""
    error = []
    for i in range(len(data)):
        error.append((data[i]-predict[i])**2)
    return sum(error)/len(error)


# plot values
plt.plot(time, datapoints, "ro", label="Measuered points")
# degree of polinomial to fit
degree = 1

res = plt.polyfit(time, datapoints, degree)
estdata = plt.polyval(res, time)
# compute error
print(f"Error: {_calc_error(datapoints, estdata)}")
plt.plot(time, estdata, 'b', label='linear fit, k = '+str(round(res[0], 2)))
plt.legend(loc="upper left")
plt.show()
