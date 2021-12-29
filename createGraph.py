from urllib.parse import unquote
import networkx as nx


def createGraph():
    def createNodes(g,Lines):
        for line in Lines[12:]:
            article=line.replace('\n', '')
            article = unquote(article)
            g.add_node(article,category=[])
        return g

    def createEdges(g,Lines):
        for line in Lines[12:]:
            line=line.replace('\n', '')
            nodeOne,nodeTwo=line.split('\t')
            nodeOne = unquote(nodeOne)
            nodeTwo = unquote(nodeTwo)
            g.add_edge(nodeOne,nodeTwo)
        return g

    def addCategory(g,Lines):
        for line in Lines[13:]:
            line=line.replace('\n', '')
            node,category=line.split('\t')
            node=unquote(node)
            g.nodes[node]['category'].append(category)

        return g

    fileAticle = open('data/articles.tsv', 'r')
    articlesLines = fileAticle.readlines()
    fileAticle.close()

    fileLinks = open('data/links.tsv', 'r')
    linksLines = fileLinks.readlines()
    fileLinks.close()

    fileCategories = open('data/categories.tsv', 'r')
    categoriesLines = fileCategories.readlines()
    fileCategories.close()

    g = nx.DiGraph()  # create empty graph
    g = createNodes(g,articlesLines)
    g = createEdges(g,linksLines)
    g = addCategory(g,categoriesLines)

    return g

def getCentralityIndices(g):
    k=len(g.nodes()) #paramter to put inside the betweens but it takes time so meanwhile without it
    betweenness = nx.betweenness_centrality(g, k=100)
    # deg_centrality = nx.degree_centrality(g)
    in_degree = nx.in_degree_centrality(g)
    out_deg = nx.out_degree_centrality(g)
    page_rank = nx.pagerank(g)
    closeness= nx.closeness_centrality(g)

    def funcListOfCentralityForGame(game):
        betw_game = [betweenness[x] for x in game]
        in_deg_game = [in_degree[x] for x in game]
        out_deg_game = [out_deg[x] for x in game]
        pge_rnk_game = [page_rank[x] for x in game]
        clos_game = [closeness[x] for x in game]
        return betw_game,in_deg_game,out_deg_game,pge_rnk_game,clos_game

    return funcListOfCentralityForGame