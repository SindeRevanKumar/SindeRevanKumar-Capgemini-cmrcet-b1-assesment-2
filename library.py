# You are building a Library Management System. 
# Create a `Book` class with properties like `title`, `author`, and `isbn`. 
# Write a method to display book details.
class Library:
    def details(self,isbn,title,book,author):
        self.isbn=isbn
        self.title=title
        self.book=book
        self.author=author
    def display(self):
        print(f"isbn:{self.isbn}\nname:{self.title}\nbook:{self.book}\nauthor:{self.author}")
num=int(input("Enter the isbn of book : "))
name=input("Enter the title of the book : ")
copies=int(input("Enter the number of copies avilable : "))
auth=input("Enter the author name : ")
c=Library()
c.details(num,name,copies,auth)
c.display()