<center> <h1>AirBnB clone - MySQL</h1> </center>

# Background Context

Environment variables will be your best friend for this project!

    HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
    HBNB_MYSQL_USER: the username of your MySQL
    HBNB_MYSQL_PWD: the password of your MySQL
    HBNB_MYSQL_HOST: the hostname of your MySQL
    HBNB_MYSQL_DB: the database name of your MySQL
    HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)

# Resources

Read or watch:

- [cmd module](https://docs.python.org/3/library/cmd.html)
- packages concept page
- [unittest module](https://docs.python.org/3/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [Python3 and environment variables](https://docs.python.org/3/library/os.html?highlight=env#os.getenv)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [AirBnB clone - ORM](https://www.youtube.com/watch?v=jeJwRB33YNg)

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/Elias-Dewa/AirBnB_clone_v2/tree/master/tests) | All class-defining modules are unittest |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel with kwargs | [/models/base_model.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) [/models/__init__.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/__init__.py) [/models/base_model.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/console.py) [/models/engine/file_storage.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) [/models/user.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/user.py) [/models/place.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/place.py) [/models/city.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/city.py) [/models/amenity.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/amenity.py) [/models/state.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/state.py) [/models/review.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/console.py) [/models/engine/file_storage.py](https://github.com/Elias-Dewa/AirBnB_clone_v2/blob/master/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:

```
/AirBnB_clone$ ./console.py
```

4. When this command is run the following prompt should appear:

```
(hbnb)
```

5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands

    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)

## <center><h1>Available commands and what they do</h1></center>

The recognizable commands by the interpreter are the following:

| Command         | Description                                                                                                                                                                                                                |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **quit or EOF** | Exits the program                                                                                                                                                                                                          |
| **Usage**       | By itself                                                                                                                                                                                                                  |
| **-----**       | **-----**                                                                                                                                                                                                                  |
| **help**        | Provides a text describing how to use a command.                                                                                                                                                                           |
| **Usage**       | By itself --or-- **help <command\>**                                                                                                                                                                                       |
| **-----**       | **-----**                                                                                                                                                                                                                  |
| **create**      | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`. Valid classes are: BaseModel, User, State, City, Amenity, Place, Review.                                                       |
| **Usage**       | **create <class name\>**                                                                                                                                                                                                   |
| **-----**       | **-----**                                                                                                                                                                                                                  |
| **show**        | Prints the string representation of an instance based on the class name and `id`                                                                                                                                           |
| **Usage**       | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**                                                                                                                                                          |
| **-----**       | **-----**                                                                                                                                                                                                                  |
| **destroy**     | Deletes an instance based on the class name and `id` (saves the change into a JSON file).                                                                                                                                  |
| **Usage**       | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)**                                                                                                                                                      |
| **-----**       | **-----**                                                                                                                                                                                                                  |
| **all**         | Prints all string representation of all instances based or not on the class name.                                                                                                                                          |
| **Usage**       | By itself or **all <class name\>** --or-- **<class name\>.all()**                                                                                                                                                          |
| **-----**       | **-----**                                                                                                                                                                                                                  |
| **update**      | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).                                                                                                 |
| **Usage**       | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)** |
| **-----**       | **-----**                                                                                                                                                                                                                  |
| **count**       | Retrieve the number of instances of a class.                                                                                                                                                                               |
| **Usage**       | **<class name\>.count()**                                                                                                                                                                                                  |
