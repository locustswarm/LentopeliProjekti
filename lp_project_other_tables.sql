create table game(
ID int not null  auto_increment,
co2_consumed int(8),
co2_budget int(8),
gamertag varchar(30),
location varchar(40),
moneys int(8), 
primary key(id),
foreign key (location) references airport(ident)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table boss(
ID int not null auto_increment,
boss_hp int(8),
boss_fight int(1),
likes_apples varchar(40),
name varchar(40),
primary key(ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
create table boss_reached(
game_id int,
boss_id int,
primary key(game_ID, boss_ID),
foreign key(game_id) references game(ID),
foreign key(boss_id) references boss(ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table airport_cleared(
game_ID int,
airport_ident varchar(10),
primary key(game_ID, airport_ident),
foreign key(game_id) references game(id),
foreign key(airport_ident) references airport(ident)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table country_unlock(
game_id int,
iso_country varchar(40),
primary key(game_ID, iso_country),
foreign key(game_id) references game(id),
foreign key(iso_country) references country(iso_country)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
alter table airport add foreign key (iso_country) references country(iso_country); 
