
drop database tharunraj;
create database tharunraj;
use tharunraj;
CREATE TABLE student (
    student_id INT not null AUTO_INCREMENT,
    name VARCHAR(25),
    age INT NOT NULL,
    gender varchar(25),
    Primary key (student_id)
);

create table orders(
	order_id int AUTO_INCREMENT,
    product varchar(35),
    student_id int,
    primary key (order_id),
    foreign key (student_id) references student(student_id)
);

ALTER table student
add phone varchar(10);

ALTER table student
modify column phone char(10) default "1234567890";

INSERT INTO student (name, age,gender) VALUES
('ram', 23,"male"),
('john', 24,"male"),
("neha",26,"female"),
("jack",32,"male");

INSERT INTO orders (product,student_id) values
("pro1",2),
("pro2",3),
("pro3",2);

CREATE UNIQUE INDEX index_name
ON student (name,age);

update student set age=34 where student_id=3;

select * from student where age>20 order by age asc;
select * from orders;
select min(age) from student;
select count(age) from student where age>23;
select sum(age) from student where age>23;
select avg(age) from student;
select * from student where name like	"%a%";
select name,age,student.student_id from student  join orders on student.student_id=orders.student_id;
select gender,count(gender) from student group by gender;