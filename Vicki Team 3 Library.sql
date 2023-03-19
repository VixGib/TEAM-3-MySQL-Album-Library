-- hello TEAM 3!!

-- User stories
-- As a Member I want to be able to:
	-- Borrow an Album
	-- Search for an Album by Artist
	-- Search for any Album by Any Name
	-- View my History
	-- Check my Due Dates
    
-- As the Lending system I want to be able to:
	-- Check Availability
    -- To see Whos is Borrowing what
    -- To be able to Contact a Member

CREATE DATABASE Library;
USE Library;
CREATE TABLE if not exists artist(
art_id smallint not null primary key auto_increment,
first_name varchar(70)not null,
last_name varchar(70)not null,
nationality varchar(70));

CREATE TABLE if not exists record_label(
rec_id smallint not null primary key auto_increment,
label_name varchar(70)not null);

CREATE TABLE if not exists genre(
genre_id smallint not null primary key auto_increment,
genre_name varchar(70)not null);

CREATE TABLE if not exists album(
album_id smallint not null primary key auto_increment,
album_name varchar(150)not null,
artist_id smallint not null,
FOREIGN KEY(artist_id) REFERENCES artist(art_id),
album_genre_id smallint not null,
FOREIGN KEY (album_genre_id) REFERENCES genre(genre_id),
record_label_id smallint,
FOREIGN KEY (record_label_id) REFERENCES record_label(rec_id),
album_year year(4));

CREATE TABLE if not exists customer(
cust_id smallint not null primary key auto_increment,
first_name varchar(70)not null,
last_name varchar(70)not null,
email varchar(70) not null,
mobile_num varchar(11),
addrss varchar(150),
postcode varchar(8),
join_date date);

CREATE TABLE if not exists loan_procedure(
loan_id smallint not null primary key auto_increment,
loan_album_id smallint not null,
FOREIGN KEY (loan_album_id) REFERENCES album(album_id),
loan_cust_id smallint not null,
FOREIGN KEY (loan_cust_id) REFERENCES customer (cust_id),
issue_date date,
due_back_date date );

-- Genre data

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

-- Faye's Record Label
insert into record_label values(1, "Rhino");
insert into record_label values(2, "V2");
insert into record_label values(3, "Sony Music");
insert into record_label values(4, "EMI");
insert into record_label values(5, "Columbia");
insert into record_label values(6, "PHILIPS");

-- Vicki's Record label data

insert into record_label values(7, "RCA Records");
insert into record_label values(8, "LA Face Records");
insert into record_label values(9, "Virgin Records");
insert into record_label values(10, "Deconstruction Records");
insert into record_label values(11, "Fly Eye Records");
insert into record_label values(12, "Columbia");

-- Rachel's Record Label
insert into record_label values(13, "Roc Nation Records");
insert into record_label values(14, "Chrysalis Records Limited");
insert into record_label values(15, "More Alarming Records");
insert into record_label values(16, "Silvertone Records Limited");
insert into record_label values(17, "Westbury Road Roc Nation");


-- Fays's Artists data
insert into artist values(1, "Frankie", "Valli", "American");
insert into artist values(2, "Toots and the Maytals", "Toots and the Maytals", "Jamaican");
insert into artist values(3, "George", "Ezra", "English");
insert into artist values(4, "Diana", "Ross", "American");
insert into artist values(5, "Johnny", "Cash", "American");

-- Vicki's Artist data

insert into artist values(6, "Pink", "Pink", "American");
insert into artist values(7, "Phil", "Collins", "English");
insert into artist values(8, "Take That", "Take That", "English");
insert into artist values(9, "Calvin", "Harris", "Scotish");

-- Rachel Artist data
insert into artist values(10, "The Stone Roses", "The Stone Roses");
insert into artist values(11, "Rihanna", "Rihanna");
insert into artist values(12, "Laura", "Marling");

