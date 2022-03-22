create table Pathway(
	pathway_id int primary key);

create table Enroll(
	enroll_id int primary key);

create table Progress(
	progress_id int primary key);

create table Endpoint(
	endpoint_id int primary key);

create table Availability(
	availability_id int primary key);

create table State(
	state_id int primary key);

create table Uses(
	uses_id int primary key);

create table Recovery(
	recovery_id int primary key);

create table if not exists Resource (
	resource_id int primary key);
