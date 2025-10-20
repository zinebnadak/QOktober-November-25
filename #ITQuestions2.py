DATABASES

Without databases, none of the IT systems we rely on could function reliably and efficiently.
In this course, we cover the fundamental principles of databases in both theory and practice.
We focus primarily on relational databases and the SQL query language, but we also get acquainted with document databases.

1. Database
Question: What is a database and why is it important in managing data?

2. Table (Relation)
Question: What is a table in a relational database, and how does it organize data?

3. Row (Tuple)
Question: What is a row (or tuple) in a relational database, and what kind of information does it represent?

4. Column (Attribute)
Question: What is the role of a column (attribute) in a relational database table, and how is it defined?

5. Primary Key (PK)
Question: What is a primary key, and why must it be unique in every row of a table?

6. Foreign Key (FK)
Question: How does a foreign key create a relationship between two tables in a relational database?

7. Domain
Question: What is a domain in the context of a relational database, and how does it affect the values a column can hold?

8. Cardinality
Question: What are the three types of cardinality in database relationships, and how do they impact how tables are related?

9. Normalization
Question: What is the purpose of database normalization, and how does it improve the structure of the data?

10. SQL (Structured Query Language)
Question: What is SQL, and what role does it play in interacting with relational databases?

11. Unique Key
Question: How does a unique key differ from a primary key, and when might it be used?

12. Index
Question: What is an index in a database, and how does it improve data retrieval performance?

13. NULL
Question: What does a NULL value represent in a relational database, and how does it differ from an empty string or zero?

14. Relationship Between Tables
Question: How do relationships between tables (e.g., one-to-one, one-to-many, many-to-many) help organize data in a relational database?

15. Schema
Question: What is a database schema, and what does it define in terms of table structure and relationships?

16. Transactions
Question: What is a transaction in a database, and what are the key properties that ensure its reliability (ACID)?

17. SQL Joins
Question: What is the difference between an INNER JOIN, LEFT JOIN, and RIGHT JOIN in SQL, and how are they used to retrieve data from multiple tables?

18. Composite Key
Question: What is a composite key, and when would you use multiple columns to create a primary key?

19. Candidate Key
Question: What is a candidate key, and how is it different from a primary key in a relational database?

20. Alternate Key
Question: What is an alternate key, and how does it relate to the candidate keys in a database table?

21. Superkey
Question: What is a superkey, and how is it related to a primary key in terms of uniquely identifying a record?

22. Natural Key
Question: What is a natural key, and what are the advantages and disadvantages of using it in a relational database?

23. Surrogate Key
Question: What is a surrogate key, and why might it be used in place of a natural key or composite key?

Each question corresponds to a key concept in relational databases and SQL. These can help you reinforce your understanding of database management, structure, and relationships. Let me know if you'd like more detail on any of these!

Du sade:
and the answer to it

ChatGPT sade:
Sure! Here are the answers to the questions based on the terms and concepts related to databases and SQL:

1. Database
Question: What is a database and why is it important in managing data? Answer: A database is a structured collection of data that is stored and managed to allow for easy retrieval, modification, and organization. It is important because it helps store large amounts of data efficiently, maintain data integrity, and provide a method for querying and analyzing the data.

2. Table (Relation)
Question: What is a table in a relational database, and how does it organize data? Answer: A table in a relational database is a collection of data organized into rows (records) and columns (attributes). Each row represents a record, and each column represents an attribute of that record. Tables allow you to structure and store data logically.

3. Row (Tuple)
Question: What is a row (or tuple) in a relational database, and what kind of information does it represent? Answer: A row (or tuple) is a single, complete record in a table, representing a unique entity or instance. For example, in a "Customers" table, each row might represent a single customer with attributes like CustomerID, Name, and Email.

4. Column (Attribute)
Question: What is the role of a column (attribute) in a relational database table, and how is it defined? Answer: A column (attribute) in a table defines a specific type of data stored for each record. For instance, in a "Users" table, columns might include Username, Email, and DateOfBirth. Each column has a defined data type (e.g., VARCHAR, INT, DATE).

5. Primary Key (PK)
Question: What is a primary key, and why must it be unique in every row of a table? Answer: A primary key is a column or a set of columns that uniquely identifies each row in a table. It must be unique and cannot contain NULL values to ensure that every record is distinct and can be efficiently accessed or referenced.

