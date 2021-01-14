USE learnOnlineDB;
insert into  Teachers(first_name, last_name, e_mail, phone, likes, gender, aviable_after_lesson) 
values ("Gad", "Barak", "gadBarak@gmail.com", '0504120411' , 0, 'male', True );

USE learnOnlineDB;
insert into  Teachers(first_name, last_name, e_mail, phone, likes, gender, aviable_after_lesson) 
values  ("Chana", "Coen", "chana@gmail.com", '0554412014' , 0, 'female', False );

USE learnOnlineDB;
insert into  Teachers(first_name, last_name, e_mail, phone, likes, gender, aviable_after_lesson) 
values ("Mirian", "ben-shimon", "mBenS@gmail.com", '0522217745' , 0, 'female', True );



insert into Subjects ( description, category)
values ("Linear Algebra", 'Algebra'),
        ("Boolean Algebra", 'Algebra'),
        ("Article", 'English'),
        ("Writing", 'English'),
        ("c++", 'software'),
        ("python", 'software');

-- USE learnOnlineDB;
-- insert into SubjectsForTechers(teacher_id, subject_id)
-- values(10,1),
--        (10,2),
--        (10, 4),
--        (11,3), 
--        (11, 4),
--        (12,5),
--        (12,6)
USE learnOnlineDB;

select * from Teachers;

USE learnOnlineDB;

insert into  Teachers(first_name,last_name, e_mail,phone,gender, likes, aviable_after_lesson) 
                values ('aaa','yyy', 'yy@gmail.com','0504144488','male', 0 , 1)

USE learnOnlineDB;
update  Teachers
set likes  = 15
where id > 17 and id <23;


USE learnOnlineDB;
select * from teacher where likes >0
 
USE learnOnlineDB;insert into Comments values(default,1,"Awesome Teachers!","Explain to you how all this mistaken idea of math" ,"Jacques Philips","images/testi_02.png")
USE learnOnlineDB;insert into Comments values(default,1,"Great & Talented Teachers!","The great teacher I found here helped me a lot" ,"Venanda Mercy","images/testi_03.png")
USE learnOnlineDB;insert into Comments values(default,2,"Wondefull!","I've enjoy so much' and for free!!" ,"Yosef Cohen","images/testi_01.png")


use learnOnlineDB;
select id, description, category 
from SubjectsForTechers join Subjects on Subjects.id = SubjectsForTechers.subject_id
where  SubjectsForTechers.teacher_id=7;

use learnOnlineDB;
select * from SubjectsForTechers;
USE learnOnlineDB;
select Subjects.description, Subjects.category ,SubjectsForTechers.teacher_id, subject_id
                    from SubjectsForTechers join Subjects on SubjectsForTechers.subject_id = Subjects.id

select Subjects.description, Subjects.category , subject_id
from SubjectsForTechers join Subjects on SubjectsForTechers.subject_id = Subjects.id
where SubjectsForTechers.teacher_id = 55

USE learnOnlineDB;
select * from teachers;

USE learnOnlineDB;
select Subjects.description, Subjects.category , subject_id
                    from SubjectsForTechers join Subjects on SubjectsForTechers.subject_id = Subjects.id
                    where SubjectsForTechers.teacher_id  = 61

select * from SubjectsForTechers

where SubjectsForTechers.teacher_id =61
USE learnOnlineDB;

USE learnOnlineDB;

select * from teachers

USE learnOnlineDB;

select Subjects.description, Subjects.category , subject_id
                    from SubjectsForTechers join Subjects on SubjectsForTechers.subject_id = Subjects.id
                    where SubjectsForTechers.teacher_id=49

USE learnOnlineDB;insert into Comments values(default,32,"Awesome Teachers!","Explain to you how all this mistaken idea of math" ,"Jacques Philips","images/testi_02.png")
USE learnOnlineDB;insert into Comments values(default,32,"Great & Talented Teachers!","The great teacher I found here helped me a lot" ,"Venanda Mercy","images/testi_03.png")
USE learnOnlineDB;insert into Comments values(default,33,"Wondefull!","I've enjoy so much' and for free!!" ,"Yosef Cohen","images/testi_01.png")

USE learnOnlineDB;
update  Teachers
set likes  = 15
where id > 17 and id <23;


USE learnOnlineDB;
update  Teachers
set likes  = 12
where id > 23 and id <32;


USE learnOnlineDB;
update  Teachers
set likes  = 18
where id > 37 and id <40;


USE learnOnlineDB;
update  Teachers
set likes  = 45
where id =17;