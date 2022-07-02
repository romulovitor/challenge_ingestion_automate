drop table if exists examples;

create table `examples` (
  `id` int not null auto_increment,
  `name` varchar(80) default null,
  primary key (`id`)
);

CREATE TABLE `coordinate` (
   `id` int not null auto_increment,
   `name` varchar(200) not null,
   `age` int not null,
   `city` varchar(200) not null,
   `interest1` varchar(200),
   `interest3` varchar(200),
   `interest4` varchar(200),
   `phone_number` varchar(50) not null,
   primary key (`id`)
);