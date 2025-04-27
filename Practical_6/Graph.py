#
# Directional graph class implementation for practical 6
#


import LinkedList as LL


class DSAGraph():
    #----------- Private inner GraphNode class -----------#
    class _DSAGraphNode():
        def __init__(self, _label: str=None, _data=None):
            self._label = _label
            self._data = _data
            self._connections = LL.DSALinkedList()
            self._visited = False

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

        def _addConnection(self, edge: str):
            self._connections.insertLast(edge[1])

        def setVisited(self):
            self._visited = True

        def clearVisited(self):
            self._visited = False

        def getVisited(self):
            return self._visited

    #----------- Graph class -----------#
