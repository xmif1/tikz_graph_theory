import csv


class VertexSet:

    def __init__(self, file_path):

        self.vertices = []

        self._fetch(file_path)

    def _fetch(self, file_path):

        with open(file_path, 'rb') as csvfile:
            fetched = csv.reader(csvfile, delimiter=',', quotechar='|')

            for row in fetched:
                self.vertices.append(row)

    def ret_vertices(self):

        return self.vertices


class EdgeSet:

    def __init__(self, file_path):

        self.edges = []

        self._fetch(file_path)

    def _fetch(self, file_path):

        with open(file_path, 'rb') as csvfile:
            fetched = csv.reader(csvfile, delimiter=',', quotechar='|')

            for row in fetched:
                self.edges.append(row)

    def ret_edges(self):

        return self.edges


class Graph:

    def __init__(self, file_path, vertex_set, edge_set, directed=False):

        self.write_loc = file_path
        self.vertex_set = vertex_set
        self.edge_set = edge_set

        if directed:
            self.edge_format = '->'
        else:
            self.edge_format = '-'

        self.tikz_code_gen()

    def tikz_code_gen(self):

        init_str = '\documentclass{article}\n\n\usepackage{tikz}\n\usetikzlibrary{arrows.meta}\n\n\\begin{document}' \
                   '\n\\begin{tikzpicture}\n\\begin{scope}[every node/.style={circle,thick,draw}]'

        for vertex in self.vertex_set:
            init_str += '\n\t\\node (' + str(vertex[0]) + ') at (' + str(vertex[1]) + ',' + str(vertex[2]) + ') {' \
                        + str(vertex[0]) + '};'

        init_str += '\n\end{scope}\n\\begin{scope}[>={Stealth[black]},\nevery node/.style={fill=white,circle},\n' \
                    'every edge/.style={draw=red,very thick}]'

        for edge in self.edge_set:
            init_str += '\n\t\\path [' + self.edge_format + '] (' + str(edge[0]) + ') edge'

            if str(edge[2]) is not '':
                init_str += '[' + str(edge[2]) + ']'

            if str(edge[3]) is not '':
                init_str += ' node {$' + str(edge[3]) + '$}'

            init_str += ' (' + str(edge[1]) + ');'

        init_str += '\n\end{scope}\n\n\end{tikzpicture}\n\end{document}'

        with open(self.write_loc, 'w') as textfile:
            textfile.write(init_str)


vertices = VertexSet('/Users/xandrumifsud/Desktop/test/v.csv')
vertices = vertices.ret_vertices()

edges = EdgeSet('/Users/xandrumifsud/Desktop/test/e.csv')
edges = edges.ret_edges()

Graph('/Users/xandrumifsud/Desktop/test/code.txt', vertices, edges, directed=True)
