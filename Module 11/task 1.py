class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class Book(Publication):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def print_information(self):
        print(f"Book: '{self.title}' by author: {self.author}, has {self.page_count} pages")
class Magazine(Publication):
    def __init__(self, title, author):
        super().__init__(title, author)
    def print_information(self):
        print(f"Magazine: '{self.title}' by chief editor: {self.author}")
book1=Book("Compartment No.6","Rosa Liksom", 192)
magazine1=Magazine("Donald Duck","Aki Hyyppä")
book1.print_information()
magazine1.print_information()