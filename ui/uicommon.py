from collections import namedtuple


def emptyLayout(layout):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)


StructItem = namedtuple("StructItem", ["offset", "name", "struct"])