-- Faye's Album data
insert into album values(1, "Working my way back to you", 1, 1, 1, 2011);
insert into album values(2, "True Love", 2, 4, 2, 2004);
insert into album values(3, "Gold Rush Kid", 3, 3, 3, 2022);
insert into album values(4, "One Woman", 4, 5, 4, 1993);
insert into album values(5, "At Folsom Prison", 5, 2, 3, 1968);
insert into album values(6, "Wanted on Voyage", 3, 3, 5, 2015);
insert into album values(7, "Staying at Tamara's", 3, 3, 5, 2018);
insert into album values(8, "Solo", 1, 1, 6, 1967);
insert into album values(9, "Workin' overtime", 4, 5, 4, 1989);

-- Vicki's Album data

insert into album values(10, "All I Know So Far", 6, 1, 7, 2021);
insert into album values(11, "Fun House", 6, 1, 8, 2008);
insert into album values(12, "No Jacket Required", 7, 1, 9, 1985);
insert into album values(13, "Never Forget", 8, 1, 7, 2005);
insert into album values(14, "18 Months", 9, 6, 10, 2012);

-- Rachel's Album data
insert into album values(15, "The Stone Roses" , 10, 8, 16, 1989);
insert into album values(16, "Loud" , 11, 7, 13, 1989);
insert into album values(17, "Anti" , 11, 7, 17, 1989);
insert into album values(18, "Song for our Daughter", 12, 10, 15, 1989);
insert into album values(19, "Semper Femina", 12, 10, 14, 1989);


-- Faye's Customer data
insert into customer values(1, "Faye", "Quinn", "fayequinn@email.com", "07836233821", "4 Blossom Hill", "WF4 6HT", "2018-03-12");
insert into customer values(2, "Bobby", "Smith", "bobbysmith@email.com", "07865752816", "87 Cherry Tree Drive", "WF5 6F1", "2018-04-18");
insert into customer values(3, "Carl", "Turner", "carlturner@email.com", "07652988789", "21 Magnolia Way", "WF3 3LT", "2019-01-05");
insert into customer values(4, "William", "Brooks", "williambrooks@warmmail.com", "07885990823", "43 Daffodil Drive", "LS3 0LY", "2014-07-16");
insert into customer values(5, "Louis", "Potter", "louispotter@email.com", "07889776542", "12 Tulip Close", "WF2 8LT", "2015-09-09");

-- Vicki's Customer data

insert into customer values(6, "Vicki", "Gibbison", "vickigibbison@hotmail.com", "07967806688", "85 Shakespeare Drive", "SK82DQ", "2011-08-11");
insert into customer values(7, "Phil", "Brown", "philbrown@sky.com", "07856935628", "52 Ash Road", "WA167RP", "2014-02-28");
insert into customer values(8, "Carloine", "Pickle", "carolinepickle@skyemail.com", "07478930266", "91 Purple Drive", "BL48UT", "2020-07-25");
insert into customer values(9, "Andrew", "Wallis", "andrewwallis@aol.com", "07784602275", "1 Hill Avenue", "WA3 5PZ", "2016-11-12");
insert into customer values(10, "Lois", "Travis", "loistravis@gmail.com", "07620853399", "14 Parsonage Close", "M28 3PT", "2019-01-30");

-- Rachel' Customer data
insert into customer values(11, "John", "Barnes", "jb@gmail.com", "07783888555", "5 The Row", "BL1 5LJ", 2022-06-21);
insert into customer values(12, "Jenna", "Wade", "jennagirl@gmail.com", "07885101295", "15 Walton avenue", "TS5 7RN", 2023-01-21);
insert into customer values(13, "Evelyn", "Boomer", "eve45@btconnect.com", "07234661660", "Rose Cottage", "HX6 1DG", 2023-01-30);
insert into customer values(14, "Dave", "Glynn", "dglynn@yahoo.co.uk", "07885101295", "15 Walton avenue", "TS5 7RN", 2022-01-21);
