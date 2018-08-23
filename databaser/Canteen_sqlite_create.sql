/*Creating database and tables*/
CREATE TABLE Owner 
(
	Owner_id integer PRIMARY KEY AUTOINCREMENT,
	Owner_name text
);

CREATE TABLE Canteen 
(
	Canteen_id integer PRIMARY KEY AUTOINCREMENT,
	Canteen_name text,
	Owner_id integer
);

CREATE TABLE Items 
(
	Items_id integer PRIMARY KEY AUTOINCREMENT,
	Items_name text,
	Item_type text
);

CREATE TABLE Has 
(
	Canteen_id integer,
	Items_id integer,
	Has_quantity integer,
	PRIMARY KEY (Canteen_id,Items_id),
	FOREIGN KEY (Canteen_id) REFERENCES Canteen(Canteen_id),
	FOREIGN KEY (Items_id) REFERENCES Items(Items_id)
);

/*Insert values */
insert into Owner(Owner_name) values ("Owner1");
insert into Owner(Owner_name) values ("Owner2");
insert into Owner(Owner_name) values ("Owner3");
insert into Owner(Owner_name) values ("Owner4");


insert into Canteen(Canteen_name,Owner_id) values ("Canteen1",1);
insert into Canteen(Canteen_name,Owner_id) values ("Canteen2",2);
insert into Canteen(Canteen_name,Owner_id) values ("Canteen3",3);
insert into Canteen(Canteen_name,Owner_id) values ("Canteen4",4);


insert into Items(Items_name,item_type) values ("Parle","Biscuit");
insert into Items(Items_name,item_type) values ("Fruit bowl","Fruit Salad");
insert into Items(Items_name,item_type) values ("Maggi","Noodles");
insert into Items(Items_name,item_type) values ("Yippe","Noodles");
insert into Items(Items_name,item_type) values ("Samosa","Fried snack");
insert into Items(Items_name,item_type) values ("Lays", "Snack");
insert into Items(Items_name,item_type) values ("Munch","Chocolate");

insert into Has(Canteen_id,Items_id,Has_quantity) values (1,1,20);
insert into Has(Canteen_id,Items_id,Has_quantity) values (1,2,10);
insert into Has(Canteen_id,Items_id,Has_quantity) values (1,3,15);
insert into Has(Canteen_id,Items_id,Has_quantity) values (1,4,3);
insert into Has(Canteen_id,Items_id,Has_quantity) values (1,5,3);
