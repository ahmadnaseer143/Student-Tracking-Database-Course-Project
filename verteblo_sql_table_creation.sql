-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2025-02-19 18:28:29.944

-- tables
-- Table: Assignments
CREATE TABLE Assignments (
    Assignment_ID int  NOT NULL,
    Title varchar(255)  NOT NULL,
    Due_Date Date  NOT NULL,
    Max_Score int  NOT NULL CHECK (Max_Score>0),
    Courses_Code varchar(10)  NOT NULL,
    CONSTRAINT Assignments_pk PRIMARY KEY (Assignment_ID)
);

-- Table: Attendance
CREATE TABLE Attendance (
    Attendance_ID int  NOT NULL,
    Attendance_Percentage int  NOT NULL CHECK (Attendance_Percentage>=0 and At=100tendance_Percentage<),
    Student_ID int  NOT NULL,
    Course_Code varchar(10)  NOT NULL,
    CONSTRAINT Attendance_pk PRIMARY KEY (Attendance_ID)
);

-- Table: Courses
CREATE TABLE Courses (
    Course_Code varchar(10)  NOT NULL,
    Course_Name varchar(255)  NULL,
    Credits int  NOT NULL CHECK (Credits>0),
    Teachers_ID int  NOT NULL,
    Department_ID int  NOT NULL,
    CONSTRAINT Courses_pk PRIMARY KEY (Course_Code)
);

-- Table: Departments
CREATE TABLE Departments (
    Department_ID int  NOT NULL,
    Name varchar(100)  NULL,
    Head varchar(100)  NOT NULL,
    CONSTRAINT Departments_pk PRIMARY KEY (Department_ID)
);

-- Table: Grades
CREATE TABLE Grades (
    Grade_ID int  NOT NULL,
    Assignment_Title varchar(255)  NOT NULL,
    Score int  NOT NULL CHECK (Score>0 And Score<=100),
    Assignment_ID int  NOT NULL,
    Student_ID int  NOT NULL,
    CONSTRAINT Grades_pk PRIMARY KEY (Grade_ID)
);

-- Table: Parents
CREATE TABLE Parents (
    Parent_ID int  NOT NULL,
    Name varchar(100)  NULL,
    Email varchar(255)  NULL,
    CONSTRAINT Parents_pk PRIMARY KEY (Parent_ID)
);

-- Table: Student_Course_Enrollment
CREATE TABLE Student_Course_Enrollment (
    Enrollment_ID int  NOT NULL,
    Enrollment_Date varchar(155)  NOT NULL,
    Course_Code varchar(10)  NOT NULL,
    Student_ID int  NOT NULL,
    CONSTRAINT Student_Course_Enrollment_pk PRIMARY KEY (Enrollment_ID)
);

-- Table: Students
CREATE TABLE Students (
    Student_ID int  NOT NULL,
    Name varchar(100)  NULL,
    Age int  NOT NULL CHECK (Age>5 and Age<26),
    Grade_Level varchar(55)  NOT NULL,
    Parent_ID int  NOT NULL,
    CONSTRAINT Students_pk PRIMARY KEY (Student_ID)
);

-- Table: Teachers
CREATE TABLE Teachers (
    Employee_ID int  NOT NULL,
    Name varchar(100)  NULL,
    Contact_Info varchar(255)  NULL,
    CONSTRAINT Teachers_pk PRIMARY KEY (Employee_ID)
);

-- foreign keys
-- Reference: Assignments_Courses (table: Assignments)
ALTER TABLE Assignments ADD CONSTRAINT Assignments_Courses FOREIGN KEY Assignments_Courses (Courses_Code)
    REFERENCES Courses (Course_Code);

-- Reference: Attendance_Courses (table: Attendance)
ALTER TABLE Attendance ADD CONSTRAINT Attendance_Courses FOREIGN KEY Attendance_Courses (Course_Code)
    REFERENCES Courses (Course_Code);

-- Reference: Attendance_Students (table: Attendance)
ALTER TABLE Attendance ADD CONSTRAINT Attendance_Students FOREIGN KEY Attendance_Students (Student_ID)
    REFERENCES Students (Student_ID);

-- Reference: Courses_Departments (table: Courses)
ALTER TABLE Courses ADD CONSTRAINT Courses_Departments FOREIGN KEY Courses_Departments (Department_ID)
    REFERENCES Departments (Department_ID);

-- Reference: Courses_Teachers (table: Courses)
ALTER TABLE Courses ADD CONSTRAINT Courses_Teachers FOREIGN KEY Courses_Teachers (Teachers_ID)
    REFERENCES Teachers (Employee_ID);

-- Reference: Grades_Assignments (table: Grades)
ALTER TABLE Grades ADD CONSTRAINT Grades_Assignments FOREIGN KEY Grades_Assignments (Assignment_ID)
    REFERENCES Assignments (Assignment_ID);

-- Reference: Grades_Students (table: Grades)
ALTER TABLE Grades ADD CONSTRAINT Grades_Students FOREIGN KEY Grades_Students (Student_ID)
    REFERENCES Students (Student_ID);

-- Reference: Student_Course_Enrollment_Courses (table: Student_Course_Enrollment)
ALTER TABLE Student_Course_Enrollment ADD CONSTRAINT Student_Course_Enrollment_Courses FOREIGN KEY Student_Course_Enrollment_Courses (Course_Code)
    REFERENCES Courses (Course_Code);

-- Reference: Student_Course_Enrollment_Students (table: Student_Course_Enrollment)
ALTER TABLE Student_Course_Enrollment ADD CONSTRAINT Student_Course_Enrollment_Students FOREIGN KEY Student_Course_Enrollment_Students (Student_ID)
    REFERENCES Students (Student_ID);

-- Reference: Students_Parents (table: Students)
ALTER TABLE Students ADD CONSTRAINT Students_Parents FOREIGN KEY Students_Parents (Parent_ID)
    REFERENCES Parents (Parent_ID);

-- End of file.

