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


