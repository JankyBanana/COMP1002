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

        def _getLabel(self):
            return self._label

        def _getData(self):
            return self._data

        def _getNeighbours(self):
            return self._connections.values()

        def _getConnections(self):
            connectionList = LL.DSALinkedList()
            tempList = self._connections

            for i in range(self._connections.nodes):
                connectionList.insertLast(self._label + tempList.removeFirst())
            return connectionList

        def _addEdge(self, sink: str):
            self._inDegree += 1
            self._connections.insertLast(sink)

        def setVisited(self):
            self._visited = True

        def clearVisited(self):
            self._visited = False

        def getVisited(self):
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

        self.getVertex(sourceLabel)._addEdge(sinkLabel)
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
        tempList = self.vertices

        for i in range(self.vertices.nodes):
            if tempList.peekFirst()._getLabel == sourceLabel:
                return tempList.peekFirst()
            tempList.removeFirst()
        raise Exception("Vertex label not found")

    def getVertexCount(self):
        return self.vertices.nodes

    def getEdgeCount(self):
        sumOutDegree = 0
        tempList = self.vertices

        for i in range(self.vertices.nodes):
            sumOutDegree += tempList.removeFirst()._outDegree

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
