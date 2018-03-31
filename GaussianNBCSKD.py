import numpy as np
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
import pylab as pl

yaxis_max = 0
xaxis_max = 0
yaxis_min = 20
xaxis_min = 20


def pretty_picture(clf, X_test, y_test):  # From Udacity course "Intro to Machine Learning"
    x_min = xaxis_min-5
    x_max = int(xaxis_max+(xaxis_max/7.5))
    y_min = yaxis_min-5
    y_max = int(yaxis_max+(yaxis_max/7.5))
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    h = 0.25  # step size in the mesh
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[yy.ravel(), xx.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.pcolormesh(xx, yy, Z, cmap=pl.cm.seismic)

    # Plot also the test points
    kills_sig = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    deaths_sig = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    kills_bkg = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 1]
    deaths_bkg = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 1]

    plt.scatter(deaths_sig, kills_sig, color="cyan", label="s1mple")
    plt.scatter(deaths_bkg, kills_bkg, color="orange", label="zeus")
#    plt.scatter(deaths, kills, color="green", label="prediction")
    plt.scatter(xaxis_min-5, yaxis_min-5, color="blue", label="s1mple surface")
    plt.scatter(xaxis_min-5, yaxis_min-5, color="red", label="zeus surface")
#    plt.xlabel("deaths")
#    plt.ylabel("kills")
    plt.legend()
    plt.savefig("img.png")
    print("img.png")


def predict_func():
    global yaxis_max
    global xaxis_max
    global yaxis_min
    global xaxis_min
    X_list = []
    Y_list = []
    f = open("data.txt", 'r')
    for i in f.readlines():
        i_array = i.split(" ")
        x_var1 = int(i_array[0].strip())
        x_var2 = int(i_array[1])
        y_var = int(i_array[2].strip())
        x_var = [x_var1, x_var2]
        X_list.append(x_var)
        Y_list.append(y_var)
        if xaxis_max < x_var1:
            xaxis_max = x_var1
        elif xaxis_min > x_var1:
            xaxis_min = x_var1
        if yaxis_max < x_var2:
            yaxis_max = x_var2
        elif yaxis_min > x_var2:
            yaxis_min = x_var2
    # Using sklearn to train (fit) the algorithm
    f.close()
    X_train = np.array(X_list)
    Y_train = np.array(Y_list)
    classifier = GaussianNB()  # Creating a classifier of a gaussian naive bayes type
    classifier.fit(X_train, Y_train)  # Try fit features, X, to labels, Y using training points to train classifier
    prediction_input = input("Prediction in form kills, deaths: ").split(", ")
    kills = int(prediction_input[0])
    deaths = int(prediction_input[1])

    if kills > yaxis_max:
        yaxis_max = kills
    if deaths > xaxis_max:
        xaxis_max = deaths

    prediction = classifier.predict([[kills, deaths]])  # Now attempting to predict a label for a new set of features
    if prediction == 0:
        print("s1mple")
    elif prediction == 1:
        print("zeus")
    else:
        print("Error")


def graph_func():
    global yaxis_max
    global xaxis_max
    global yaxis_min
    global xaxis_min
    X_list = []
    Y_list = []
    number = 0
    f = open("data.txt", 'r')
    for i in f.readlines():
        i_array = i.split(" ")
        x_var1 = int(i_array[0].strip())
        x_var2 = int(i_array[1])
        y_var = int(i_array[2].strip())
        x_var = [x_var1, x_var2]
        X_list.append(x_var)
        Y_list.append(y_var)
        if xaxis_max < x_var1:
            xaxis_max = x_var1
        elif xaxis_min > x_var1:
            xaxis_min = x_var1
        if yaxis_max < x_var2:
            yaxis_max = x_var2
        elif yaxis_min > x_var2:
            yaxis_min = x_var2

    # Using sklearn to train (fit) the algorithm
    X_train = np.array(X_list)
    Y_train = np.array(Y_list)
    classifier = GaussianNB()  # Creating a classifier of a gaussian naive bayes type
    classifier.fit(X_train, Y_train)  # Try fit features, X, to labels, Y using training points to train classifier
    pretty_picture(classifier, X_list, Y_list)
    f.close()


begin_check = input("Predict (p) or graph (g)? ")

if begin_check == "p":
    predict_func()
elif begin_check == "g":
    graph_func()
else:
    quit()