6. Foreign Key (FK)
Question: How does a foreign key create a relationship between two tables in a relational database? Answer: A foreign key is a column in one table that references the primary key of another table. This relationship links data between the two tables, ensuring referential integrity by making sure the data in the foreign key column corresponds to an existing value in the referenced table.

7. Domain
Question: What is a domain in the context of a relational database, and how does it affect the values a column can hold? Answer: A domain is the set of allowable values for a given column. It defines the valid range of values that can be stored in that column, such as specifying that a Age column can only hold integer values between 0 and 150 or that an Email column should follow a specific pattern.

8. Cardinality
Question: What are the three types of cardinality in database relationships, and how do they impact how tables are related? Answer:
* One-to-One (1:1): Each record in one table is related to exactly one record in another table.
* One-to-Many (1:M): One record in a table can be related to many records in another table.
* Many-to-Many (M:N): Multiple records in one table can be related to multiple records in another table (often managed by a junction table). Cardinality defines how tables are linked and the type of relationship they share.

9. Normalization
Question: What is the purpose of database normalization, and how does it improve the structure of the data? Answer: Normalization is the process of organizing data to reduce redundancy and improve data integrity. By dividing large tables into smaller ones and establishing relationships between them, normalization minimizes duplication, ensures consistency, and makes the database easier to maintain.

10. SQL (Structured Query Language)
Question: What is SQL, and what role does it play in interacting with relational databases? Answer: SQL is a standard programming language used to manage and manipulate relational databases. It allows you to create, read, update, and delete data (CRUD operations), as well as define the structure of the database (e.g., CREATE TABLE, ALTER TABLE), and query data (e.g., SELECT).

11. Unique Key
Question: How does a unique key differ from a primary key, and when might it be used? Answer: A unique key ensures that all values in a column are distinct, similar to a primary key. However, unlike a primary key, a unique key can allow NULL values (unless otherwise restricted). It's useful when you need to enforce uniqueness for a column but don't want it to be the primary identifier for records.

12. Index
Question: What is an index in a database, and how does it improve data retrieval performance? Answer: An index is a database object that improves the speed of data retrieval operations by creating a data structure (often a tree or hash) to quickly locate records. It's like an index in a book, making searches faster but slightly slower when inserting or updating data.

13. NULL
Question: What does a NULL value represent in a relational database, and how does it differ from an empty string or zero? Answer: A NULL value represents the absence of a value or unknown data. It is different from an empty string ("") or zero (0), which are valid data entries. NULL is used to indicate missing or undefined data.

14. Relationship Between Tables
Question: How do relationships between tables (e.g., one-to-one, one-to-many, many-to-many) help organize data in a relational database? Answer: Relationships define how data in one table is related to data in another. They help avoid redundancy, enforce integrity, and make it possible to query data across multiple tables. For example, a one-to-many relationship links a customer to multiple orders, while a many-to-many relationship links students to multiple courses through a junction table.

15. Schema
Question: What is a database schema, and what does it define in terms of table structure and relationships? Answer: A schema is the logical design or blueprint of a database, including the tables, columns, relationships, and constraints. It defines the structure and organization of the data, ensuring that all data is stored consistently and efficiently.

16. Transactions
Question: What is a transaction in a database, and what are the key properties that ensure its reliability (ACID)? Answer: A transaction is a sequence of database operations that are executed as a single unit. The ACID properties ensure reliability:
* Atomicity: All operations in a transaction must succeed or fail together.
* Consistency: The database moves from one valid state to another.
* Isolation: Transactions are isolated from one another.
* Durability: Once committed, changes are permanent.

17. SQL Joins
Question: What is the difference between an INNER JOIN, LEFT JOIN, and RIGHT JOIN in SQL, and how are they used to retrieve data from multiple tables? Answer:
* INNER JOIN: Returns only rows with matching values in both tables.
* LEFT JOIN: Returns all rows from the left table and matched rows from the right table (if no match, NULL is returned for the right).
* RIGHT JOIN: Similar to LEFT JOIN, but returns all rows from the right table and matched rows from the left. These joins are used to combine rows from two or more tables based on a related column.


KEYS 


^18. Primary Key (PK)
Question: What is the purpose of a primary key in a relational database, and what are its key properties? Answer: The primary key uniquely identifies each row in a table. Its key properties are:
* Uniqueness: The primary key column must contain unique values for every row.
* Non-NULL: A primary key cannot contain NULL values, ensuring that every row has a unique identifier.
* One per table: A table can only have one primary key, but this can consist of one or more columns (composite key).

