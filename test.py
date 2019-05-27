

class Ref:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("删除对象")
        del self.name


r = Ref(name="larry")
print(r.name)

del r
