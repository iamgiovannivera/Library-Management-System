# class Book:
#     def __init__(self, title, author, isbn, genre, publication_date, availability=True):
#         self.__title = title
#         self.__author = author
#         self.__isbn = isbn
#         self.__genre = genre
#         self.__publication_date = publication_date
#         self.__availability = availability

#     # Getters and setters
#     def get_title(self):
#         return self.__title

#     def set_title(self, title):
#         self.__title = title

#     def get_author(self):
#         return self.__author

#     def set_author(self, author):
#         self.__author = author

#     def get_isbn(self):
#         return self.__isbn

#     def set_isbn(self, isbn):
#         self.__isbn = isbn

#     def get_genre(self):
#         return self.__genre

#     def set_genre(self, genre):
#         self.__genre = genre

#     def get_publication_date(self):
#         return self.__publication_date

#     def set_publication_date(self, publication_date):
#         self.__publication_date = publication_date

#     def is_available(self):
#         return self.__availability

#     def set_availability(self, availability):
#         self.__availability = availability

#     def __str__(self):
#         return f"Title: {self.__title}, Author: {self.__author}, ISBN: {self.__isbn}, Genre: {self.__genre}, Publication Date: {self.__publication_date}, Availability: {'Available' if self.__availability else 'Borrowed'}"




# class User:
#     def __init__(self, name, library_id):
#         self.__name = name
#         self.__library_id = library_id
#         self.__borrowed_books = []

#     # Getters and setters
#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_library_id(self):
#         return self.__library_id

#     def set_library_id(self, library_id):
#         self.__library_id = library_id

#     def get_borrowed_books(self):
#         return self.__borrowed_books

#     def borrow_book(self, book):
#         self.__borrowed_books.append(book)

#     def return_book(self, book):
#         self.__borrowed_books.remove(book)

#     def __str__(self):
#         return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {', '.join([book.get_title() for book in self.__borrowed_books])}"






# class Author:
#     def __init__(self, name, biography):
#         self.__name = name
#         self.__biography = biography

#     # Getters and setters
#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_biography(self):
#         return self.__biography

#     def set_biography(self, biography):
#         self.__biography = biography

#     def __str__(self):
#         return f"Name: {self.__name}, Biography: {self.__biography}"







# class Genre:
#     def __init__(self, name, description, category):
#         self.__name = name
#         self.__description = description
#         self.__category = category

#     # Getters and setters
#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_description(self):
#         return self.__description

#     def set_description(self, description):
#         self.__description = description

#     def get_category(self):
#         return self.__category

#     def set_category(self, category):
#         self.__category = category

#     def __str__(self):
#         return f"Name: {self.__name}, Description: {self.__description}, Category: {self.__category}"



# 2. Inheritance Example



# class FictionBook(Book):
#     def __init__(self, title, author, isbn, genre, publication_date, availability=True):
#         super().__init__(title, author, isbn, genre, publication_date, availability)
    
#     def __str__(self):
#         return f"Fiction - {super().__str__()}"
    
    
    
    
    
# 3. Menu Operations






# def main_menu():
#     while True:
#         print("\nWelcome to the Library Management System!")
#         print("Main Menu:")
#         print("1. Book Operations")
#         print("2. User Operations")
#         print("3. Author Operations")
#         print("4. Genre Operations")
#         print("5. Quit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             book_operations()
#         elif choice == '2':
#             user_operations()
#         elif choice == '3':
#             author_operations()
#         elif choice == '4':
#             genre_operations()
#         elif choice == '5':
#             print("Exiting the system. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# def book_operations():
#     # Implement book operations menu and corresponding actions
#     pass

# def user_operations():
#     # Implement user operations menu and corresponding actions
#     pass

# def author_operations():
#     # Implement author operations menu and corresponding actions
#     pass

# def genre_operations():
#     # Implement genre operations menu and corresponding actions
#     pass

# if __name__ == "__main__":
#     main_menu()
    
    
    
    
# 4. Implementing Menu Actions






# def book_operations():
#     while True:
#         print("\nBook Operations:")
#         print("1. Add a new book")
#         print("2. Borrow a book")
#         print("3. Return a book")
#         print("4. Search for a book")
#         print("5. Display all books")
#         print("6. Back to main menu")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             add_new_book()
#         elif choice == '2':
#             borrow_book()
#         elif choice == '3':
#             return_book()
#         elif choice == '4':
#             search_book()
#         elif choice == '5':
#             display_all_books()
#         elif choice == '6':
#             break
#         else:
#             print("Invalid choice. Please try again.")

# def add_new_book():
#     # Implement the logic to add a new book
#     pass

# def borrow_book():
#     # Implement the logic to borrow a book
#     pass

# def return_book():
#     # Implement the logic to return a book
#     pass

# def search_book():
#     # Implement the logic to search for a book
#     pass

# def display_all_books():
#     # Implement the logic to display all books
#     pass