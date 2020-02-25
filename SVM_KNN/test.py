class text:
    def hi(self):
        print("hi")
    def by(self):
        self.hi()
        print("h")
if __name__ == "__main__":
    obj=text()
    obj.by()
