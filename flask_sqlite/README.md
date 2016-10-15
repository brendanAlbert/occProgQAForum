# a simple flask database app :shipit:

 ~ Code credit belongs to: [tutorialspoint.com/flask](https://www.tutorialspoint.com/flask/flask_sqlite.htm)
 

## steps to take before this code will work for you:
#### 1. setting up python3 and flask
- [x] 1. install [python3](https://www.python.org/downloads/release/python-352/)
- [ ] 2. at the command line or terminal, type ```  pip3 install Flask  ```
- [ ] 3. make a directory/folder to store all these files in

#### 2. set up the sqlite database 
- [ ] 1. open the terminal/cmd line and navigate to the directory/folder you will be storing these files in.
- [ ] 2. create the database by typing ```  sqlite3 database.db  ```
- [ ] 3. if it worked, you should see something like "SQLite version 3.8.10.2 2015-05-20 ... Enter ".help" for usage hints"
- [ ] 4. time to create a table in the database. type ```  create table students (name TEXT, addr TEXT, city TEXT, pin TEXT); ```
- [ ] 5. now if you type ```  .tables  ``` and you see "students" appear, you're ready to [rock](https://www.tutorialspoint.com/flask/flask_sqlite.htm)

#### 3. running the app

##### for mac
- [x] in the terminal, make sure you are inside your <flask_app> folder
- [ ] Use ``` cd <directory_name>``` to move across and further into your directories / folders
- [ ] Use ``` cd .. ``` to go back up a directory
- [ ] Use ``` ls ``` to list the files in your current directory
- [ ] Use ``` pwd ``` to **p**rint **w**orking **d**irectory


##### for windows
- [ ] in the command line, make sure you are inside your <flask_app> folder/directory.
For our purposes here, the only command that is different between the mac terminal and windows command line
is ``` dir ```  this is windows version of mac's ``` ls ```

##### command to type to start the app
Using your computer's respective command line, you can proceed once you are in the directory containing your start.py file
Type ``` python3 start.py ```
If all is well you should see
```
* Running on http://127.0.0.1:5000/ (Press CTRL-C to quit)
* Restarting with stat
* Debugger is active
* Debugger pin code: ...
```
Go to ``` http://127.0.0.1:5000/ ``` in your browser, and check that the app works!

If it works for you, Congrats! :moneybag:


## file directory structure
### the layout of your flask_app folder should look like this:


```
flask_app
   templates
     home.html
     list.html
     student.html
     result.html
 start.py
```
