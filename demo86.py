class Layout(object):
    vias = ['v1', 'v2', 'v3']

    def __init__(self, layers):
        print("objec instinated")
        self.layers = layers
        pass

    def addLayer(self, layer_add):
        self.layers.append(layer_add)


l1 = Layout([1, 2, 3, 4])
l2 = Layout([5, 6, 7, 8])
l3 = Layout([1, 3, 5, 7])
print(l1.layers, l2.layers, l3.layers)
print(Layout.vias, l1.vias, l2.vias, l3.vias)
l1.vias.append('v4')
# l2.vias.append('v5')
print(Layout.vias, l1.vias, l2.vias, l3.vias)
l1.addLayer(10)
l2.addLayer(11)
l3.addLayer(12)
print(l1.layers, l2.layers, l3.layers)
