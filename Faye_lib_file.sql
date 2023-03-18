create database Library;

use Library;

create table if not exists artist(
art_id smallint not null primary key auto_increment,
first_name varchar(70) not null,
last_name varchar(70) not null,
nationality varchar(70));

create table if not exists record_label(
rec_id smallint not null primary key auto_increment,
label_name varchar(70) not null);

create table if not exists genre(
genre_id smallint not null primary key auto_increment,
genre_name varchar(70) not null);

create table if not exists album(
album_id smallint not null primary key auto_increment,
album_name varchar(150) not null,
artist_id smallint not null, foreign key(artist_id) references artist(art_id),
album_genre_id smallint not null, foreign key(album_genre_id) references genre(genre_id),
record_label_id smallint, foreign key(record_label_id) references record_label(rec_id),
album_year year(4) );

create table if not exists customer(
cust_id smallint not null primary key auto_increment,
first_name varchar(70) not null,
last_name varchar(70) not null,
email varchar(70) not null,
mobile_num varchar(11),
address varchar(150),
postcode varchar(8),
join_date date);

create table if not exists loan_procedure(
loan_id smallint not null primary key auto_increment,
loan_album_id smallint not null, foreign key(loan_album_id) references album(album_id),
loan_cust_id smallint not null, foreign key(loan_cust_id) references customer(cust_id),
issue_date date,
due_back_date date);

insert into genre values(1, "Pop");
insert into genre values(2, "Country");
insert into genre values(3, "Folk Country");
insert into genre values(4, "Reggae");
insert into genre values(5, "Motown");
insert into genre values(6, "Dance");
insert into genre values(7, "RnB");
insert into genre values(8, "Indie");
insert into genre values(9, "Rock");
insert into genre values(10, "Folk");
insert into genre values(11, "Jazz");
insert into genre values(12, "Blues");
insert into genre values(13, "Classical");
insert into genre values(14, "Techno");

-- select * from genre;
insert into artist values(1, "Frankie", "Valli", "American");
insert into artist values(2, "Toots and the Maytals", "Toots and the Maytals", "Jamaican");
insert into artist values(3, "George", "Ezra", "English");
insert into artist values(4, "Diana", "Ross", "American");
insert into artist values(5, "Johnny", "Cash", "American");

insert into record_label values(1, "Rhino");
insert into record_label values(2, "V2");
insert into record_label values(3, "Sony Music");
insert into record_label values(4, "EMI");
insert into record_label values(5, "Columbia");
insert into record_label values(6, "PHILIPS");

insert into album values(1, "Working my way back to you", 1, 1, 1, 2011);
insert into album values(2, "True Love", 2, 4, 2, 2004);
insert into album values(3, "Gold Rush Kid", 3, 3, 3, 2022);
insert into album values(4, "One Woman", 4, 5, 4, 1993);
insert into album values(5, "At Folsom Prison", 5, 2, 3, 1968);
insert into album values(6, "Wanted on Voyage", 3, 3, 5, 2015);
insert into album values(7, "Staying at Tamara's", 3, 3, 5, 2018);
insert into album values(8, "Solo", 1, 1, 6, 1967);
insert into album values(9, "Workin' overtime", 4, 5, 4, 1989);

insert into customer values(1, "Faye", "Quinn", "fayequinn@email.com", "07836233821", "4 Blossom Hill", "WF4 6HT", "2018-03-12");
insert into customer values(2, "Bobby", "Smith", "bobbysmith@email.com", "07865752816", "87 Cherry Tree Drive", "WF5 6F1", "2018-04-18");
insert into customer values(3, "Carl", "Turner", "carlturner@email.com", "07652988789", "21 Magnolia Way", "WF3 3LT", "2019-01-05");
insert into customer values(4, "William", "Brooks", "williambrooks@warmmail.com", "07885990823", "43 Daffodil Drive", "LS3 0LY", "2014-07-16");
insert into customer values(5, "Louis", "Potter", "louispotter@email.com", "07889776542", "12 Tulip Close", "WF2 8LT", "2015-09-09");


