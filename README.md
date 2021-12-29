# Analysis-of-social-networks

The file `createGraph.py` is used to create the big graph of all the links in wikispeedia
it uses the function `createGraph` which create the graph and return it

The file `readPath.py` is used to read all the finished paths from the file `data/paths_finished.tsv` it uses the function `read_finished_path` for this job that return a list of all the finished games

Also is used to read all the unfinished paths from the file `data/paths_unfinished.tsv` it uses the function `read_unfinished_path` for this job that return a list of all the finished games

The file  `statisticsOfPaths.py` is used to calc all the indices and make the relvant plots, the result will be saved in the directory `resultsOfAvgClicks`