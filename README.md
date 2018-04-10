## Machine Learning Naive-Bayes algorithm that learns between the KD of any two CS:GO players.

#### Prerequisites:
- numpy
- sklearn
- matplotlib
- pylab
##### For the web crawler:
- beautifulsoup4
- requests

An easy way to get all the prerequisites is to use Anaconda as your python interpreter, found [here](https://www.anaconda.com/download/).

---------------------------------

#### Style for text.txt:

First line = your first player (#0)
Second line = your second player (#1)

player # as an example:
0 = simple
1 = zeus

Below this the numbers are ordered like this:

kills deaths player

e.g. **23 12 0** means 23 kills, 12 deaths, and is the first player (s1mple).

---------------------------------

#### How to use hltv_crawl.py

Ensure that data.txt only has two lines of the two player names. If this doesn't happen the file will be written to incorrectly and so main.py will not work (e.g. there can be no spaces in the file).

Do not use too many data points as it will clutter the graph and make it unreadable. Personally I have found about 100 points for each player to be a good maximum.