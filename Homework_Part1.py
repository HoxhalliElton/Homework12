import sqlite3
import pandas as pd

# Connecting to the database
connection = sqlite3.connect('ch17/books.db')

# Printing all the authors
pd.options.display.max_columns = 10
authors =  pd.read_sql('SELECT * FROM authors', connection,
            index_col=['id'])
print(authors)
print()
print()

# Printing all the book titles
titles = pd.read_sql('SELECT * FROM titles', connection)
print(titles)
print()
print()

# Printing all the ISBN numbers
isbn = pd.read_sql('SELECT * FROM author_ISBN', connection)
print(isbn)
print()
print()

# Printing authors first and last names
author_first_last = pd.read_sql('SELECT first, last FROM authors', connection)
print(author_first_last)
print()
print()

# Printing the books whose copyright is later than 2016
copyrights = pd.read_sql("""SELECT title, edition, copyright
                            FROM titles
                            WHERE copyright > '2016' """, connection)
print(copyrights)
print()
print()

# Printing the authors whose last name starts with the letter D
matching_ch = pd.read_sql(""" SELECT id, first, last
                              FROM authors
                              WHERE last LIKE 'D%' """, connection, index_col=['id'])
print(matching_ch)
print()
print()

# Printing the authors whose first name has a least one letter B
matching_any_ch = pd.read_sql(""" SELECT id, first, last
                              FROM authors
                              WHERE first LIKE '_b%' """, connection, index_col=['id'])
print(matching_any_ch)
print()
print()

# Printing the book titles in ascending order
titles_asc = pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)
print(titles_asc)
print()
print()

# Printing the authors names ordering it by first name and then last name
column_order_by = pd.read_sql(""" SELECT id, first, last
                                  FROM authors
                                  ORDER BY first, last """,
                                  connection, index_col=['id'])
print(column_order_by)
print()
print()

# Printing the authors names ordering it by last name in descending order
# and then first name in ascending order
column_order_by_desc = pd.read_sql(""" SELECT id, first, last
                                  FROM authors
                                  ORDER BY last DESC, first ASC """,
                                  connection, index_col=['id'])
print(column_order_by_desc)
print()
print()

# Printing the book titles who have "How to Program" on their title
where_query = pd.read_sql(""" SELECT isbn, title, edition, copyright
                              FROM titles
                              WHERE title LIKE '%How to Program'
                              ORDER BY title """, connection)
print(where_query)
print()
print()


# Doing an inner join between authors table and author_ISBN table
inner_join = pd.read_sql(""" SELECT first, last, isbn
                             FROM authors
                             INNER JOIN author_ISBN
                                ON authors.id = author_ISBN.id
                             ORDER BY last, first """, connection).head()
print(inner_join)
print()
print()


cursor = connection.cursor()

# Inserting a new author into the database
cursor.execute("""INSERT INTO authors (first, last)
                  VALUES ('Sue', 'Red')""")

# Seeing the changes made into the database
authors_new = pd.read_sql('SELECT id, first, last FROM authors',
                          connection, index_col=['id'])
print(authors_new)
print()
print()

# Modifying the last name of an author
cursor = cursor.execute("""UPDATE authors SET last='Black'
                           WHERE last='Red' AND first='Sue'""")

# Seeing the changes made into the database
authors_changed = pd.read_sql('SELECT id, first, last FROM authors',
                          connection, index_col=['id'])
print(authors_changed)
print()
print()

# Deleting the author whose ID number is 6
cursor = cursor.execute('DELETE FROM authors WHERE id=6')

# Seeing the changes made into the database
authors_change = pd.read_sql('SELECT id, first, last FROM authors',
                             connection, index_col=['id'])
print(authors_change)
print()
print()

# Printing the book titles in descending order by their edition
titles_desc = pd.read_sql("""SELECT title, edition FROM titles
                                      ORDER BY edition DESC""", connection).head(3)
print(titles_desc)
print()
print()

# Printing the authors whose first name starts with the letter A
author_start_with_a = pd.read_sql("""SELECT * FROM  authors
                                     WHERE first LIKE 'A%' """, connection)
print(author_start_with_a)
print()
print()

# Closing the connection to the database
connection.close()