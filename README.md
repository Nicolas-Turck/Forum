## for um in python with Bdd 
# use postgresql
The application has the following features:
- When the user launches the application, the home page displays all the messages contained in the database
- A message is presented with the name of the person who wrote it, 
the date of publication, the time of publication and his id
- The user can choose between viewing the messages (default action), 
writing a message or leaving the application
- When the user writes a message, we successively ask him the nickname 
he wants to use and the message he wants to post
Of course to store messages written by users and be able to find them later, 
you will save them in a PostgreSQL database.
This database will contain only one table: message, of which here is the structure.

id(integer, serial primary key, not null)
content(text, not nul) 
publishing_date(timestampz, not nul) 
author(varchar(50), not nul)