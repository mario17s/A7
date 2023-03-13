# A7
You will be given one of the problems below to solve
The program must provide a menu-driven console user interface.
Use classes to represent the following:
The UI class which implements the user interface
A Services class that implements the required functionalities
The domain entity (complex, expense, student, book) class
A Repository class whose job it is to store the domain entity instances. This class will have three implementations: (1) a MemoryRepository, which stores domain instances in memory (just like in previous assignments); (2) a TextFileRepository, which persists domain entities to a text file, and (3) a BinaryFileRepository, which persists domain entities using object serialization with Pickle. You should be able to switch between which repository is in use by changing the instantiated class. When using a file-backed repository, changes made while running the program must be persisted across runs.
Have 10 programmatically generated entries in the application at start-up. Save these to the text/binary input files.
Unit tests and specifications for non-UI functions related to the first functionality.

2. Expenses
Manage a list of expenses. Each expense has a day (integer between 1 and 30), amount of money (positive integer) and expense type (string). Provide the following features:

Add an expense. Expense data is read from the console.
Display the list of expenses.
Filter the list so that it contains only expenses above a certain value read from the console.
Undo the last operation that modified program data. This step can be repeated. The user can undo only those operations made during the current run of the program.
