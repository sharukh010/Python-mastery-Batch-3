# **Python Project: Student Management System**

**Difficulty:** Beginner to Intermediate

**Objective:** Build a menu-driven Student Management System using Python fundamentals without using Object-Oriented Programming.

## **Problem Statement**

Create an application that allows a teacher to manage student records, maintain academic information, calculate grades, and generate performance reports.

## **1. Application Menu**

Display the following menu whenever the application runs:

```
====================================
       STUDENT MANAGEMENT SYSTEM
====================================

1. Add Student
2. View All Students
3. Search Student
4. Update Student Details
5. Delete Student
6. Enter Student Marks
7. Calculate Student Grade
8. Display Class Performance
9. Display Topper
10. Display Subject Statistics
11. Generate Student Report
12. Exit

Enter your choice:
```

## **2. Functional Requirements**

**1. Add Student**

- Register a new student.
- Each student must have a unique ID.
- Store student ID, name, age, and marks.
- Do not allow duplicate student IDs.

**2. View All Students**

- Display all registered students.
- Display their ID, name, and age.
- Show an appropriate message if no students exist.

**3. Search Student**

- Search using student ID or name.
- Display complete student details when found.
- Display an error message when the student doesn't exist.

**4. Update Student Details**

- Search for a student using their ID.
- Allow updating the student's name and age.
- Do not allow modification of the student ID.

**5. Delete Student**

- Search using student ID.
- Delete the corresponding student record.
- Update the collection of registered student IDs.

**6. Enter Student Marks**

- Select a student using their ID.
- Display the available subjects.
- Allow entering marks for each subject.
- Marks must be between 0 and 100.

**7. Calculate Student Grade**

Calculate the total marks, average, and grade.

| Average  | Grade |
| -------- | ----- |
| 90–100   | A+    |
| 80–89    | A     |
| 70–79    | B     |
| 60–69    | C     |
| 50–59    | D     |
| Below 50 | F     |

A student must score at least 35 in every subject to pass.

**8. Display Class Performance**

Display:

- Total registered students.
- Number of passed students.
- Number of failed students.
- Overall class average.
- Highest average.
- Lowest average.

**9. Display Topper**

- Identify the student with the highest average.
- If multiple students have the same average, display all of them.

**10. Display Subject Statistics**

For each subject, display:

- Highest marks.
- Lowest marks.
- Average marks.
- Number of students passed.
- Number of students failed.

**11. Generate Student Report**

Generate a complete report containing:

- Student information.
- Subject-wise marks.
- Total marks.
- Average marks.
- Grade.
- Pass/fail status.

## **3. Technical Requirements**

Your application must use:

- Variables and data types.
- Functions with parameters and return values.
- Lists.
- Tuples.
- Sets.
- Dictionaries.
- Conditional statements.
- For and while loops.
- String manipulation methods.
- Type conversion.
- Exception handling.
- Built-in functions.

## **4. Additional Challenges**

After completing the main application, implement these features:

1. Sort students according to their average marks.
2. Display the top three students.
3. Search students using partial names.
4. Calculate the class pass percentage.
5. Identify duplicate student names using sets.
6. Validate all user inputs.
7. Handle situations where marks have not yet been entered.

**Your goal:** Build the entire application using functions and Python's built-in data structures.