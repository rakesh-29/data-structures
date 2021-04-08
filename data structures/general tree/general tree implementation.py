class treenode:

    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level=level+1
            p=p.parent
        return level

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def print_tree(self):
        spaces=" " * self.get_level() * 10
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root=treenode("Electronics")

    laptop=treenode("Laptop")
    laptop.add_child(treenode("Asus"))
    laptop.add_child(treenode("Microsoft"))
    laptop.add_child(treenode("Mac"))

    cellphone=treenode("cellphone")
    cellphone.add_child(treenode("Samsung"))
    cellphone.add_child(treenode("iphone"))
    cellphone.add_child(treenode("realme"))

    tv=treenode("Television")
    tv.add_child(treenode("Samsung"))
    tv.add_child(treenode("Sony"))
    tv.add_child(treenode("realme"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == "__main__":
    build_tree()
