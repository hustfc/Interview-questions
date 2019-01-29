class Sample:
    def __enter__(self):
        print("__enter__()方法")
        return "Foo"

    def __exit__(self, type, value, trace):
        print("__exit__()方法")
def get_sample():
    return Sample()
with get_sample() as aaa:
    print(aaa)