class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}"

class Member(Person):
    def __init__(self, name, age, gender, membership_id):
        Person.__init__(self,name, age, gender)
        self.membership_id = membership_id
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}, with membership_id: {self.membership_id}."

class Author(Person):
    def __init__(self, name, age, gender, books_written):
        super().__init__(name, age, gender)
        self.books_written = books_written
    def introduce(self):
        return f"{super().introduce()}, books_written: {self.books_written}."
    def list_book(self):
        return str(self.books_written)

class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, membership_id, books_written):
        Member.__init__(self, name, age, gender, membership_id)
        Author.__init__(self, name, age, gender, books_written)
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}, with membership_id: {self.membership_id}. Book written: {self.books_written}."
author_member=AuthorMember("Long",18,"M",123, ["First book","Second book","Third book"])
print(author_member.introduce())
print(author_member.list_book())
author=Author("Minh",18,"M",["1","2","3"])
print(author.introduce())