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

