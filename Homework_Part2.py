import sqlite3

# Connecting to the database
connection = sqlite3.connect("ch17/books.db")
cursor = connection.cursor()


# 1. Select all authors' last names in descending order
cursor.execute("""
    SELECT last
    FROM authors
    ORDER BY last DESC
""")

print("Authors' last names in descending order:")
for author in cursor.fetchall():
    print(author[0])


# 2. Select all book titles in ascending order
cursor.execute("""
    SELECT title
    FROM titles
    ORDER BY title ASC
""")

print("\nBook titles in ascending order:")
for book in cursor.fetchall():
    print(book[0])


# 3. Select all books for a specific author using INNER JOIN
cursor.execute("""
    SELECT titles.title, titles.copyright, titles.isbn
    FROM titles
    INNER JOIN author_ISBN
        ON titles.isbn = author_ISBN.isbn
    INNER JOIN authors
        ON author_ISBN.id = authors.id
    WHERE authors.last = 'Deitel'
    ORDER BY titles.title ASC
""")

print("\nBooks by Deitel:")
for book in cursor.fetchall():
    print(book)


# 4. Insert a new author
cursor.execute("""
    INSERT INTO authors (first, last)
    VALUES ('John', 'Smith')
""")

connection.commit()

print("\nNew author added: Jim Smith")


# Get the ID of the new author
cursor.execute("""
    SELECT id
    FROM authors
    WHERE first = 'Jim' AND last = 'Smith'
""")



# 5. Insert a new title for the author
cursor.execute("""
    INSERT INTO titles (isbn, title, edition, copyright)
    VALUES ('034567890123', 'Ruby Programming', 1, '2026')
""")

connection.commit()

print("New title added: Ruby Programming")


# Close the database connection
connection.close()