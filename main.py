class library:

    def __init__(self, list_of_books, name_lib):
        self.list_of_books = list_of_books
        self.library_name = name_lib
        self.record = {}

    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        print("book added successfully")

    def lend_book(self, book, user):
        self.list_of_books.remove(book)
        self.record[user] = book

    def display_book(self):
        print("current books in dictionary are :")
        print(self.list_of_books)

    def return_book(self, re_book, re_user):
        self.list_of_books.append(re_book)
        del self.record[re_user]


harry = library(["a", "b", "c", "d", "e"], "ayush_library")

want_to_continue = "yes"
while want_to_continue == "yes":
    print("want you want to do ?")
    print("1.add a book\n"
          "2.lend a book\n"
          "3.display all books\n"
          "4.return book")
    print("\n")
    choice = int(input("enter your choice : "))
    if choice == 1:
        bookname = input("enter book name : ")
        harry.add_book(bookname)
    elif choice == 3:
        harry.display_book()
    elif choice == 2:
        harry.display_book()
        lend_book = input("enter the name of book you want to lend :")
        if lend_book in harry.list_of_books:
            lend_user = input("enter name of lender : ")
            harry.lend_book(lend_book, lend_user)
        else:
            print("sorry the current book is not available at the moment ")
            print("currently the book is owned by ", end=" ")
            for i in harry.record:
                if harry.record[i] == lend_book:
                    print(i)
        print("current books available now are : ", harry.list_of_books)
        print("current record of lenders are : ", harry.record)
    elif choice == 4:
        print("current record of lenders are : ", harry.record)
        return_book = input("enetr the name of the book you are returning ? :")
        return_user = input("enter name of user who is returning:")
        if return_user in harry.record.keys() or return_book in harry.record.values():
            harry.return_book(return_book, return_user)
            print("current books available now are : ", harry.list_of_books)
            print("current record of lenders are : ", harry.record)
        else:
            print("sorry no data found in lenders account")

    want_to_continue = input("want to remain in the system :(yes/no)")
