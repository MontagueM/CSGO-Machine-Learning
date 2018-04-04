import numpy as np
from sklearn.naive_bayes import GaussianNB
from draw_graph import picture

yaxis_max = 0
xaxis_max = 0
yaxis_min = 20
xaxis_min = 20


def predict_func():
    global yaxis_max
    global xaxis_max
    global yaxis_min
    global xaxis_min
    x_list = []
    y_list = []
    f = open("data.txt", 'r')
    for i in f.readlines():
        i_array = i.split(" ")
        x_var1 = int(i_array[0].strip())
        x_var2 = int(i_array[1])
        y_var = int(i_array[2].strip())
        x_var = [x_var1, x_var2]
        x_list.append(x_var)
        y_list.append(y_var)
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
    x_train = np.array(x_list)
    y_train = np.array(y_list)
    classifier = GaussianNB()  # Creating a classifier of a gaussian naive bayes type
    classifier.fit(x_train, y_train)  # Try fit features, X, to labels, Y using training points to train classifier
    prediction_input = input("Prediction in form kills, deaths: ").split(", ")
    to_be_graphed = input("Would you liked it graphed y/n: ").lower()
    kills = int(prediction_input[0])
    deaths = int(prediction_input[1])

    if kills > yaxis_max:
        yaxis_max = kills
    if deaths > xaxis_max:
        xaxis_max = deaths

    prediction = classifier.predict([[kills, deaths]])  # Now attempting to predict a label for a new set of features
    if prediction == 0:
        print("\nPrediction: s1mple for " + str(kills) + " kills and " + str(deaths) + " deaths.\n")
    elif prediction == 1:
        print("\nPrediction: zeus for " + str(kills) + " kills and " + str(deaths) + " deaths.\n")
    else:
        print("Error")
    correct_q = input("Was it right y/n: ").lower()
    if correct_q == "y":
        correct = prediction[0]
    elif correct_q == "n":
        if prediction[0] == 0:
            correct = "1"
        else:
            correct = 0
    else:
        correct = "Error"
    to_save = input("Thanks! Do you want this saved for next time y/n: ").lower()
    if to_save == "y":
        q = open("data.txt", "a")
        towrite = "\n" + str(kills) + " " + str(deaths) + " " + str(correct)
        q.write(towrite)
        q.close()
        print("I'll use this for next time.")
    num_lines = sum(1 for line in open("data.txt"))
    if to_be_graphed == "y":
        picture(classifier, x_list, y_list, num_lines, xaxis_min, xaxis_max, yaxis_min, yaxis_max, to_be_graphed, kills,
                deaths)


def graph_func():
    only_at_end = input("Do you want the end result only (y/n): ").lower()
    global yaxis_max
    global xaxis_max
    global yaxis_min
    global xaxis_min
    x_list = []
    y_list = []
    number = 0
    f = open("data.txt", 'r')
    for read_line in f.readlines():
        i_array = read_line.split(" ")  # Splitting each line into kills | deaths | player#
        x_var1 = int(i_array[0].strip())  # taking the kills number
        x_var2 = int(i_array[1])  # taking the deaths number
        y_var = int(i_array[2].strip())  # taking the player#
        x_var = [x_var1, x_var2]  # making our feature array
        x_list.append(x_var)
        y_list.append(y_var)
        if yaxis_max < x_var1:  # just dabbling with variable maximums and minimums for the graph
            yaxis_max = x_var1
        elif yaxis_min > x_var1:
            yaxis_min = x_var1
        if xaxis_max < x_var2:
            xaxis_max = x_var2
        elif xaxis_min > x_var2:
            xaxis_min = x_var2

        # Using sklearn to train (fit) the algorithm
        X_train = np.array(x_list)
        Y_train = np.array(y_list)
        classifier = GaussianNB()  # Creating a classifier of a gaussian naive bayes type
        classifier.fit(X_train, Y_train)  # Try fit features, X, to labels, Y using training points to train classifier
        num_lines = sum(1 for line in open("data.txt"))
        if number > 0:  # needs to be > 0 as otherwise there aren't any samples
            if only_at_end == "n":  # generating an image for each point
                picture(classifier, x_list, y_list, number, xaxis_min, xaxis_max, yaxis_min, yaxis_max, "n", None, None)
            if only_at_end == "y":  # generating only the last image
                if number == num_lines-1:
                    picture(classifier, x_list, y_list, num_lines, xaxis_min, xaxis_max, yaxis_min, yaxis_max, "n",
                            None, None)
                    break
        number += 1
    f.close()


begin_check = input("Predict (p) or graph (g)? ").lower()

if begin_check == "p":
    predict_func()
elif begin_check == "g":
    graph_func()
else:
    quit()
