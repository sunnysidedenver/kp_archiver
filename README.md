Kp values are not readily archived in text-row format, which makes post-storm analysis difficult. This python script will pull 3 hourly Kp from a json file staged at swpc.services.gov every 5 hours and append to a '3hrKp' database (sqlite). The database can be accessed through a command interface or using DB Browser for SQLite (GUI app). 