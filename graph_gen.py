import csv


class VertexSet:

    def __init__(self, file_path):

        self.vertices = []

        self._fetch(file_path)

    def _fetch(self, file_path):

        with open(file_path, 'rb') as csvfile:
            fetched = csv.reader(csvfile, delimiter=',', quotechar='|')

            for row in fetched:

                if len(row) == 4:
                    self.vertices.append(row)
                elif len(row) == 3:
                    self.vertices.append(row.append(''))

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

                if len(row) == 3:
                    self.edges.append(row)
                elif len(row) == 2:
                    self.edges.append(row.append(''))

    def ret_edges(self):

        return self.edges


class Graph:

    def __init__(self, file_path, vertex_set, edge_set, directed=False):
