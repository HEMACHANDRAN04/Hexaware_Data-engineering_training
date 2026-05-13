CREATE DATABASE course_tracker;
USE course_tracker;

CREATE TABLE students(
student_id INT PRIMARY KEY,
student_name VARCHAR(100),
email VARCHAR(100),
join_date DATE
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    instructor VARCHAR(100),
    duration_weeks INT
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE progress (
    progress_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    completion_percentage INT,
    last_updated DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO students VALUES
(1,'Arun','arun@gmail.com','2025-01-10'),
(2,'Priya','priya@gmail.com','2025-01-11'),
(3,'Karthik','karthik@gmail.com','2025-01-12'),
(4,'Meena','meena@gmail.com','2025-01-13'),
(5,'Rahul','rahul@gmail.com','2025-01-14'),
(6,'Sneha','sneha@gmail.com','2025-01-15'),
(7,'Vikram','vikram@gmail.com','2025-01-16'),
(8,'Divya','divya@gmail.com','2025-01-17'),
(9,'Rohit','rohit@gmail.com','2025-01-18'),
(10,'Anjali','anjali@gmail.com','2025-01-19');

INSERT INTO courses VALUES
(101,'Python Basics','John',6),
(102,'SQL Mastery','David',4),
(103,'Data Engineering','Smith',8),
(104,'Machine Learning','Andrew',10),
(105,'Cloud Computing','Raj',5),
(106,'Power BI','Kumar',3),
(107,'Java Programming','Alex',7),
(108,'Web Development','Chris',6),
(109,'DevOps','Michael',5),
(110,'PySpark','Daniel',4);

INSERT INTO enrollments VALUES
(1,1,101,'2025-02-01','Active'),
(2,2,102,'2025-02-02','Completed'),
(3,3,103,'2025-02-03','Active'),
(4,4,104,'2025-02-04','Dropped'),
(5,5,105,'2025-02-05','Completed'),
(6,6,106,'2025-02-06','Active'),
(7,7,107,'2025-02-07','Completed'),
(8,8,108,'2025-02-08','Dropped'),
(9,9,109,'2025-02-09','Active'),
(10,10,110,'2025-02-10','Completed');

INSERT INTO progress VALUES
(1,1,101,45,'2025-03-01'),
(2,2,102,100,'2025-03-02'),
(3,3,103,65,'2025-03-03'),
(4,4,104,20,'2025-03-04'),
(5,5,105,100,'2025-03-05'),
(6,6,106,55,'2025-03-06'),
(7,7,107,100,'2025-03-07'),
(8,8,108,15,'2025-03-08'),
(9,9,109,40,'2025-03-09'),
(10,10,110,100,'2025-03-10');

INSERT INTO students VALUES
(11,"Eve","eve69@gmail.com",'2025-01-20');

SELECT * FROM students;

UPDATE progress
SET  completion_percentage=75
WHERE progress_id=1;

DELETE FROM students WHERE student_id=11;

DELIMITER //

CREATE PROCEDURE GetCompletionPercentage(IN sid INT)
BEGIN
    SELECT
        student_id,
        AVG(completion_percentage) AS avg_completion
    FROM progress
    WHERE student_id = sid
    GROUP BY student_id;
END //

DELIMITER ;

CALL GetCompletionPercentage(4);

CREATE INDEX idx_student
ON enrollments(student_id);

CREATE INDEX idx_course
ON enrollments(course_id);