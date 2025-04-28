#
# Directional graph class implementation for practical 6
#


from Practical_6 import LinkedList as LL


class DSAGraph():
    #----------- Private inner GraphNode class -----------#
    class _DSAGraphVertex():
        def __init__(self, _label: str=None, _data=None):
            self._label = _label
            self._data = _data
            self._connections = LL.DSALinkedList()
            self._visited = False
            self._outDegree = 0
            self._inDegree = 0

        def getLabel(self):
            return self._label

        def getData(self):
            return self._data

        def getNeighbours(self):
            return self._connections.values()

        def getConnections(self):
            connectionString = ""
            nextVertex = self._connections.head

            while nextVertex._next is not None:
                connectionList.insertLast(self._label + nextVertex._data._label)
                nextVertex = nextVertex._next
            return connectionList

        def addEdge(self, sink: str):
            self._inDegree += 1
            self._connections.insertLast(sink)

        def _setVisited(self):
            self._visited = True

        def _clearVisited(self):
            self._visited = False

        def _getVisited(self):
            return self._visited

    #--------------------- Graph class ---------------------#
    def __init__(self):
        self.vertices = LL.DSALinkedList("Vertices")

    def addVertex(self, label: str, data=None):
        if self.vertexFind(label):
            raise ValueError("Vertex label already in use")
        else:
            newVertex = self._DSAGraphVertex(label, data)
            self.vertices.insertLast(newVertex)

    def addEdge(self, sourceLabel: str, sinkLabel: str):
        sourceVertex = self.getVertex(sourceLabel)

        if self.vertexFind(sourceLabel) == False:
            raise Exception("Source vertex not found")
        elif sourceVertex._connections.find(sinkLabel):
            raise Exception("Edge between these vertices already exists")

        self.getVertex(sourceLabel).addEdge(sinkLabel)
        self.getVertex(sinkLabel)._outDegree += 1

    def vertexFind(self, sourceLabel: str):
        j = self.vertices.head

        if j is None:
            return False

        for i in range(self.vertices.nodes):
            if j._data._label == sourceLabel:
                return True
        return False

    def getVertex(self, sourceLabel: str):
        nextVertex = self.vertices.head

        while nextVertex is not None:
            if nextVertex._data._label == sourceLabel:
                return nextVertex._data
            nextVertex = nextVertex._next
        raise Exception("Vertex label not found")

    def getVertexCount(self):
        return self.vertices.nodes

    def getEdgeCount(self):
        sumOutDegree = 0
        nextVertex = self.vertices.head

        while nextVertex is not None:
            sumOutDegree += nextVertex._data()._outDegree

        return sumOutDegree

    def getAdjacentTo(self, sourceLabel: str):
        return self.getVertex(sourceLabel)._connections

    def getAdjacentFrom(self):
        raise NotImplementedError

    def isAdjacentTo(self,sourceLabel,  sinkLabel: str):
        if sinkLabel in self.getVertex(sinkLabel)._connections:
            return True
        return False

    def isAdjacentFrom(self):
        raise NotImplementedError

    def displayAsList(self):
        raise NotImplementedError

    def displayAsMatrix(self):
        raise NotImplementedError
