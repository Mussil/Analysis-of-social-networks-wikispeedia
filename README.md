# Analysis of social networks

## About
[Wikispeedia](https://dlab.epfl.ch/wikispeedia/play/) - is an online game, in which the participant receives a source article and a target article at random (or can choose for himself). <br>
From the initial article he must navigate to the target article, using the links of wikipedia.

The information is collected by dlab - Data Science Lab, and includes the articles in the selected track and also includes the check mark '<' which represents a backward click on the previous article.
In addition the data is divided into:
* finshied games that reached the target article
* failed games that retired in the middle or reached the time limit.
Additional data saved: the level of difficulty the person ranks the game, the amount of time it took him to complete the game or give up, the encrypted IP address of the game and a timestamp indicating the start time of the game.
Beyond that each article has a category, or a number of categories belonging to it.

The game is based on an abbreviated version of wikipedia that includes only 4604 articles, and about 119,882 links that create a Network Graph through which we can draw conclusions.
The dataset exists on Stanford University's website at Wikispeedia navigation paths.

As part of the __Social Network Analysis course__, we researched this dataset.

### The research question
What characterizes a person's choices during a game towards the goal link?

### The research assumption
We assume that at the beginning of the game the average person will try to expand his options and "escape" from the randomly selected source link (compared to the target link) and after he already has good enough options he will start choosing the appropriate links logically.


### Examples
To understand the choice of track, we calculated the mean, median and standard deviation of the Out degree of game tracks in different lengths: <br>
![image](https://user-images.githubusercontent.com/79862052/153243310-81e9f379-6927-4bce-9a35-c7759532da85.png) <br>
It can be seen that at about the beginning, before the first click, the Out degree is very low and converges to low values, but the significant jump comes at the next click, where similar to our assumption the game person tries to reach an article that will allow him many exit links.
It can also be seen that even in the last article, the target article, the indices are low.

### Discussion of results
We confirmed the hypothesis, a person who plays the game wikispeedia at his first click selects an article with a high centralization indices, which indicates an article from which it is possible to expand and reach others. <br>
In this way he opens up many more options that will give him an wide gate to more relevant topics and articles. The start article is not significant because it was chosen at random and the purpose of the person playing is to escape from it.
As the game progresses the centralization indices decreases so that it begins to converge towards the target article, and the player can play according to articles corresponding to the target article.
In addition to the majority, the higher the number of exits (out degree), the shorter the route to the target article.
Similarly, in successful routes the slope is sharper compared to the unsuccessful ones while in long routes (7 clicks or more) there is no significant difference in slope. This is because in successful routes higher values ​​start at significantly lower values ​​than in unsuccessful routes.

## 💻technologies:
* Language:<br /> 
 -- python
* Workspace:<br /> 
 -- PyCharm
* Libraries:<br /> 
 -- __networkx__ <br /> 
 -- matplotlib.pyplot <br /> 
 -- matplotlib <br />

## The files
The file `createGraph.py` is used to create the big graph of all the links in wikispeedia
it uses the function `createGraph` which create the graph and return it

The file `readPath.py` is used to read all the finished paths from the file `data/paths_finished.tsv` it uses the function `read_finished_path` for this job that return a list of all the finished games

Also is used to read all the unfinished paths from the file `data/paths_unfinished.tsv` it uses the function `read_unfinished_path` for this job that return a list of all the finished games

The file  `statisticsOfPaths.py` is used to calc all the indices and make the relvant plots

The file  `graphDetails.py` is used to calculate from the graph the degree distribution for both the original graph & the largest connected component. In addition, in this file we calculated the number of clicks for all egdes from the finished paths.
