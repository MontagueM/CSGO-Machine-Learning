import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

# Written by Udacity for their ML course. I have added the variable axes and simplified some processes.

legend = 0


def picture(clf, x_test, y_test, int_progressive, xaxis_min, xaxis_max, yaxis_min, yaxis_max, should_add_prediction,
            predict_kills, predict_deaths, player0, player1):
    global legend

    image_name = "images/img" + str(int_progressive) + ".png"

    x_min = xaxis_min-5
    x_max = int(xaxis_max+(xaxis_max/7.5))
    y_min = yaxis_min-5
    y_max = int(yaxis_max+(yaxis_max/7.5))
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    h = 1  # step size in the mesh
    if int_progressive != 1:
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
        z = clf.predict(np.c_[yy.ravel(), xx.ravel()])

        # Put the result into a color plot
        z = z.reshape(xx.shape)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())

        plt.pcolormesh(xx, yy, z, cmap=pl.cm.seismic)

    # Plot points
    kills_player0 = [x_test[ii][0] for ii in range(0, len(x_test)) if y_test[ii] == 0]
    deaths_player0 = [x_test[ii][1] for ii in range(0, len(x_test)) if y_test[ii] == 0]
    kills_player1 = [x_test[ii][0] for ii in range(0, len(x_test)) if y_test[ii] == 1]
    deaths_player1 = [x_test[ii][1] for ii in range(0, len(x_test)) if y_test[ii] == 1]

    plt.scatter(deaths_player0, kills_player0, color="cyan", label=player0)
    plt.scatter(deaths_player1, kills_player1, color="orange", label=player1)
    plt.scatter(xaxis_min - 5, yaxis_min - 5, color="blue", label=player0 + " surface")
    plt.scatter(xaxis_min - 5, yaxis_min - 5, color="red", label=player1 + " surface")

    # Should we add a prediction to the graph?
    if should_add_prediction == "y":
        plt.scatter(predict_deaths, predict_kills, color="green", label="prediction")
        image_name = "images/img" + str(int_progressive) + "_prediction.png"

    # Ensuring only one legend is added
    if legend == 0:
        plt.legend()
        plt.xlabel("deaths")
        plt.ylabel("kills")
        legend = 1

    plt.savefig(image_name)
    print(image_name)
