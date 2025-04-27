#
# Directional graph class implementation for practical 6
#


import LinkedList as LL


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
        self.vertices = LL.DSALinkedList()

    def vertexFind(self, label: str):
        tempList = self.vertices

        for i in range(self.vertices.nodes):
            if tempList.removeFirst()._getLabel == label:
                return True
        return False

    def addVertex(self, label: str, data=None):
        if self.vertexFind(label):
            raise ValueError("Vertex label already in use")

        self.vertices.insertLast(self._DSAGraphVertex(label, data))

    def addEdge(self, sourceLabel: str, sinkLabel: str):
        sourceVertex = self.getVertex(sourceLabel)

        if self.vertexFind(sourceLabel) == False:
            raise Exception("Source vertex not found")
        elif sourceVertex._connections.find(sinkLabel):
            raise Exception("Edge between these vertices already exists")

        self.getVertex(sourceLabel)._addEdge(sinkLabel)
        self.getVertex(sinkLabel)._outDegree += 1

    def getVertex(self, label: str):
        tempList = self.vertices

        for i in range(self.vertices.nodes):
            if tempList.peekFirst()._getLabel == label:
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

    def getAdjacentTo(self):
        pass

    def getAdjacentFrom(self):
        pass

    def isAdjacentTo(self):
        pass

    def isAdjacentFrom(self):
        pass

    def displayAsList(self):
        pass

    def displayAsMatrix(self):
        pass