^19. Foreign Key (FK)
Question: How does a foreign key work in a relational database, and what does it enforce? Answer: A foreign key is a column (or set of columns) in one table that links to the primary key of another table. It establishes a relationship between the two tables, such as one-to-many or many-to-many. The foreign key enforces referential integrity, meaning the value in the foreign key column must exist in the referenced table. It can allow NULL values, indicating an optional relationship.

20. Unique Key
Question: What is a unique key, and how does it differ from a primary key? Answer: A unique key ensures that all values in a column are unique, similar to a primary key. However, it differs in that:
* A unique key can allow NULL values (unless explicitly restricted).
* A table can have multiple unique keys, but only one primary key. Unique keys are often used to enforce uniqueness on attributes like emails, usernames, or product codes.

21. Composite Key
Question: What is a composite key, and when is it necessary to use one? Answer: A composite key is a primary key that consists of two or more columns. It is used when a single column cannot uniquely identify a record, such as in many-to-many relationships. For example, in a "CourseEnrollments" table, the combination of StudentID and CourseID may serve as a composite key.

^22. Candidate Key
Question: What is a candidate key, and how does it relate to the primary key? Answer: A candidate key is any column or set of columns that can uniquely identify a row in a table. A table can have multiple candidate keys, but only one is selected to be the primary key. All candidate keys must have unique values and cannot be NULL, but only one is chosen to represent the record uniquely.

23. Alternate Key
Question: What is an alternate key, and how is it different from a primary key? Answer: An alternate key is a candidate key that was not chosen as the primary key. While a table can have multiple candidate keys, only one is selected as the primary key, and the others become alternate keys. Alternate keys help ensure data integrity and can still serve as unique identifiers for records.

24. Superkey
Question: What is a superkey, and how does it differ from a primary key? Answer: A superkey is a set of columns that can uniquely identify a row in a table. It can include the primary key and any additional columns that aren’t necessary for uniqueness. Every primary key is a superkey, but not every superkey is a primary key, as superkeys may contain extra, redundant columns.

25. Natural Key
Question: What is a natural key, and what are the advantages and disadvantages of using one? Answer: A natural key is a key that is derived from real-world data, such as a Social Security Number or ISBN. The advantage is that it is meaningful and easy to understand. However, natural keys can be problematic because they may change over time (e.g., a person's address or email), making them less stable and reliable than surrogate keys.

26. Surrogate Key
Question: What is a surrogate key, and why would you choose to use one instead of a natural key or composite key? Answer: A surrogate key is a system-generated key (often an auto-incremented number or GUID) used to uniquely identify a record. It has no business meaning and is typically used when natural keys are cumbersome, unreliable, or subject to change. Surrogate keys provide a stable and efficient means of uniquely identifying records.

27. Primary Key vs Foreign Key
Question: What is the difference between a primary key and a foreign key in relational databases? Answer: A primary key uniquely identifies a record within its own table, while a foreign key is a column (or set of columns) in one table that points to the primary key in another table. The primary key ensures that each record in its table is unique, while the foreign key establishes a relationship between tables.

28. Composite Key vs Primary Key
Question: When would you use a composite key rather than a primary key in a table? Answer: A composite key is used when no single column can uniquely identify a record. It’s necessary in cases where two or more columns together provide uniqueness. This typically happens in junction tables (many-to-many relationships), where a combination of attributes (like StudentID and CourseID) uniquely identifies records.

29. Surrogate Key vs Natural Key
Question: Why would you choose a surrogate key over a natural key? Answer: A surrogate key is chosen over a natural key when the natural key is either:
* Too cumbersome or complex (e.g., a combination of multiple columns),
* Prone to change (e.g., email addresses, phone numbers), or
* Not optimal for database efficiency. A surrogate key is stable, easy to generate, and simplifies database design, as it does not rely on real-world attributes.

30. Unique Key vs Primary Key
Question: How is a unique key different from a primary key, and in what situations would you use each? Answer: Both unique keys and primary keys ensure that column values are unique. However:
* A primary key is the main identifier for records and cannot contain NULL values.
* A unique key also enforces uniqueness but can allow NULL values (unless restricted). You would use a primary key for the column that uniquely identifies records, and a unique key to enforce uniqueness on other important attributes (like an email address or username).
