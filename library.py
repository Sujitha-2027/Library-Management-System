import mysql.connector

# Database Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your password",
    database="library"
)
mycursor = mydb.cursor()

class Library:

    def display_books(self):
        mycursor.execute("SELECT * FROM books")
        data = mycursor.fetchall()

        print("\nAvailable Books:")
        for row in data:
            print(row)

    def borrow_book(self, book_name):

        mycursor.execute(
            "SELECT status FROM books WHERE book_name=%s",
            (book_name,)
        )

        data = mycursor.fetchone()

        if data and data[0] == "Available":

            mycursor.execute(
                "UPDATE books SET status='Borrowed' WHERE book_name=%s",
                (book_name,)
            )

            mydb.commit()

            print(f"\nYou have borrowed '{book_name}'")

        else:
            print("\nBook not available")

    def return_book(self, book_name):

        mycursor.execute(
            "UPDATE books SET status='Available' WHERE book_name=%s",
            (book_name,)
        )

        mydb.commit()

        print(f"\n'{book_name}' returned successfully")


obj = Library()

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        obj.display_books()

    elif option == 2:
        book = input("Enter book name to borrow: ")
        obj.borrow_book(book)

    elif option == 3:
        book = input("Enter book name to return: ")
        obj.return_book(book)

    elif option == 4:
            import pyttsx3
            text_speech = pyttsx3.init()
            text_speech.say("Thank you for visiting the library!")
            text_speech.runAndWait()
            print("Thank you for visiting the Library!")
            break

    else:
        print("Invalid Option!")
