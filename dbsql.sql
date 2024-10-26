create table user(
    userid integer primary key autoincrement, 
    username text not null, 
    password text not null,
    email text not null,
    nickname text not null,
    create_at timestamp default CURRENT_TIMESTAMP
);

-- 데이터를 삽입하기 위한 SQL
--insert into user(username,password)
--values('test','123','test@gmail.com','male')

--테이블 삭제
--drop table user