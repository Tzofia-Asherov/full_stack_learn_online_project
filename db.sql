create database learnOnlineDB;

USE learnOnlineDB;
CREATE TABLE Teachers
(
    id INT NOT NULL  PRIMARY KEY AUTO_INCREMENT,
    first_name  VARCHAR(30) NOT NULL,
    last_name  VARCHAR(30),
    e_mail   VARCHAR(40) NOT null,
    phone VARCHAR(10),
    likes INT,
    gender ENUM('male', 'female'),
    aviable_after_lesson BIT
);

USE learnOnlineDB;
CREATE TABLE Subjects
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    description VARCHAR(50) NOT NULL,
    category VARCHAR(40) NOT NULL
);


USE learnOnlineDB;
CREATE TABLE SubjectsForTechers
(
    teacher_id INT NOT NULL,
    subject_id INT NOT NULL,

    FOREIGN KEY(teacher_id) REFERENCES Teachers(id),
    FOREIGN KEY(subject_id) REFERENCES Subjects(id),
    PRIMARY KEY (teacher_id,subject_id)
);

-- USE learnOnlineDB;
-- drop table SubjectsForTechers

-- USE learnOnlineDB;
-- drop table Subjects

-- USE learnOnlineDB;
-- drop table Teachers
USE learnOnlineDB;
select * from SubjectsForTechers
USE learnOnlineDB;

SELECT * from Teachers
where aviable_after_lesson = false


USE learnOnlineDB;
select * from Subjects
USE learnOnlineDB;
CREATE TABLE Comments
(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    teacher_id INT NOT NULL,
	
    title VARCHAR(40),
    descriptions  VARCHAR(200),
    student_name VARCHAR(40),
    img VARCHAR(100),
    FOREIGN KEY(teacher_id) REFERENCES Teachers(id)
);
